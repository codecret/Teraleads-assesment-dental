import {
  BrowserRouter as Router,
  Routes,
  Route,
  useNavigate,
  useParams,
} from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";
import { ProtectedRoute } from "./components/ProtectedRoute";
import LoginForm from "./components/auth/LoginForm";
import RegisterForm from "./components/auth/RegisterForm";
import PatientList from "./components/PatientList";
import PatientForm from "./components/PatientForm";
import Chatbot from "./components/Chatbot";
import Dashboard from "./components/Dashboard";
import {
  QueryClient,
  QueryClientProvider,
  useQuery,
} from "@tanstack/react-query";
import { API_URL } from "./config";

const queryClient = new QueryClient();

function PatientFormWrapper() {
  const navigate = useNavigate();
  const { id } = useParams();
  const token = localStorage.getItem("token");

  const {
    data: patient,
    isLoading,
    error,
  } = useQuery({
    queryKey: ["patient", id],
    queryFn: async () => {
      if (!id) return null;
      if (!token) {
        navigate("/login");
        return null;
      }

      const response = await fetch(`${API_URL}/api/v1/patients/${id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      });

      if (response.status === 401) {
        localStorage.removeItem("token");
        navigate("/login");
        return null;
      }

      if (!response.ok) {
        throw new Error("Failed to fetch patient data");
      }

      return response.json();
    },
    enabled: !!id,
  });

  const handleFormSuccess = () => {
    queryClient.invalidateQueries({ queryKey: ["patients"] });
    navigate("/patients");
  };

  const handleFormCancel = () => {
    navigate("/patients");
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div className="text-destructive">{error.message}</div>;
  }

  return (
    <PatientForm
      patient={patient}
      onSuccess={handleFormSuccess}
      onCancel={handleFormCancel}
    />
  );
}

function AppRoutes() {
  const navigate = useNavigate();

  const handleEditPatient = (id: number) => {
    navigate(`/patients/${id}`);
  };

  const handleFormSuccess = () => {
    queryClient.invalidateQueries({ queryKey: ["patients"] });
    navigate("/patients");
  };

  const handleFormCancel = () => {
    navigate("/patients");
  };

  return (
    <Routes>
      <Route path="/login" element={<LoginForm />} />
      <Route path="/register" element={<RegisterForm />} />
      <Route
        path="/"
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        }
      />
      <Route
        path="/patients"
        element={
          <ProtectedRoute>
            <PatientList onEditPatient={handleEditPatient} />
          </ProtectedRoute>
        }
      />
      <Route
        path="/patients/new"
        element={
          <ProtectedRoute>
            <PatientForm
              patient={null}
              onSuccess={handleFormSuccess}
              onCancel={handleFormCancel}
            />
          </ProtectedRoute>
        }
      />
      <Route
        path="/patients/:id"
        element={
          <ProtectedRoute>
            <PatientFormWrapper />
          </ProtectedRoute>
        }
      />
      <Route
        path="/chatbot"
        element={
          <ProtectedRoute>
            <Chatbot />
          </ProtectedRoute>
        }
      />
    </Routes>
  );
}

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <AuthProvider>
          <AppRoutes />
        </AuthProvider>
      </Router>
    </QueryClientProvider>
  );
}

export default App;
