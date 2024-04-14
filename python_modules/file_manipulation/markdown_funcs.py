r'''
    Module to convert any number of Markdown files to PDF files using github.com/Wandmalfarbe's pandoc template. "(https://github.com/Wandmalfarbe/pandoc-latex-template?tab=readme-ov-file)"

    External Dependencies:
        - Python
            - Getch : pip install getch
        - CLI Tools
            - texlive (Latex processor) : brew install texlive
            - cairo (vector graphics processor) : brew install cairo
            - pandoc (file converter) : brew install pandoc
        - Pandoc Eisvogel Latex Template
            - extract most recent zip file from : "https://github.com/Wandmalfarbe/pandoc-latex-template/releases/tag/2.4.2"
                - Will need to be moved into your pandoc templates directory!
                    - Unix / Linux / MacOS : "/Users/USERNAME/.local/share/pandoc/templates/"
                    - Windows Vista or later : "C:\Users\USERNAME\AppData\Roaming\pandoc\\templates"
'''

from directory import Directory, get_key_press
from typing import List
import subprocess
import os
from time import sleep

class MarkdownFile():
    '''
        Object representing a single markdown file. No parent classes.
        
        Properties:
            - self.Parent_Directory : path to parent directory of file object
            - self.Target_Name : file name of the targeted md file
            - self.Target_Path : path to targeted md file
            - self.Destination_Name : file name of the destination pdf file
            - self.Destination_Path : path to desination pdf file
    '''
    def __init__(self, target_name:str, directory_path:str) -> None:
        self.__parent_directory = directory_path
        self.__target_name = target_name
        self.__target_path = f'{directory_path}/{target_name}'
        self.__destination_name = target_name.replace('.md','.pdf')
        self.__destination_path = f'{directory_path}/{self.Destination_Name}'


    @property
    def Parent_Directory(self) -> str:
        return self. __parent_directory
    @Parent_Directory.getter
    def Parent_Directory(self, parent_dir) -> None:
        self.__parent_directory = parent_dir

    @property
    def Target_Name(self) -> str:
        return self.__target_name
    @Target_Name.setter
    def Target_Name(self, target_name:str) -> None:
        self.__target_name = target_name

    @property
    def Target_Path(self) -> str:
        return self.__target_path
    @Target_Path.setter
    def Target_Path(self, target_path:str) -> None:
        self.__target_path = target_path

    @property
    def Destination_Name(self) -> str:
        return self.__destination_name
    @Destination_Name.setter
    def Destination_Name(self, destination_name:str) -> None:
        self.__destination_name = destination_name

    @property
    def Destination_Path(self) -> str:
        return self.__destination_path
    @Destination_Path.setter
    def Destination_Path(self, destination_path:str) -> None:
        self.__destination_path = destination_path

    def __str__(self):
        return f'File Name : {self.Target_Name}\nParent directory : {self.Parent_Directory}'

    def confirm_conversion(self) -> str:
        '''
            Confirm with enter key before converting.
        '''
        conversion_string = f'Attempting to convert {self.Target_Name}  ---->  {self.Destination_Name}...'
        print('\n\n', conversion_string)
        get_key_press(message=f'\nPress enter to convert or any other key to terminate...')
        return conversion_string

    def open_pdf_file(self) -> None:
        '''
            Open pdf file in preview.
        '''
        subprocess.run(['open', self.Destination_Path])
        os.system('clear')

    def convert_md_to_pdf(self, converted_files:dict) -> None:
        '''
            Convert target markdown file to a pdf of the same name.
        '''
        os.system('clear')
        conversion_string = self.confirm_conversion()
        os.system('clear')
        print('\n\n', f'{conversion_string:^50}'.replace('Attempting to convert', 'Converting'))
        self.conversion(converted_files)
        os.system('clear')
        open_confirmed = get_key_press(message=f'\n\nFinished converting {self.Destination_Name}. Press enter to open or any other key to continue...\n', pressed_enter=True, pressed_any_other=False)
        if open_confirmed:
            self.open_pdf_file()

    def conversion(self, converted_files:dict) -> None:
        try:
            subprocess.check_call(['pandoc', self.Target_Path, '-o', self.Destination_Path, '--from', 'markdown', '--template', 'eisvogel', '--listings'])
            converted_files[self.Target_Name] = self.Destination_Name
        except subprocess.CalledProcessError:
            get_key_press(message=f'\n{self.Target_Name} failed to convert. Press enter to continue converting or any other key to terminate...')

class MarkdownFiles(Directory):
    '''
        Converts one or more Markdown Files to PDF using pandoc after inheriting attributes
        from directory.py's Directory class.
    '''
    def __init__(self, target_extension:str|List[str]=False):
        '''
            Inherit attributes and obtain list of target markdown file objects.
        '''
        Directory.__init__(self, target_extension)
        self.__target_files:List[MarkdownFile] = [MarkdownFile(x, self.Directory_Path) for x in self.choose_multiple_items()]

    @property
    def Target_Files(self) -> List[MarkdownFile]:
        return self.__target_files
    @Target_Files.setter
    def Target_Files(self, target_files:List[MarkdownFile]) -> None:
        self.__target_files = target_files

    def __str__(self) -> str:
        '''
            Markdown Files : file1.md, file2.md, file3.md, ...
            Parent Directory : /path/to/markdown/files
        '''
        return f'Markdown Files : {', '.join(self.Target_Files)}\nParent Directory : {self.Directory_Path}'

    def finished_converting(self) -> None:
        '''
            Once finished converting, print all files that successfully converted
        '''
        if len(self.converted_files.keys()) == 0:
            print('\nNo md were converted.\n')
        else:
            tar_width = len(max(self.converted_files.keys()))
            print(f'\nFinished processing all md files in {self.Directory_Path}.\n')
            for target, destination in self.converted_files.items():
                print(f'    {target:>{tar_width}} ----> {destination}')

    def convert_files(self) -> None:
        self.converted_files:dict = {}
        for mdfile in self.Target_Files:
            mdfile.convert_md_to_pdf(self.converted_files)
        os.system('clear')
        self.finished_converting()

def main():
    markdown_files = MarkdownFiles('md')
    markdown_files.convert_files()

if __name__ == "__main__":
    main()