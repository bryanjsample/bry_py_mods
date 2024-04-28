'''
    Module to assist with selecting items from a directory.
    Author : Bryan Sample
    Date : 4/14/2024

    External Dependencies:
        - Python
            - Getch : pip install getch
'''

import os
from typing import List, Dict
from file_manipulation.get_keys import get_key_press


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
            from directory import Directory\n
                directory = Directory('md')\n
                target_file:str = directory.choose_one_item()\n
                target_files:list = directory.choose_multiple_items()\n
    '''
    def __init__(self, welcome_message_command:str, target_extension:str|list=False, echo_dir_contents_at_init:bool=True) -> None:
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
        self._welcome_message_command:str = welcome_message_command
        self._target_extension:str|List[str] = self.check_target_extensions(target_extension)
        self._changed_directory:bool = False 
        self._files:List[str] = self.parse_directory()
        if len(self.Files) > 1:
            self._file_dict:Dict[int, str] = self.form_file_dict()
        if not echo_dir_contents_at_init:
            os.system('clear')

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
    def WelcomeCommand(self) -> str:
        return self._welcome_message_command

    @property
    def Target_Extension(self) -> str|bool:
        return self._target_extension

    @property
    def Files(self) -> List[str]:
        return self._files

    @property
    def File_Dict(self) -> Dict[int, str]:
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
        valid_extensions = ['pdf', 'md', 'jpg', 'jpeg', 'svg', 'gif', 'html', 'xls', 'docx', 'png', 'doc', 'avi', 'fnt', 'txt', 'xml', 'csv', 'tiff', 'tif', 'exe', 'py', 'c', 'css']
        if target_extension:
            if type(target_extension) is list:
                extensions = [x.lower().replace('.', '') for x in target_extension]
                for i in extensions:
                    if i not in valid_extensions:
                        print(f'\n{i} is not a valid extenstion. Please adjust your instantiation arguments and try again.\nTerminating...\n')
                        quit()
                print(f'Searching for {', '.join(extensions)} files to {self.WelcomeCommand} inside of {self.Directory_Path.split('/')[-1]}...')
                return extensions
            else:
                extension = target_extension.lower().replace('.', '')
                if extension in ['Q', 'q', 'Quit', 'quit']:
                    print('\nTerminating...\n')
                    quit()
                if extension not in valid_extensions:
                    print(f'{extension} is not a valid extenstion. Please adjust your arguments and try again.\n\nTerminating...\n')
                    quit()
                else:
                    print(f'Searching for {extension} files to {self.WelcomeCommand} inside of {self.Directory_Path.split('/')[-1]}...')
                    return extension
        else:
            print(f'Searching for all files to {self.WelcomeCommand} inside of {self.Directory_Path.split('/')[-1]}...')
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
            extension_name = '* all extensions *'
        file_list = self.list_files()
        if len(file_list) == 0:
            get_key_press(message='No matching files found in the current working directory.\n\n    ENTER : input a custom file-path\n    ANY OTHER KEY : quit...')
            new_path = self.input_new_file_path()
            if new_path:
                self.Changed_Directory = True
                file_list = self.reset_directory_attributes(new_path)
        elif len(file_list) == 1:
            get_key_press(message=f'There is only one file in the directory \n\n    {file_list[0]}\n\n    ENTER : continue with file\n    ANY OTHER KEY : quit...')
        else:
            print(f'There is more than one file in the current working directory:\n')
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
            if get_key_press(message='\n    ENTER : list non-hidden items only\n    ANY OTHER KEY : list all items', pressed_any_other=False):
                file_list = [x for x in file_list if x[0] != '.']
        os.system('clear')
        return sorted(file_list)

    def form_file_dict(self, count:int=1) -> Dict[int,str]:
        '''
            Form a dictionary containing all target files as values and an associated integer as the key and returns it.
            No need to call outside of __init__().
        '''
        file_dict:Dict[int,str] = {}
        for f in self.Files:
            if file_dict.get(count, 'DNE') == 'DNE':
                file_dict[count] = f
                count += 1
        return file_dict
    
    def display_file_dict(self, file_dict:Dict[int,str]|bool=False) -> None:
        if not file_dict:
            file_dict = self.File_Dict
        for count, f in file_dict.items():
            print(f'{count: >{4+len(str(len(self.Files)))}} : {f}') 

    def input_new_file_path(self) -> str:
        '''
            Optionally input a new file path. First, check that it exists. If it does, return it. Otherwise
            you can decided whether to retry or terminate the script.
            No need to call outside of __init__().
        '''
        def lint_path(fpath:str) -> str:
            path_elements = fpath.split('/')
            valid_elements = [element for element in path_elements if element != '']
            return f'/{'/'.join(valid_elements)}'
        while True:
            fpath = lint_path(input('\nEnter new path to directory or q to quit: '))
            if fpath in ['q', 'Q', 'quit', 'Quit', 'exit']:
                print('\nTerminating...\n')
            else:
                try:
                    os.listdir(fpath)
                except FileNotFoundError:
                    get_key_press(message='\nDirectory path not found.\n\n    ENTER : retry entering new path\n    ANY OTHER KEY : quit...')
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
                os.system('clear')
                self.display_file_dict()
                try:
                    selection = int(input(f'\nEnter number to {self.WelcomeCommand} corresponding file: ').strip())
                    if selection in ['Q', 'q', 'Quit', 'quit']:
                        print('\nTerminating...\n')
                        quit()
                    elif selection not in acceptable_numbers:
                        get_key_press(message='\nNot an acceptable value.\n\n    ENTER : retry\n    ANY OTHER KEY : quit...')
                    else:
                        return self.File_Dict[selection]
                except ValueError:
                    get_key_press(message='\nNot an acceptable value.\n\n    ENTER : retry\n    ANY OTHER KEY : quit...')
        else:
            return [self.Files[0]]

    def choose_multiple_items(self) -> List[str] | str:
        '''If there is only one file, return it. Otherwise, print formatted dictionary and allow the user to select multiple files using a space seperated sequence.'''
        if len(self.Files) > 1:
            acceptable_numbers = self.File_Dict.keys()
            while True:
                os.system('clear')
                self.display_file_dict()
                try:
                    selections = [x for x in input(f'\nEnter space seperated numbers to {self.WelcomeCommand} corresponding file: ').split(' ')]
                    invalid_values = []
                    valid_files = []
                    for selection in selections:
                        if selection in ['Q', 'q', 'Quit', 'quit']:
                            print('\nTerminating...\n')
                            quit()
                        elif selection == '':
                            continue
                        elif int(selection) not in acceptable_numbers:
                            invalid_values.append(selection)
                        else:
                            valid_files.append(self.File_Dict[int(selection)])
                    if len(invalid_values) > 0:
                        get_key_press(message=f'{', '.join(invalid_values)} are not acceptable values.\n\n    ENTER : retry \n    ANY OTHER KEY : quit...')
                    elif len(valid_files) == 0:
                        return False
                    else:
                        return valid_files
                except ValueError:
                    get_key_press(message='\nNot an acceptable list of values.\n\n    ENTER : retry\n    ANY OTHER KEY : quit...')
                selections.clear()
        else:
            return [self.Files[0]]
