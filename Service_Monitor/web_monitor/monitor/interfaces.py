from abc import ABC, abstractmethod
from typing import List

class ISiteChecker(ABC):
    @abstractmethod
    def check_sites(self) -> List[tuple[str, str, bool]]:
        pass
