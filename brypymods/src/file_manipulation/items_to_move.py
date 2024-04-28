from file_manipulation.directory import Directory
from file_manipulation.get_keys import get_key_press
from typing import List
from time import sleep
import subprocess
import os

class ItemsToMove(Directory):
    def __init__(self, target_extension:str|list=False, echo_dir_contents_at_init:bool=True) -> None:
        Directory.__init__(self, welcome_message_command='move', target_extension=target_extension, echo_dir_contents_at_init=echo_dir_contents_at_init)
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
                os.system('clear')
                destination = self.Destination_Paths[indx]
                move_confirmed = get_key_press(message=f'Attempting to move {path.split('/')[-1]} ----> {destination}...\n\n    ENTER :  move file\n    ANY OTHER KEY : continue without moving file', pressed_any_other=False)
                if move_confirmed:
                    subprocess.check_call(['mv', path, destination])
                    print(f'\nMoved {path} ----> {destination}')
                    sleep(1)
        def all_at_once():
            for indx, path in enumerate(self.Target_Paths):
                destination = self.Destination_Paths[indx]
                subprocess.check_call(['mv', path, destination])
                print(' '.join(['mv', path, destination]))
        os.system('clear')
        get_key_press(message=f'Attempting to move :\n\n      {',\n      '.join(self.Target_Items)}\n {' '*(max([len(x) for x in self.Target_Items])+7)}----> {self.Destination_Directory}\n\n    ENTER: move all files at once\n    ANY OTHER KEY : move files one at a time...', pressed_enter=all_at_once, pressed_any_other=one_at_at_time)
        os.system('clear')
        print(f'All files successfully moved to {self.Destination_Directory}')


def main():
    files = ItemsToMove()
    files.move_items()

if __name__ == "__main__":
    main()