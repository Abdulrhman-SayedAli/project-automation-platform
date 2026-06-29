import { Settings } from "lucide-react";
import { PageHeader } from "@/components/page-header";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const settingsRows = [
  ["Coding Provider", "API controlled"],
  ["Worker Count", "3"],
  ["Retry Limit", "3"],
  ["GitHub Owner", "Environment"]
];

export default function SettingsPage() {
  return (
    <main className="space-y-6">
      <PageHeader title="Settings" description="Runtime configuration exposed by FastAPI" />
      <Card>
        <CardHeader className="flex flex-row items-center justify-between">
          <CardTitle>Configuration</CardTitle>
          <Settings className="h-5 w-5 text-muted-foreground" aria-hidden="true" />
        </CardHeader>
        <CardContent className="divide-y divide-border">
          {settingsRows.map(([label, value]) => (
            <div key={label} className="flex items-center justify-between py-3 text-sm">
              <span className="font-medium">{label}</span>
              <span className="text-muted-foreground">{value}</span>
            </div>
          ))}
        </CardContent>
      </Card>
    </main>
  );
}

