import asyncio

class SMBEnum:
    name = "SMB Enum"

    async def run(self, target):
        proc = await asyncio.create_subprocess_shell(
            f"enum4linux {target}",
            stdout=asyncio.subprocess.PIPE
        )

        out, _ = await proc.communicate()
        return out.decode()