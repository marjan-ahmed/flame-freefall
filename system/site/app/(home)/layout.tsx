import Script from "next/script";

// The root `/` is a full-screen ChatKit interface, not the record's cover: no
// navbar, no search, no theme switch, no docs chrome — a deliberate product
// choice (2026-09-22), overriding the front-door design this route group
// carried before. The chatkit.js web component is loaded only here, not in
// the root layout, since nothing outside this route uses it.
export default function Layout({ children }: LayoutProps<"/">) {
  return (
    <>
      <Script
        src="https://cdn.platform.openai.com/deployments/chatkit/chatkit.js"
        strategy="afterInteractive"
      />
      {children}
    </>
  );
}
