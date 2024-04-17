from file_manipulation.directory import Directory
from typing import List

class ItemsToMove(Directory):
    def __init__(self, target_extension: str | list = False) -> None:
        super().__init__(target_extension)
        self._target_items:List[str] = self.choose_multiple_items()
        self._target_paths:List[str] = [f'{self.Directory_Path}/{item_name}' for item_name in self.Target_Items]

    @property
    def Target_Items(self) -> List[str]:
        return self._target_items

    @property
    def Target_Paths(self) -> List[str]:
        return self._target_paths
