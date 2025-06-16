import requests
from typing import List
from .interfaces import ISiteChecker
from .site import Site

class BasicSiteChecker(ISiteChecker):
    def __init__(self, sites: List[Site]):
        self.sites = sites

    def check_sites(self) -> List[tuple[str, str, bool]]:
        result = []
        for site in self.sites:
            try:
                res = requests.get(site.url, timeout=5)
                site.status = res.status_code == 200
            except Exception:
                site.status = False
            result.append((site.name, site.url, site.status))
        return result
