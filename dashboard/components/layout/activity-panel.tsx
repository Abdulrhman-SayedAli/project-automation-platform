import { Clock3 } from "lucide-react";

export function ActivityPanel() {
  return (
    <aside className="hidden w-72 border-l border-border bg-background px-4 py-5 xl:block">
      <div className="flex items-center gap-2 text-sm font-semibold">
        <Clock3 className="h-4 w-4 text-muted-foreground" aria-hidden="true" />
        Activity
      </div>
      <div className="mt-6 rounded-md border border-dashed border-border p-4 text-sm text-muted-foreground">
        Awaiting platform events
      </div>
    </aside>
  );
}

