import { useState } from "react";
import PatientList from "@/components/PatientList";
import PatientForm from "@/components/PatientForm";
import Chatbot from "@/components/Chatbot";
import { Button } from "@/components/ui/button";
import { useAuth } from "@/contexts/AuthContext";

interface Patient {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  phone: string;
  date_of_birth: string;
  address: string;
  medical_history: string;
}

export function Dashboard() {
  const [showForm, setShowForm] = useState(false);
  const [selectedPatient, setSelectedPatient] = useState<Patient | null>(null);
  const { logout } = useAuth();

  const handleEditPatient = (patientId: number) => {
    setSelectedPatient({
      id: patientId,
      first_name: "",
      last_name: "",
      email: "",
      phone: "",
      date_of_birth: "",
      address: "",
      medical_history: "",
    });
    setShowForm(true);
  };

  const handleFormSuccess = () => {
    setShowForm(false);
    setSelectedPatient(null);
  };

  const handleFormCancel = () => {
    setShowForm(false);
    setSelectedPatient(null);
  };

  return (
    <div className="min-h-screen bg-background">
      <header className="border-b">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <h1 className="text-3xl font-bold tracking-tight">
            Dental Clinic Dashboard
          </h1>
          <Button variant="outline" onClick={logout}>
            Logout
          </Button>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div className="space-y-6">
            <div className="flex justify-between items-center">
              <h2 className="text-2xl font-semibold tracking-tight">
                Patient Management
              </h2>
              <Button
                onClick={() => {
                  setSelectedPatient(null);
                  setShowForm(true);
                }}
                size="sm"
              >
                Add New Patient
              </Button>
            </div>

            {showForm ? (
              <PatientForm
                patient={selectedPatient}
                onSuccess={handleFormSuccess}
                onCancel={handleFormCancel}
              />
            ) : (
              <PatientList onEditPatient={handleEditPatient} />
            )}
          </div>

          <div className="space-y-6">
            <h2 className="text-2xl font-semibold tracking-tight">
              AI Assistant
            </h2>
            <Chatbot />
          </div>
        </div>
      </main>
    </div>
  );
}
