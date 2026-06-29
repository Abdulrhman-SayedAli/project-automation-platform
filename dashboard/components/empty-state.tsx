import { Inbox } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";

type EmptyStateProps = {
  title: string;
  detail: string;
};

export function EmptyState({ title, detail }: EmptyStateProps) {
  return (
    <Card>
      <CardContent className="flex min-h-48 flex-col items-center justify-center gap-3 text-center">
        <Inbox className="h-8 w-8 text-muted-foreground" aria-hidden="true" />
        <div>
          <h2 className="text-base font-semibold">{title}</h2>
          <p className="mt-1 text-sm text-muted-foreground">{detail}</p>
        </div>
      </CardContent>
    </Card>
  );
}

