import Script from "next/script";

// /chat uses the shared workspace header around a full-screen ChatKit
// interface, without the docs chrome. Moved off the root `/`
// (which is now the landing page — 2026-09-25 decision) so the first thing a
// visitor sees is what the product is, not an empty composer. The chatkit.js
// web component is loaded only here, not in the root layout, since nothing
// outside this route uses it.
export default function Layout({ children }: LayoutProps<"/chat">) {
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
