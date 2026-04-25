import asyncio 

class Engine:
    def __init__(self):
        self.target = target
        self.profile = profile
        self.modules = []

        def register(self, module):
            self.modules.append(module)

        async def run_module(self, module):
            print(f"[+] Running {module.name}")
            try:
                result = await module.run(self.target)
                return {"module":module.name, "data": result}
            except Exception as e:
                return {"module": module.name, "error": str(e)}

        async def run(self):
                tasks = [self.run_module(m) for m in self.modules]
                return await asyncio.gather(*tasks)