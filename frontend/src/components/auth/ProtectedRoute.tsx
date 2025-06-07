import { ReactNode } from "react";
import { Navigate } from "react-router-dom";
import { getToken } from "../../lib/token";

interface ProtectedRouteProps {
  children: ReactNode;
}

export default function ProtectedRoute({ children }: ProtectedRouteProps) {
  const token = getToken();
  console.log(token);

  if (!token) {
    // Redirect to login if there's no token
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
}
