import { ActivityPanel } from "@/components/layout/activity-panel";
import { Sidebar } from "@/components/layout/sidebar";

type AppShellProps = {
  children: React.ReactNode;
};

export function AppShell({ children }: AppShellProps) {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <div className="flex min-h-screen">
        <Sidebar />
        <div className="flex min-w-0 flex-1">
          <div className="min-w-0 flex-1 px-4 py-5 sm:px-6 lg:px-8">{children}</div>
          <ActivityPanel />
        </div>
      </div>
    </div>
  );
}

