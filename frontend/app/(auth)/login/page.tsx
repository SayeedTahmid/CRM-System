"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { FormEvent, useState } from "react";

import { supabaseClient } from "../../../lib/supabaseClient";

export default function LoginPage() {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const email = formData.get("email") as string;
    const password = formData.get("password") as string;
    const { error } = await supabaseClient.auth.signInWithPassword({ email, password });
    if (error) {
      setError(error.message);
      return;
    }
    router.push("/");
  };

  return (
    <main style={{ display: "grid", placeItems: "center", minHeight: "100vh", padding: "2rem" }}>
      <form onSubmit={handleSubmit} className="card" style={{ width: "100%", maxWidth: "420px" }}>
        <h2>Log in to CRM</h2>
        <label style={{ display: "grid", gap: "0.5rem" }}>
          <span>Email</span>
          <input name="email" type="email" required style={inputStyle} />
        </label>
        <label style={{ display: "grid", gap: "0.5rem", marginTop: "1rem" }}>
          <span>Password</span>
          <input name="password" type="password" required style={inputStyle} />
        </label>
        {error && <p style={{ color: "#f87171", fontSize: "0.9rem" }}>{error}</p>}
        <button type="submit" className="btn-primary" style={{ marginTop: "1.5rem" }}>
          Sign in
        </button>
        <p style={{ marginTop: "1rem", fontSize: "0.85rem", color: "rgba(226,232,240,0.7)" }}>
          Need an account? <Link href="/register">Create one</Link>
        </p>
      </form>
    </main>
  );
}

const inputStyle: React.CSSProperties = {
  background: "rgba(15,23,42,0.7)",
  border: "1px solid rgba(148,163,184,0.2)",
  borderRadius: "12px",
  padding: "0.75rem 1rem",
  color: "white"
};
