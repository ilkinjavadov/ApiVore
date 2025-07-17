import json
from pathlib import Path

def save_report(report: dict, output_path: str):
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
    print(f"[+] Report saved to {output_path}")

def generate_report(idor_results, rate_results, ai_results=None):
    report = {
        "idor": idor_results,
        "rate_limit": rate_results,
        "ai_analysis": ai_results if ai_results else "Not enabled"
    }
    return report

def generate_html_report(report: dict, output_path: str):
    # Basit HTML şablon - isteğe göre geliştirilebilir
    html_content = """
    <html>
    <head><title>Apivore API Abuse Report</title></head>
    <body>
    <h1>API Abuse Scan Report</h1>
    <h2>IDOR Findings</h2>
    <pre>{idor}</pre>
    <h2>Rate Limit Findings</h2>
    <pre>{rate}</pre>
    <h2>AI Analysis</h2>
    <pre>{ai}</pre>
    </body>
    </html>
    """.format(
        idor=json.dumps(report.get("idor", {}), indent=4),
        rate=json.dumps(report.get("rate_limit", {}), indent=4),
        ai=report.get("ai_analysis", "Not enabled")
    )

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[+] HTML report saved to {output_path}")
