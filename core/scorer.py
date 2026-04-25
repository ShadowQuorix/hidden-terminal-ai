class Scorer:

    @staticmethod
    def score(service):
        score = 0

        if "http" in service:
            score += 3
        if "smb" in service.lower():
                score +=5
        if "ssh" in service.lower():
            score += 2

        if score >= 7:
                return "HIGH"
        elif score >= 4:
            return "MEDIUM"
        return "LOW"
            