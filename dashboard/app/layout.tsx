import type { Metadata } from "next";
import "./globals.css";
import { QueryProvider } from "@/components/providers/query-provider";
import { AppShell } from "@/components/layout/app-shell";

export const metadata: Metadata = {
  title: "AI Software Factory",
  description: "Operational dashboard for autonomous software delivery"
};

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <QueryProvider>
          <AppShell>{children}</AppShell>
        </QueryProvider>
      </body>
    </html>
  );
}

