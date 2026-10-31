"""Check the static export at --url, including mobile comparison and downloads.

Requires Python Playwright and its Chromium browser. Start npm run preview
after npm run build. Timings are local navigation-to-ready measurements.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time
from urllib.parse import urlencode
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://localhost:3100")
    args = parser.parse_args()
    first, second = "PSI-101:SAME #57", "PSI-101:SAME #56"
    params = urlencode([("investigation", "same-r"), ("run", first), ("compare", first), ("compare", second), ("compare_quantity", "spread_rate")])
    report = {"url": args.url, "scope": "Local static export in Chromium; navigation includes parsing/hydration and dataset loading. No deployed-host or live chatbot latency.", "viewports": []}
    expected_hash = hashlib.sha256((ROOT / "psi-data/derived/runs.json").read_bytes()).hexdigest()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for width in (1280, 390):
            context = browser.new_context(viewport={"width": width, "height": 900}, accept_downloads=True)
            page = context.new_page()
            page.set_default_timeout(60000)
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            start = time.perf_counter()
            response = page.goto(args.url + "/explore/?" + params)
            assert response.status == 200
            expect(page.get_by_role("heading", name="Compare selected tests")).to_be_visible()
            panel = page.locator("section[aria-labelledby='comparison-heading']")
            expect(panel.get_by_role("status")).to_contain_text("Insufficient metadata")
            ready_ms = round((time.perf_counter() - start) * 1000, 2)
            expect(panel.get_by_role("combobox").nth(0)).to_have_value("spread_rate")
            expect(panel).to_contain_text("not reported")
            panel.get_by_role("combobox").nth(0).select_option("dusttrak_a_mass_concentration")
            panel.get_by_role("combobox").nth(1).select_option("flow_cm_s")
            page.wait_for_function("new URL(location.href).searchParams.get('compare_quantity') === 'dusttrak_a_mass_concentration' && new URL(location.href).searchParams.get('compare_varied') === 'flow_cm_s'")
            page.reload()
            expect(panel.get_by_role("combobox").nth(0)).to_have_value("dusttrak_a_mass_concentration")
            expect(panel.get_by_role("combobox").nth(1)).to_have_value("flow_cm_s")
            with page.expect_download() as pending:
                panel.get_by_role("button", name="Export comparison JSON").click()
            data = json.loads(Path(pending.value.path()).read_text(encoding="utf-8"))
            assert data["dataset"]["sha256"] == expected_hash
            assert data["assessment"]["can_compare"] is False
            assert data["assessment"]["quantity"] == "dusttrak_a_mass_concentration"
            assert data["assessment"]["varied_axis"] == "flow_cm_s"
            assert len(data["records"]) == 2
            assert data["assessment"]["unknown_or_conflicted"]
            detail = page.get_by_role("article", name="Run " + first, exact=True)
            expect(detail).to_contain_text("source processed")
            detail.get_by_text("Source cells, exactly as written", exact=True).click()
            expect(detail.get_by_text("Formula", exact=False).first).to_be_visible()
            with page.expect_download() as pending:
                page.get_by_role("button", name="Download evidence JSON").click()
            evidence = json.loads(Path(pending.value.path()).read_text(encoding="utf-8"))
            assert evidence["dataset"]["sha256"] == expected_hash
            assert evidence["records"] and evidence["limitations"]
            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 1"), "viewport overflow"
            panel.get_by_role("button", name="Remove " + second, exact=True).click()
            expect(panel).to_contain_text("Open another test")
            panel.get_by_role("button", name=first, exact=True).click()
            # Reports within one investigation may cite different publications.
            # Some sources carry a canonical URL; others (a poster distributed in
            # the PSI archive) are cited by a textual descriptor only. Both forms
            # must render, each keeping its own title.
            runs = json.loads((ROOT / "psi-data/derived/runs.json").read_text(encoding="utf-8"))["runs"]
            url_run = next(r for r in runs if any(s.get("scope") == "campaign apparatus" and s.get("url") for s in r["sources"]))
            page.goto(args.url + "/explore/?" + urlencode({"investigation": url_run["investigation"], "run": url_run["id"]}))
            url_detail = page.get_by_role("article", name="Run " + url_run["id"], exact=True)
            apparatus_source = next(s for s in url_run["sources"] if s.get("scope") == "campaign apparatus" and s.get("url"))
            expect(url_detail.get_by_role("link", name=apparatus_source["title"], exact=True).first).to_have_attribute("href", apparatus_source["url"])
            # No URL -> no link pretending one exists; the textual descriptor must show.
            desc_run = next(r for r in runs if any(s.get("scope") == "campaign apparatus" and not s.get("url") for s in r["sources"]))
            page.goto(args.url + "/explore/?" + urlencode({"investigation": desc_run["investigation"], "run": desc_run["id"]}))
            desc_detail = page.get_by_role("article", name="Run " + desc_run["id"], exact=True)
            desc_source = next(s for s in desc_run["sources"] if s.get("scope") == "campaign apparatus" and not s.get("url"))
            expect(desc_detail.get_by_text(desc_source["title"], exact=False).first).to_be_visible()
            expect(desc_detail.get_by_text(desc_source["descriptor"][0:60], exact=False)).to_be_visible()
            expect(desc_detail.get_by_role("link", name=desc_source["title"], exact=True)).to_have_count(0)
            # Newly exposed Table 2 measurements retain their location, units,
            # source index and original values in the user-facing export.
            page.goto(args.url + "/explore/?" + urlencode({"investigation": "saffire-iv-vi", "run": "saffire-iv-vi:VI-3"}))
            saffire = page.get_by_role("article", name="Run saffire-iv-vi:VI-3", exact=True)
            expect(saffire).to_contain_text("Max temperature at far-field device / nearest location")
            expect(saffire).to_contain_text("CO₂ partial-pressure increase")
            with page.expect_download() as pending:
                page.get_by_role("button", name="Download evidence JSON").click()
            exported = json.loads(Path(pending.value.path()).read_text(encoding="utf-8"))
            assert exported["dataset"]["sha256"] == expected_hash
            selected = next(item["run"] for item in exported["records"] if item["run"]["id"] == "saffire-iv-vi:VI-3")
            for quantity, value, unit in (("max_temp_ffd_nearest", 21, "°C"),
                                           ("co2_partial_pressure_increase", 3.51, "mmHg"),
                                           ("smoke_threshold_crossing_time", 981, "s")):
                outcome = next(o for o in selected["outcomes"] if o["quantity"] == quantity)
                assert outcome["measure"]["value"] == value and outcome["measure"]["unit"] == unit
                assert selected["sources"][outcome["source"]]["source_id"] == "saffire-vi-ices-2024"
            threshold = next(o for o in selected["outcomes"] if o["quantity"] == "smoke_threshold_crossing_time")
            assert threshold["at"] == {"selected_mass_concentration_mg_m3": 1}
            expect(saffire).to_contain_text("1 mg/m³ selected smoke threshold")
            assert all(s.get("doc_status") != "draft" for item in exported["records"] for s in item["run"]["sources"])
            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 1"), "SAFFIRE viewport overflow"
            page.goto(args.url + "/explore/?" + urlencode({"investigation": "saffire-iv-vi", "run": "saffire-iv-vi:VI-2"}))
            quarantined = page.get_by_role("article", name="Run saffire-iv-vi:VI-2", exact=True)
            expect(quarantined).to_contain_text("excluded from analysis pending source clarification")
            with page.expect_download() as pending:
                page.get_by_role("button", name="Download evidence JSON").click()
            quarantine_export = json.loads(Path(pending.value.path()).read_text(encoding="utf-8"))
            row = next(item["run"] for item in quarantine_export["records"] if item["run"]["id"] == "saffire-iv-vi:VI-2")
            withheld = [o for o in row["outcomes"] if "source_definition_unresolved" in o.get("measure", {}).get("flags", [])]
            assert len(withheld) == 5
            assert next(o for o in withheld if o["quantity"] == "total_heat_release_imaging")["measure"]["value"] == 580
            page.goto(args.url + "/")
            expect(page.get_by_role("heading", name="The current evidence record")).to_be_visible()
            expect(page.get_by_role("heading", name="Published literature beyond PSI test rows")).to_be_visible()
            for slug in ("literature/luci-rotating-rocket", "literature/daft-cabin-aerosol",
                         "investigations/droplet-combustion/flex-2-cool-flame-results"):
                assert page.locator(f'a[href$="/docs/{slug}"]').count() + page.locator(f'a[href$="/docs/{slug}/"]').count() > 0
                response = context.request.get(args.url + "/md/" + slug + ".md")
                assert response.status == 200, slug
                assert "status: stable" in response.text(), slug
            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 1"), "home viewport overflow"
            assert not errors, errors
            report["viewports"].append({"width": width, "navigation_to_comparison_ready_ms": ready_ms,
                                         "comparison_export": True, "evidence_export": True, "source_cells": True,
                                         "saffire_measurements_export": True, "saffire_quarantine": True, "published_literature": True,
                                         "no_viewport_overflow": True, "page_errors": errors})
            context.close()
        browser.close()
    target = ROOT / "research/browser-validation.json"
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
