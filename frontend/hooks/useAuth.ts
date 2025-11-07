"use client";

import { createContext, useContext, useEffect, useMemo, useState } from "react";
import { Session, createClientComponentClient } from "@supabase/auth-helpers-nextjs";

const AuthContext = createContext<{ session: Session | null; loading: boolean }>({ session: null, loading: true });

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const supabase = useMemo(() => createClientComponentClient(), []);
  const [session, setSession] = useState<Session | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    supabase.auth.getSession().then(({ data }) => {
      setSession(data.session ?? null);
      setLoading(false);
    });

    const { data: listener } = supabase.auth.onAuthStateChange((_event, newSession) => {
      setSession(newSession ?? null);
      setLoading(false);
    });

    return () => {
      listener.subscription.unsubscribe();
    };
  }, [supabase]);

  return <AuthContext.Provider value={{ session, loading }}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  return useContext(AuthContext);
}
