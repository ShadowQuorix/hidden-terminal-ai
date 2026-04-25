from core.correlator import Correlator

class Orchestrator:

    def __init__(self, engine, profile):
        self.engine = engine
        self.profile = profile
        
    def load_modules(self, services):
        actions = Correlator.analyze(services)

        for action in actions:
            if action == "web":
                from modules.enum.web import WebEnum
                self.engine.register(WebEnum())

            if action == "smb":
                from modules.enum.smb import SMBEnum
                self.engine.register(SMBEnum())