from file_manipulation.directory import Directory
from file_manipulation.get_keys import get_key_press
from typing import List
from time import sleep
import subprocess
import os

class ItemsToMove(Directory):
    def __init__(self, target_extension:str|list=False) -> None:
        Directory.__init__(self, welcome_message_command='move', target_extension=target_extension)
        self._target_items:List[str] = self.choose_multiple_items()
        self._target_paths:List[str] = [f'{self.Directory_Path}/{item_name}' for item_name in self.Target_Items]
        self._destination_directory:str = self.input_new_file_path()
        self._destination_paths:List[str] = [f'{self.Destination_Directory}/{item_name}' for item_name in self.Target_Items]

    @property
    def Target_Items(self) -> List[str]:
        return self._target_items

    @property
    def Target_Paths(self) -> List[str]:
        return self._target_paths

    @property
    def Destination_Directory(self) -> str:
        return self._destination_directory

    @property
    def Destination_Paths(self) -> List[str]:
        return self._destination_paths
    

    def move_items(self):
        def one_at_at_time():
            for indx, path in enumerate(self.Target_Paths):
                destination = self.Destination_Paths[indx]
                open_confired = get_key_press(message=f'\nAttempting to move {path} ----> {destination}...\n\nPress enter to move or any other key to continue.', pressed_any_other=False)
                if open_confired:
                    subprocess.run(['mv', path, destination])
                    sleep(1)
                os.system('clear')
        def all_at_once():
            for indx, path in enumerate(self.Target_Paths):
                destination = self.Destination_Paths[indx]
                subprocess.run(['mv', path, destination])
                print(' '.join(['mv', path, destination]))
        os.system('clear')
        get_key_press(message=f'\nPress enter to move {', '.join(self.Target_Items)} ----> {self.Destination_Directory} all at once or any other key to open one at a time...', pressed_enter=all_at_once, pressed_any_other=one_at_at_time)
        os.system('clear')
        print(f'All files successfully moved to {self.Destination_Directory}')


def main():
    files = ItemsToMove()
    files.move_items()

if __name__ == "__main__":
    main()