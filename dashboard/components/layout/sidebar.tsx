import Link from "next/link";
import {
  Boxes,
  Gauge,
  ListChecks,
  RadioTower,
  Server,
  Settings,
  Workflow
} from "lucide-react";

const navItems = [
  { href: "/", label: "Dashboard", icon: Gauge },
  { href: "/projects", label: "Projects", icon: Boxes },
  { href: "/tasks", label: "Tasks", icon: ListChecks },
  { href: "/workers", label: "Workers", icon: Server },
  { href: "/graphs", label: "Graphs", icon: Workflow },
  { href: "/events", label: "Events", icon: RadioTower },
  { href: "/settings", label: "Settings", icon: Settings }
];

export function Sidebar() {
  return (
    <aside className="hidden w-64 shrink-0 border-r border-border bg-muted/35 px-3 py-4 md:block">
      <div className="px-3 pb-5">
        <div className="text-sm font-semibold uppercase text-muted-foreground">AI Software</div>
        <div className="text-xl font-semibold">Factory</div>
      </div>
      <nav className="space-y-1">
        {navItems.map((item) => {
          const Icon = item.icon;
          return (
            <Link
              key={item.href}
              href={item.href}
              className="flex min-h-10 items-center gap-3 rounded-md px-3 text-sm font-medium text-muted-foreground hover:bg-background hover:text-foreground"
            >
              <Icon className="h-4 w-4" aria-hidden="true" />
              {item.label}
            </Link>
          );
        })}
      </nav>
    </aside>
  );
}

