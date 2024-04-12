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
        self.target_file = self.choose_file()

    def convert_md_to_pdf(self):
        '''Convert target markdown file to a pdf of the same name.'''
        os.system('clear')
        new_name = self.change_target_extension()
        conversion_string = f'Attempting to convert {self.target_file}  ---->  {new_name}...'
        print('\n\n', conversion_string)
        self.get_key_press(f'\nPress enter to convert or any other key to terminate...')
        os.system('clear')
        print('\n\n', f'{conversion_string:^50}'.replace('Attempting to convert', 'Converting'))
        subprocess.check_call(['pandoc', self.target_file, '-o', new_name, '--from', 'markdown', '--template', 'eisvogel', '--listings'])
        os.system('clear')
        self.get_key_press(f'\n\nFinished converting {new_name}. Press enter to open or any other key to terminate...\n')
        self.open_pdf_file(new_name)

    def open_pdf_file(self, new_name):
        self.add_pdf_to_path(new_name)
        subprocess.run(['open', self.path])
        os.system('clear')

    def change_target_extension(self):
        '''Change file extension from '.md' to '.pdf'.'''
        return self.target_file.replace('.md', '.pdf')
    
    def add_pdf_to_path(self, new_name):
        '''Add new pdf file to self.path.'''
        self.path += '/' + new_name

def main():
    markdown_file = MarkdownFile('md')
    markdown_file.convert_md_to_pdf()


if __name__ == "__main__":
    main()