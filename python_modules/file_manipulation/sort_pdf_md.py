'''Class definition for working with multiple files as opposed to one.'''

from directory import Directory
import os
from time import sleep

class TargetFiles(Directory):
    def __init__(self, target_extension:str|list=False) -> None:
        Directory.__init__(self, target_extension)

    def sort_files(self):
        destination = self.destination_path()
        if self.directory_does_not_exist():
            os.mkdir(destination)
        for file in self.files:
            os.rename(f'{self.path}/{file}', f'{destination}/{file}')
        print(f'Moved all {self.target_extension} files.\n')
        sleep(1)

    def directory_does_not_exist(self):
        cwd_contents = os.listdir(self.path)
        if f'{self.target_extension}_files' not in cwd_contents:
            return True
        else:
            return False
    
    def destination_path(self):
        return f'{self.path}/{self.target_extension}_files'

def main():
    pdfs = TargetFiles('pdf')
    destination = pdfs.destination_path()
    pdfs.get_key_press(f'\nPress enter to move files into {destination} or any other key to quit...\n')
    pdfs.sort_files()

    mds = TargetFiles('md')
    destination = mds.destination_path()
    mds.get_key_press(f'\nPress enter to move files into {destination} or any other key to quit...\n')
    mds.sort_files()

if __name__ == "__main__":
    main()