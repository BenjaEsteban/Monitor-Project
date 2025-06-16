import configparser
from .site import Site
from .checker import BasicSiteChecker

class MonitorManager:
    def __init__(self, config_file='config.ini'):
        self.sites = self.load_sites(config_file)
        self.checker = BasicSiteChecker(self.sites)

    def load_sites(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        sites = []
        for name in config['Sitios']:
            sites.append(Site(name, config['Sitios'][name]))
        return sites

    def check_all(self):
        return self.checker.check_sites()
