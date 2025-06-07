import React from "react";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  children,
  className = "",
  ...props
}) => {
  return (
    <button
      className={`${className} disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-200`}
      {...props}
    >
      {children}
    </button>
  );
};
