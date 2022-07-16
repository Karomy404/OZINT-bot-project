import whois


class OzintDomain():
    def __init__(self, domain: str):
        self.domain = domain

    def whois(self):
        return whois.whois(self.domain)
