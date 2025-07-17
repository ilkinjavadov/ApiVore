import argparse
import asyncio
from core import parser, auth, idor, ratelimit, ai_assist, output
from utils.logger import setup_logger
from rich.console import Console

console = Console()
logger = setup_logger()

async def main():
    parser_args = argparse.ArgumentParser(
        description="Apivore - AI Powered API Abuse Scanner"
    )
    parser_args.add_argument(
        "--openapi", required=True, help="OpenAPI / Swagger spec YAML file path"
    )
    parser_args.add_argument(
        "--auth-type",
        choices=["bearer", "basic", "none"],
        default="none",
        help="Authentication type (default: none)",
    )
    parser_args.add_argument("--auth-token", help="Bearer token or basic auth user:pass")
    parser_args.add_argument(
        "--output", default="output/report.json", help="Report output file"
    )
    parser_args.add_argument(
        "--enable-ai", action="store_true", help="Enable AI-powered analysis"
    )
    args = parser_args.parse_args()

    console.print("[bold green]Apivore API Abuse Scanner starting...[/]")

    endpoints = parser.load_endpoints(args.openapi)
    if not endpoints:
        console.print("[red]No endpoints found in spec. Exiting.[/]")
        return

    # Auth client creation
    client = auth.create_client(args.auth_type, args.auth_token)

    console.print(f"[cyan]Loaded {len(endpoints)} endpoints from spec.[/]")
    console.print("[yellow]Running IDOR tests...[/]")
    idor_results = await idor.scan(endpoints, client)

    console.print("[yellow]Running Rate Limit tests...[/]")
    rate_results = await ratelimit.scan(endpoints, client)

    ai_results = {}
    if args.enable_ai:
        console.print("[yellow]Running AI assisted analysis...[/]")
        ai_results = await ai_assist.analyze(endpoints)

    report = output.generate_report(idor_results, rate_results, ai_results)
    output.save_report(report, args.output)

    console.print(f"[bold green]Scan complete. Report saved to {args.output}[/]")

if __name__ == "__main__":
    asyncio.run(main())
