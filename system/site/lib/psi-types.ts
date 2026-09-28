// Shapes of psi-data/derived/*.json (written by system/psi-ingest).

export type Measure = {
  raw: string;
  value?: number;
  min?: number;
  max?: number;
  unit?: string;
  values?: number[];
  flags?: string[];
};

export type Category = { value: string; raw?: string; basis?: string; source?: number };

export type Condition = Measure | Category;

export type Source = {
  kind: "psi" | "psi-workbook" | "psi-aux" | "report";
  dataset?: string;
  file?: string;
  row?: number | null;
  sheet?: string;
  note?: string;
  table?: string;
  line?: number;
  doc?: string;
  doc_title?: string;
  doc_status?: string;
  source_id?: string;
  title?: string;
  url?: string;
  via?: string;
};

export type SlimSource = Pick<Source, "kind" | "dataset" | "file" | "row" | "sheet" | "table" | "line" | "doc" | "source_id" | "title" | "via">;

export type Outcome = {
  quantity: string;
  source: number;
  measure?: Measure;
  text?: string;
  at?: Record<string, number>;
  note?: string;
  confirmed_by?: number[];
};

export type Conflict = {
  field: string;
  values: { source: number; raw: string; min?: number; max?: number; unit?: string }[];
};

type RunBase = {
  id: string;
  investigation: string;
  label: string;
  granularity: "test" | "test-point" | "day" | "summary" | "envelope";
  date: string | null;
  conditions: Record<string, Condition>;
  outcomes: Outcome[];
  conflicts?: Conflict[];
  notes?: string[];
};

export type Run = RunBase & { sources: Source[]; raw: Record<string, string>[] };
export type SlimRun = RunBase & { sources: SlimSource[] };
export type RawBundle = Record<string, Record<string, string>[]>;

export type Citation = {
  doc: string;
  doc_title?: string;
  doc_status?: string;
  source_id?: string;
  title?: string;
  url?: string;
};

export type Investigation = {
  id: string;
  name: string;
  full_name: string | null;
  psi_id: string | null;
  geometry_class: string;
  citation: Citation | null;
  runs: number;
  granularity: Record<string, number>;
  runs_with_report_data: number;
  runs_with_outcomes: number;
  conflicts: number;
  outcome_quantities: Record<string, number>;
  coverage: Record<string, unknown>;
  table_notes: string[];
  psi_files: string[];
};

export function isMeasure(c: Condition | undefined): c is Measure {
  return !!c && "raw" in c && !("value" in c && typeof (c as Category).value === "string");
}

export function isCategory(c: Condition | undefined): c is Category {
  return !!c && typeof (c as Category).value === "string";
}
