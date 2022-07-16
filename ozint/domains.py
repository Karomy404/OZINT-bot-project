import whois


class OzintDomain():
    def owhois(self, domain: str):
        return whois.whois(domain)
