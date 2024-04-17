'''
    Module to assist with selecting items from a directory.
    Author : Bryan Sample
    Date : 4/14/2024

    External Dependencies:
        - Python
            - Getch : pip install getch
'''

import os
from typing import  List
from .get_keys import get_key_press


class Directory():
    '''
        Directory Class to be inherited / manipulated

        Import Directory class from this module and instantiate with an
        optional parameter {target_extension:str}. If provided, then only
        items with that extension will be listed. Otherwise, you can choose
        to show all items, including hidden items, or only non-hidden items.

        Properties
            - self.Target_Extension: optional extension to search for in directory
            - self.Directory_Path : string of the absolute path to the directory
            - self.Changed_Directory: defaults to false, only changed to true if a new path is used
            - self.Files: list containing files targeted
            - self.File_Dict: dictionary to select one file from many, only needed if there is > 1 file

        Example Instantiation:
            `from directory import Directory
                directory = Directory('md')
                target_file:str = directory.choose_one_item()
                target_files:list = directory.choose_multiple_items()
    '''
    def __init__(self, target_extension:str|list=False) -> None:
        '''
            1. Clear stdout
            2. Obtain cwd path and set self.Directory_Path
            3. Check that target extensions are valid if provided, or default to displaying all files
            4. Obtain a list of targeted file name strings if there is more than one, or a single file name string if there is only one.
            5. Form a dictionary of files and print keys and values to stdout

            Attributes:
                self.Directory_Path: absolute path to the current working directory
                self.Target_Extension: optional extension to search for in directory
                self.Changed_Directory: defaults to false, only changed to true if a new path is used
                self.Files: list containing files targeted
                self.File_Dict: dictionary to select one file from many, only needed if there is > 1 file
        '''
        os.system('clear')
        self._directory_path:str = os.getcwd()
        self._target_extension:str|List[str] = self.check_target_extensions(target_extension)
        self._changed_directory:bool = False 
        self._files:List[str] = self.parse_directory()
        if len(self.Files) > 1:
            self._file_dict:dict = self.form_file_dict()

    @property
    def Directory_Path(self) -> str:
        return self._directory_path
    @Directory_Path.setter
    def Directory_Path(self, new_path:str) -> None:
        self._directory_path = new_path

    @property
    def Changed_Directory(self) -> bool:
        return self._changed_directory
    @Changed_Directory.setter
    def Changed_Directory(self, value:bool) -> None:
        self._changed_directory = value

    @property
    def Target_Extension(self) -> str|bool:
        return self._target_extension

    @property
    def Files(self) -> List[str]:
        return self._files

    @property
    def File_Dict(self) -> dict:
        return self._file_dict

    def __str__(self) -> str:
        '''
            Directory path: /example/path/to/directory

            Files:
                file1.txt
                file2.txt
                file3.txt
                ...
        '''
        return f'\n\nDirectory path: {self.Directory_Path}\n\nFiles:\n    {'\n    '.join([f for f in self.Files])}'

    def check_target_extensions(self, target_extension:str|List[str]) -> str|List[str]|bool:
        '''
            Correct any minor mistakes made within target_extension argument. If any arguments are invalid, then execution will be terminated.
            No need to call outside of __init__().
        '''
        valid_extensions = ['pdf', 'md', 'jpg', 'jpeg', 'svg', 'gif', 'html', 'xls', 'docx', 'png', 'doc', 'avi', 'fnt', 'txt', 'xml', 'csv', 'tiff', 'tif', 'exe']
        if target_extension:
            if type(target_extension) is list:
                extensions = [x.lower().replace('.', '') for x in target_extension]
                for i in extensions:
                    if i not in valid_extensions:
                        print(f'\n{i} is not a valid extenstion. Please adjust your instantiation arguments and try again.\nTerminating...\n')
                        quit()
                print(f'\nSearching for {', '.join(extensions)} files inside of {self.Directory_Path}...')
                return extensions
            else:
                extension = target_extension.lower().replace('.', '')
                if extension in ['Q', 'q', 'Quit', 'quit']:
                    print('\nTerminating...\n')
                    quit()
                if extension not in valid_extensions:
                    print(f'\n{extension} is not a valid extenstion. Please adjust your instantiation arguments and try again.\n\nTerminating...\n')
                    quit()
                else:
                    print(f'\nSearching for {extension} files inside of {self.Directory_Path}...')
                    return extension
        else:
            print(f'\nSearching for all files inside of {self.Directory_Path}...')
            return False

    def parse_directory(self) -> List[str]:
        '''
            Determines the number of files within the current directory. 
            If there are no target files, then you can choose to search
            from a new path. At that point, self.Changed_Directory will
            flip to True, self.Path, self.Files, and self.File_Dict will
            be reassigned accordingly.
            No need to call outside of __init__().
        '''
        extension_name = self.Target_Extension
        if not extension_name: # if extension is not provided
            extension_name = '*'
        file_list = self.list_files()
        if len(file_list) == 0:
            get_key_press(message='\nNo matching files found in the current working directory. Press enter to input a custom file-path or any other key to quit...')
            new_path = self.input_new_file_path()
            if new_path:
                self.Changed_Directory = True
                file_list = self.reset_directory_attributes(new_path)
        elif len(file_list) == 1:
            get_key_press(message=f'\nThere is only one {extension_name} file in the directory \n\n    {file_list[0]}\n\nPress enter to continue or any other key to quit...')
        else:
            print(f'\nThere is more than one {extension_name} file in the current working directory:\n')
        return file_list

    def list_files(self) -> List[str]:
        '''
            Forms a list of target files and returns the list.
            No need to call outside of __init__().
        '''
        if self.Target_Extension: # if parameter is provided
            if type(self.Target_Extension) is list: # if a list of extensions is provided
                file_list = []
                for extension in self.Target_Extension:
                    file_list.extend([x for x in os.listdir(self.Directory_Path) if extension == x.split('.')[-1]])
            else: # if only one extension is provided
                file_list = [x for x in os.listdir(self.Directory_Path) if self.Target_Extension == x.split('.')[-1]] # list of files in cwd if extension == target extenstion
        else: # if no parameter is provided 
            file_list = os.listdir(self.Directory_Path)
            if get_key_press(message='\nPress enter to list only visible files or any other key to list all files...', pressed_any_other=False):
                file_list = [x for x in file_list if x[0] != '.']
        return file_list

    def form_file_dict(self, count:int=1) -> dict:
        '''
            Form a dictionary containing all target files as values and an associated integer as the key and returns it.
            No need to call outside of __init__().
        '''
        file_dict = {}
        for f in self.Files:
            if file_dict.get(count, 'DNE') == 'DNE':
                file_dict[count] = f
                print(f'{count: >{4+len(str(len(self.Files)))}} : {f}') 
                count += 1
        return file_dict

    def input_new_file_path(self) -> str:
        '''
            Optionally input a new file path. First, check that it exists. If it does, return it. Otherwise
            you can decided whether to retry or terminate the script.
            No need to call outside of __init__().
        '''
        while True:
            fpath = input('\nEnter new path to directory or q to quit: ')
            if fpath in ['q', 'Q', 'quit', 'Quit', 'exit']:
                print('\nTerminating...\n')
            else:
                try:
                    os.listdir(fpath)
                except FileNotFoundError:
                    get_key_press(message='\nDirectory path not found. Press enter to retry or any other key to quit...')
                else:
                    return fpath

    def reset_directory_attributes(self, new_path:str) -> List[str]:
        '''
            If a new path is provided, then reset self.Path and extract new target files.
            No need to call outside of __init__().
        '''
        self.Directory_Path = new_path
        new_files = self.parse_directory()
        return new_files

    def choose_one_item(self) -> str:
        '''If there is only one file, return it. Otherwise, print formatted dictionary and allow the user to select the file.'''
        if len(self.Files) > 1:
            acceptable_numbers = self.File_Dict.keys()
            while True:
                try:
                    selection = int(input('\nEnter number to choose corresponding file: '))
                    if selection not in acceptable_numbers:
                        get_key_press(message='\nNot an acceptable value. Press enter to retry or any other key to quit...')
                    else:
                        return self.File_Dict[selection]
                except ValueError:
                    get_key_press(message='\nNot an acceptable value. Press enter to retry or any other key to quit...')
        else:
            return [self.Files[0]]

    def choose_multiple_items(self) -> List[str] | str:
        '''If there is only one file, return it. Otherwise, print formatted dictionary and allow the user to select multiple files using a space seperated sequence.'''
        if len(self.Files) > 1:
            acceptable_numbers = self.File_Dict.keys()
            while True:
                try:
                    selections = [x for x in input('\nEnter space seperated numbers to choose corresponding file: ').split(' ')]
                    invalid_values = []
                    valid_files = []
                    for selection in selections:
                        if int(selection) not in acceptable_numbers:
                            invalid_values.append(selection)
                        else:
                            valid_files.append(self.File_Dict[int(selection)])
                    if len(invalid_values) > 0:
                        get_key_press(message=f'{', '.join(invalid_values)} are not acceptable values. Press enter to retry or any other key to quit...')
                    else:
                        return valid_files
                except ValueError:
                    get_key_press(message='\nNot an acceptable list of values. Press enter to retry or any other key to quit...')
                selections.clear()
        else:
            return [self.Files[0]]



def main():
    direct = Directory()


if __name__ == "__main__":
    main()