'''
    Module to sort files in a directory into their own sub-directories based on their extension

    External Dependencies:
        - Python
            - Getch : pip install getch
'''

from file_manipulation.directory import Directory
import os
from time import sleep

class Sorter(Directory):
    '''
        Class to sort files into their own sub-directories based on their extension.
        All attributes are inherited from directory.Directory
    '''
    def __init__(self, target_extension:str|list=False) -> None:
        Directory.__init__(welcome_message_command='move', target_extension=target_extension)

    def sort_items(self) -> None:
        '''Move files into their respective sub-directories'''
        destination = self.destination_path()
        if self.directory_does_not_exist():
            os.mkdir(destination)
        for file in self.Files:
            os.rename(f'{self.Directory_Path}/{file}', f'{destination}/{file}')
        print(f'Moved all {self.Target_Extension} files.\n')
        sleep(1)

    def directory_does_not_exist(self) -> bool:
        '''If directories exist, great! If not, make them.'''
        cwd_contents = os.listdir(self.Directory_Path)
        if f'{self.Target_Extension}_files' not in cwd_contents:
            return True
        else:
            return False
    
    def destination_path(self) -> str:
        return f'{self.Directory_Path}/{self.Target_Extension}_files'
