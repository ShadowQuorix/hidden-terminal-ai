import asyncio

from core.engine import Engine
from core.parser import Parser
from core.scorer import Scorer
from core.reporter import Reporter
from core.orchestrator import Orchestrator

from ai.analyzer import AIAnalyzer
from modules.recon.nmap import NmapScan

from config.settings import get_args, load_profile

async def main():
    args = get_args()
    profile = load_profile(args.mode)

    engine = Engine(args.target, profile)

    # Phase 1:Recon
    engine.register(NmapScan(profile["nmap_flags"]))
    results = await engine.run()

    nmap_output = results[0]["data"]
    services = Parser.extract__services(nmap_output)

    findings = []

    print("\n[+] AI Analysis:\n")

    for s in services:
        analysis = AIAnalyzer.analyze(s, profile)
        risk = Scorer.score(s)
    print(f"[{risk}]) {s}")

    findings.append({
        "service":s,
        "analysis": analysis,
        "risk": risk
    })

    # Phase 2 :Enumeration
    engine.mofules = []
    orchestrator = Orchestrator(engine. profile)
    orchestrator.load_modules(services)

    await engine.run()

    # Report
    Reporter.generate(findings)

    print(f"\n[+] Mode: {args.mode}")
    print("[+] Report saved → out/reports/report.html")
if __name__ == "__main__":
    asyncio.run(main())