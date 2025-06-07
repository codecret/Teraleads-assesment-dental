import {
  createContext,
  useContext,
  useState,
  useEffect,
  ReactNode,
} from "react";
import {
  User,
  login as loginApi,
  register as registerApi,
  logout as logoutApi,
} from "@/lib/auth";
import { getAuthHeader, getToken } from "@/lib/token";
import { API_URL } from "@/config";

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (name: string, email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if user is logged in on mount
    const checkAuth = async () => {
      try {
        const token = getToken();
        console.log("Current token:", token); // Debug log

        const response = await fetch(`${API_URL}/api/auth/me`, {
          headers: {
            ...getAuthHeader(),
            "Content-Type": "application/json",
          },
          credentials: "include",
        });

        console.log("Auth response status:", response.status); // Debug log

        if (response.ok) {
          const userData = await response.json();
          setUser(userData);
        } else {
          const errorData = await response.json();
          console.error("Auth error:", errorData); // Debug log
        }
      } catch (error) {
        console.error("Auth check failed:", error);
      } finally {
        setLoading(false);
      }
    };

    checkAuth();
  }, []);

  const login = async (email: string, password: string) => {
    const user = await loginApi({ email, password });
    setUser(user);
  };

  const register = async (name: string, email: string, password: string) => {
    const user = await registerApi({
      name,
      email,
      password,
      confirmPassword: password,
    });
    setUser(user);
  };

  const logout = async () => {
    await logoutApi();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
}
