class Correlator:

    @staticmethod
    def analyze(services):
        actions = []

        for s in services:
            if "80/tcp" in s or "http" in s:
                actions.append("web")
            
            if "445/tcp" in s:
                actions.append("smb")

        return list(set(actions))