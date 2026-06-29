import { Activity, Boxes, CircleAlert, GitPullRequest, Server, Workflow } from "lucide-react";
import { StatusBadge } from "@/components/status-badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const metrics = [
  { label: "Projects", value: "0", icon: Boxes, tone: "text-cyan-700" },
  { label: "Running Workers", value: "0", icon: Server, tone: "text-emerald-700" },
  { label: "Running Graphs", value: "0", icon: Workflow, tone: "text-violet-700" },
  { label: "Open PRs", value: "0", icon: GitPullRequest, tone: "text-blue-700" },
  { label: "Failed Tasks", value: "0", icon: CircleAlert, tone: "text-red-700" },
  { label: "Blocked Tasks", value: "0", icon: Activity, tone: "text-amber-700" }
];

export default function DashboardPage() {
  return (
    <main className="space-y-6">
      <section className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <h1 className="text-2xl font-semibold tracking-normal">Dashboard</h1>
          <p className="mt-1 text-sm text-muted-foreground">Platform foundation status</p>
        </div>
        <StatusBadge label="API boundary ready" status="ready" />
      </section>

      <section className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
        {metrics.map((metric) => {
          const Icon = metric.icon;
          return (
            <Card key={metric.label}>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle>{metric.label}</CardTitle>
                <Icon className={`h-5 w-5 ${metric.tone}`} aria-hidden="true" />
              </CardHeader>
              <CardContent>
                <div className="text-3xl font-semibold">{metric.value}</div>
              </CardContent>
            </Card>
          );
        })}
      </section>

      <section className="grid gap-4 lg:grid-cols-[2fr_1fr]">
        <Card>
          <CardHeader>
            <CardTitle>System Health</CardTitle>
          </CardHeader>
          <CardContent className="grid gap-3 sm:grid-cols-3">
            <StatusBadge label="API" status="ready" />
            <StatusBadge label="PostgreSQL" status="pending" />
            <StatusBadge label="Redis" status="pending" />
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Provider</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-lg font-medium">Codex</div>
            <div className="text-sm text-muted-foreground">Configured through API settings</div>
          </CardContent>
        </Card>
      </section>
    </main>
  );
}

