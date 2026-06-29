type PageHeaderProps = {
  title: string;
  description: string;
};

export function PageHeader({ title, description }: PageHeaderProps) {
  return (
    <section>
      <h1 className="text-2xl font-semibold tracking-normal">{title}</h1>
      <p className="mt-1 text-sm text-muted-foreground">{description}</p>
    </section>
  );
}

