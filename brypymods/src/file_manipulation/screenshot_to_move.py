from file_manipulation.items_to_move import ItemsToMove
from typing import List
import os

class ScreenshotToMove(ItemsToMove):
    def __init__(self) -> None:
        target_extension:List[str]=['jpg', 'jpeg', 'png']
        self._desktop_directory = self.locate_desktop()
        os.chdir(self.Desktop_Directory)
        ItemsToMove.__init__(self, target_extension)

    @property
    def Desktop_Directory(self):
        return self._desktop_directory

    def locate_desktop(self):
        path_elements = os.getcwd().split('/')
        Users, username = path_elements[1:3]
        return f'/{Users}/{username}/Desktop'


def main():
    screenies = ScreenshotToMove()
    screenies.move_items()

if __name__ == "__main__":
    main()