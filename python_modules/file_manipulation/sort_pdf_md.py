'''Class definition for working with multiple files as opposed to one.'''

from directory import Directory, get_key_press
import os
from time import sleep

class TargetFiles(Directory):
    def __init__(self, target_extension:str|list=False) -> None:
        Directory.__init__(self, target_extension)

    def sort_files(self):
        destination = self.destination_path()
        if self.directory_does_not_exist():
            os.mkdir(destination)
        for file in self.Files:
            os.rename(f'{self.Directory_Path}/{file}', f'{destination}/{file}')
        print(f'Moved all {self.Target_Extension} files.\n')
        sleep(1)

    def directory_does_not_exist(self):
        cwd_contents = os.listdir(self.Directory_Path)
        if f'{self.Target_Extension}_files' not in cwd_contents:
            return True
        else:
            return False
    
    def destination_path(self):
        return f'{self.Directory_Path}/{self.Target_Extension}_files'

def main():
    pdfs = TargetFiles('pdf')
    destination = pdfs.destination_path()
    get_key_press(message=f'\nPress enter to move files into {destination} or any other key to quit...\n')
    pdfs.sort_files()

    mds = TargetFiles('md')
    destination = mds.destination_path()
    get_key_press(message=f'\nPress enter to move files into {destination} or any other key to quit...\n')
    mds.sort_files()

if __name__ == "__main__":
    main()