import asyncio

class WebEnum:
    name = "Web Enum"

    async def run(self, target):
        proc = await asyncio.create_subprocess_shell(
            f"whatweb {target}",
            stdout=asyncio.subprocess.PIPE
        )

        out, _ = await proc.communicate()
        return out.decode()