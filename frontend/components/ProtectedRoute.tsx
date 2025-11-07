"use client";

import { useRouter } from "next/navigation";
import { useEffect } from "react";

import { useAuth } from "../hooks/useAuth";

type ProtectedRouteProps = {
  children: React.ReactNode;
};

export function ProtectedRoute({ children }: ProtectedRouteProps) {
  const { session, loading } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!loading && !session) {
      router.push("/login");
    }
  }, [loading, session, router]);

  if (!session) {
    return <p style={{ padding: "2rem" }}>Checking authentication…</p>;
  }

  return <>{children}</>;
}
