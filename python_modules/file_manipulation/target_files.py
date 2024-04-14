from directory import Directory
import os
from time import sleep

class TargetFiles(Directory):
    def __init__(self, target_extension:str|list=False) -> None:
        Directory.__init__(self, target_extension)
        self.files = list(filter(lambda x:x.split('.')[-1] == self.target_extension, self.files))
        self.destination = f'{self.path}/{self.target_extension}_files' 

    def move_files(self):
        if self.directory_does_not_exist():
            os.mkdir(self.destination)
        for file in self.files:
            os.rename(f'{self.path}/{file}', f'{self.destination}/{file}')
        print(f'Moved all {self.target_extension} files.\n')
        sleep(1)

    def directory_does_not_exist(self):
        cwd_contents = os.listdir(self.path)
        if f'{self.target_extension}_files' not in cwd_contents:
            return True
        else:
            return False