import asyncio
from core.engine import Engine
from modules.recon.nmap import NmapScan


def run_scan(target):

    async def scan():
        engine = Engine(target, profile={"nmap_flags": "-sC -sV"})
        engine.register(NmapScan("-sC -sV"))

        results = await engine.run()

        return str(results)

    return asyncio.run(scan())