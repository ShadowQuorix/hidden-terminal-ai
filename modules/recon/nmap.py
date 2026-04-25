import asyncio


class NmapScan:
    name = "Nmap Scan"

    def __init__(self, flags="-sC -sV"):
        self.flags = flags

    async def run(self, target):
        cmd = f"nmap {self.flags} {target}"

        process = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        if stderr:
            return stderr.decode()

        return stdout.decode()