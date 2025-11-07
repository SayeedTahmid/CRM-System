"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { FormEvent, useState } from "react";

import { supabaseClient } from "../../../lib/supabaseClient";
import { apiFetch } from "../../../lib/api";

export default function RegisterPage() {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const email = formData.get("email") as string;
    const password = formData.get("password") as string;
    const fullName = formData.get("name") as string;
    const company = formData.get("company") as string;

    const { data, error: signUpError } = await supabaseClient.auth.signUp({ email, password, options: { data: { full_name: fullName } } });
    if (signUpError) {
      setError(signUpError.message);
      return;
    }

    try {
      await apiFetch("/auth/register", {
        method: "POST",
        body: { email, password, full_name: fullName, company_name: company }
      });
      router.push("/login");
    } catch (err) {
      setError((err as Error).message);
    }
  };

  return (
    <main style={{ display: "grid", placeItems: "center", minHeight: "100vh", padding: "2rem" }}>
      <form onSubmit={handleSubmit} className="card" style={{ width: "100%", maxWidth: "420px" }}>
        <h2>Create your workspace</h2>
        <label style={{ display: "grid", gap: "0.5rem" }}>
          <span>Name</span>
          <input name="name" type="text" required style={inputStyle} />
        </label>
        <label style={{ display: "grid", gap: "0.5rem", marginTop: "1rem" }}>
          <span>Company</span>
          <input name="company" type="text" required style={inputStyle} />
        </label>
        <label style={{ display: "grid", gap: "0.5rem", marginTop: "1rem" }}>
          <span>Email</span>
          <input name="email" type="email" required style={inputStyle} />
        </label>
        <label style={{ display: "grid", gap: "0.5rem", marginTop: "1rem" }}>
          <span>Password</span>
          <input name="password" type="password" required style={inputStyle} />
        </label>
        {error && <p style={{ color: "#f87171", fontSize: "0.9rem" }}>{error}</p>}
        <button type="submit" className="btn-primary" style={{ marginTop: "1.5rem" }}>
          Create account
        </button>
        <p style={{ marginTop: "1rem", fontSize: "0.85rem", color: "rgba(226,232,240,0.7)" }}>
          Already have an account? <Link href="/login">Sign in</Link>
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
