'''
    Module to convert a Markdown file to a PDF file.
'''

from directory import Directory
import subprocess
import os

class MarkdownFile(Directory):
    '''
        Converts a Markdown File to PDF using pandoc after inheriting attributes
        from directory.py's Directory class.
    '''
    def __init__(self, target_extension:bool | str=False):
        '''Inherit attributes and obtain target file.'''
        Directory.__init__(self, target_extension)
        self.__target_file = self.choose_one_item()
        self.__target_path = f'{self.Directory_Path}/{self.Target_File}'
        self.__destination_file = None
        self.__destination_path = None


    @property
    def Target_File(self) -> str:
        return self.__target_file
    @Target_File.setter
    def Target_File(self, target_file:str) -> None:
        self.__target_file = target_file

    @property
    def Target_Path(self) -> str:
        return self.__target_path
    @Target_Path.setter
    def Target_Path(self, file_path:str) -> None:
        self.__target_path = file_path

    @property
    def Destination_Path(self) -> str:
        return self.__destination_path
    @Destination_Path.setter
    def Destination_Path(self, dest_path:str) -> None:
        self.__destination_path = dest_path

    @property
    def Destination_File(self) -> str:
        return self.__destination_file
    @Destination_File.setter
    def Destination_File(self, new_name) -> None:
        self.__destination_file = new_name


    def __str__(self):
        '''
            Markdown File : file.md
            Parent Directory : /path/to/markdown/file
        '''
        return f'Markdown File : {self.Target_File}\nParent Directory : {self.Directory_Path}'

    def confirm_conversion(self):
        self.Destination_File = self.change_target_extension()
        self.Destination_Path = f'{self.Directory_Path}/{self.Destination_File}'
        conversion_string = f'Attempting to convert {self.Target_File}  ---->  {self.Destination_File}...'
        print('\n\n', conversion_string)
        self.get_key_press(f'\nPress enter to convert or any other key to terminate...')
        return conversion_string

    def open_pdf_file(self):
        subprocess.run(['open', self.Destination_Path])
        os.system('clear')

    def change_target_extension(self):
        '''Change file extension from '.md' to '.pdf'.'''
        return self.Target_File.replace('.md', '.pdf')
    
    def convert_md_to_pdf(self):
        '''Convert target markdown file to a pdf of the same name.'''
        os.system('clear')
        conversion_string = self.confirm_conversion()
        os.system('clear')
        print('\n\n', f'{conversion_string:^50}'.replace('Attempting to convert', 'Converting'))
        subprocess.check_call(['pandoc', self.Target_Path, '-o', self.Destination_Path, '--from', 'markdown', '--template', 'eisvogel', '--listings'])
        os.system('clear')
        self.get_key_press(f'\n\nFinished converting {self.Destination_File}. Press enter to open or any other key to terminate...\n')
        self.open_pdf_file()

def main():
    markdown_file = MarkdownFile('md')
    markdown_file.convert_md_to_pdf()


if __name__ == "__main__":
    main()