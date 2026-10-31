"use client";

import { useEffect, useState } from "react";
import { useTheme } from "fumadocs-ui/provider/base";
import { Moon, Sun } from "lucide-react";

export function ThemeToggle() {
  const { resolvedTheme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

  useEffect(() => setMounted(true), []);

  return (
    <button
      type="button"
      className="atlas-theme-toggle"
      disabled={!mounted}
      aria-label="Dark mode"
      aria-pressed={mounted && resolvedTheme === "dark"}
      title="Toggle light or dark mode"
      onClick={() => setTheme(resolvedTheme === "dark" ? "light" : "dark")}
    >
      <Moon className="atlas-theme-moon" size={20} aria-hidden="true" />
      <Sun className="atlas-theme-sun" size={20} aria-hidden="true" />
    </button>
  );
}
