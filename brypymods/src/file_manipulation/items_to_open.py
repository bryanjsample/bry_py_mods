from file_manipulation.directory import Directory
from file_manipulation.get_keys import get_key_press
import os
import subprocess
from typing import List

class ItemsToOpen(Directory):
    '''
    
    '''
    def __init__(self, target_extension:bool | str=False):
        Directory.__init__(self, welcome_message_command='open', target_extension=target_extension)
        self._target_items:List[str] = self.choose_multiple_items()
        self._item_paths:List[str] = [f'{self.Directory_Path}/{item_name}' for item_name in self.Target_Items]

    @property
    def Target_Items(self) -> List[str]:
        return self._target_items

    @property
    def Item_Paths(self) -> List[str]:
        return self._item_paths

    def open_items(self):
        def one_at_at_time():
            for path in self.Item_Paths:
                open_confired = get_key_press(message=f'\nAttempting to open {path}\n\n    ENTER : open file\n    ANY OTHER KEY : continue without opening', pressed_any_other=False)
                if open_confired:
                    subprocess.run(['open', '-g', path])
        def all_at_once():
            self.Item_Paths.insert(0, 'open')
            subprocess.run(self.Item_Paths)
        os.system('clear')
        get_key_press(message=f'Attemping to open:\n\n  {',\n  '.join(self.Target_Items)}\n\n    ENTER : open all files at once\n    ANY OTHER KEY : open files one at a time', pressed_enter=all_at_once, pressed_any_other=one_at_at_time)
        os.system('clear')
        print('All files successfully opened.')

