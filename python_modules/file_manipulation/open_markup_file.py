from directory import Directory
import os
import subprocess

class MarkupFile(Directory):
    '''

    '''
    def __init__(self, target_extension:bool | str=False):
        Directory.__init__(self, target_extension)
        self.target_file = self.choose_file()
        self.path += '/' + self.target_file

    def open_file(self):
        subprocess.run(['open', self.path])
        os.system('clear')

def main():
    markup_file = MarkupFile(['txt', 'html', 'pdf', 'docx'])
    markup_file.open_file()


if __name__ == "__main__":
    main()