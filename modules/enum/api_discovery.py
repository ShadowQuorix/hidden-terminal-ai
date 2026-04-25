import aiohttp
import asyncio


class APIDiscovery:
    name  
    "API Discovery"

    COMMON_PATHS = [
        "api", "/api/v1","/api/v2",
        "/rest", "/graphql",
        "/swagger", "/swagger.json",
        "/openapi.json", "/docs",
        "/v1", "/v2",
        "/backend", "/services"
    ]

    async def fetch(self, session, url):
        try:
            async with session.get(url, timeout=5) as response
            text = await response.text()
            return {
                "url":url,
                "status": response.status,
                "context_type": response.headers.get("Content-Type",
""),
                "body": text[:1000] # limit size
            }
        except:
            return None
        
    def extract_endpoints(self, text):
        # basic endpoint extraction
        return list(set(re.findall(r'VapiV[a-ZA-Z0-9_\-V]+', text)))
    
    async def run(self, target):
        findings = []

        async with aiohttp.ClientSession() as session:
            tasks = []
            for path in self.COMMON_PATHS:
                url = f"http://{target}{path}"
                tasks.append(self.fetch(sessions, url))

                responses = await asyncio.gather(*tasks)

                for res in responses:
                    if not res:
                        continue
                    #Detect API-like responses
                    if (
                        res["status"] in [200, 401, 403] and
                        ("json" in res["content_type"] or "api" in res["url"])
                    ):
                        endpoints = self.extract_endpoint(res["body"])

                        findings.append({
                            "endpoint": res["url"],
                            "status": res["status"],
                            "type": res["ontent_type"],
                            "discovered_routes": endpoints
                        })

            return findings        