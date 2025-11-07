import type { Metadata } from "next";
import "./globals.css";
import { AuthProvider } from "../hooks/useAuth";

export const metadata: Metadata = {
  title: "Supabase CRM",
  description: "Full-stack CRM platform powered by FastAPI and Supabase"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-slate-950 text-slate-100">
        <AuthProvider>{children}</AuthProvider>
      </body>
    </html>
  );
}
