from abc import ABC, abstractmethod
from typing import List, Optional
from entities.Administrator import Administrator

class IAdminRepository(ABC):
    
    @abstractmethod
    def add_administrator(self, admin: Administrator) -> None:
        pass
    
    @abstractmethod
    def get_administrators(self) -> List[Administrator]:
        pass

    @abstractmethod
    def get_administrator_by_id(self, admin_id: int) -> Optional[Administrator]:
        pass

    @abstractmethod
    def update_administrator(self, admin: Administrator) -> None:
        pass

    @abstractmethod
    def delete_administrator(self, admin_id: int) -> None:
        pass