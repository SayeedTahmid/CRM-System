"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const links = [
  { href: "/", label: "Dashboard" },
  { href: "/contacts", label: "Contacts" },
  { href: "/pipeline", label: "Pipeline" },
  { href: "/activities", label: "Activities" }
];

const baseButton = {
  borderRadius: "999px",
  padding: "0.5rem 1.25rem",
  textTransform: "uppercase" as const,
  fontSize: "0.75rem",
  letterSpacing: "0.12em",
  transition: "background 0.2s ease, color 0.2s ease"
};

export function Navigation() {
  const pathname = usePathname();

  return (
    <nav
      style={{
        display: "flex",
        alignItems: "center",
        gap: "1.5rem",
        padding: "1.75rem 2rem",
        background: "rgba(15,23,42,0.6)",
        borderBottom: "1px solid rgba(168,85,247,0.2)",
        position: "sticky",
        top: 0,
        backdropFilter: "blur(10px)",
        zIndex: 10
      }}
    >
      <span style={{ fontSize: "1.25rem", fontWeight: 600, color: "var(--purple-500)" }}>Supabase CRM</span>
      <div style={{ display: "flex", alignItems: "center", gap: "0.75rem" }}>
        {links.map((link) => {
          const active = pathname === link.href;
          return (
            <Link
              key={link.href}
              href={link.href}
              style={{
                ...baseButton,
                background: active ? "linear-gradient(120deg, var(--purple-900), var(--purple-500))" : "rgba(30,41,59,0.9)",
                color: active ? "white" : "rgba(226,232,240,0.75)"
              }}
            >
              {link.label}
            </Link>
          );
        })}
      </div>
    </nav>
  );
}
