import React from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { Button } from "./ui/button";
import { Users, MessageSquare, PlusCircle, List, LogOut } from "lucide-react";
import { useAuth } from "@/contexts/AuthContext";

const Sidebar: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { user, logout } = useAuth();
  const userName = user?.name || "User";

  const isActive = (path: string) => {
    return location.pathname === path;
  };

  const handleLogout = async () => {
    await logout();
    navigate("/login");
  };

  const navItems = [
    // {
    //   title: "Dashboard",
    //   href: "/dashboard",
    //   icon: <LayoutDashboard className="w-5 h-5" />,
    // },
    {
      title: "Patients",
      href: "/patients",
      icon: <Users className="w-5 h-5" />,
      subItems: [
        {
          title: "View Patients",
          href: "/patients",
          icon: <List className="w-4 h-4" />,
        },
        {
          title: "Add Patient",
          href: "/patients/new",
          icon: <PlusCircle className="w-4 h-4" />,
        },
      ],
    },
    {
      title: "AI Assistant",
      href: "/chatbot",
      icon: <MessageSquare className="w-5 h-5" />,
    },
  ];

  return (
    <div className="w-64 h-screen bg-background border-r fixed left-0 top-0 flex flex-col">
      <div className="p-6 flex-grow">
        <h1 className="text-2xl font-bold mb-8">Dental Clinic</h1>
        <div className="mb-8">
          <p className="text-muted-foreground">Welcome,</p>
          <p className="font-semibold">{userName}</p>
        </div>
        <nav className="space-y-2">
          {navItems.map((item) => (
            <div key={item.href}>
              <Link to={item.href}>
                <Button
                  variant={isActive(item.href) ? "secondary" : "ghost"}
                  className="w-full justify-start gap-2"
                >
                  {item.icon}
                  {item.title}
                </Button>
              </Link>
              {item.subItems && (
                <div className="ml-6 mt-2 space-y-1">
                  {item.subItems.map((subItem) => (
                    <Link key={subItem.href} to={subItem.href}>
                      <Button
                        variant={isActive(subItem.href) ? "secondary" : "ghost"}
                        className="w-full justify-start gap-2"
                        size="sm"
                      >
                        {subItem.icon}
                        {subItem.title}
                      </Button>
                    </Link>
                  ))}
                </div>
              )}
            </div>
          ))}
        </nav>
      </div>
      <div className="p-6 border-t">
        <Button
          variant="ghost"
          className="w-full justify-start gap-2 text-muted-foreground hover:text-foreground"
          onClick={handleLogout}
        >
          <LogOut className="w-5 h-5" />
          Logout
        </Button>
      </div>
    </div>
  );
};

export default Sidebar;
