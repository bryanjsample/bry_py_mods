'''
    Module to assist with selecting items from a directory.
    Import Directory class from this module and instantiate with an
    optional parameter {target_extension}. If provided, then only
    items with that extension will be listed. Otherwise, you can choose
    to show all items, including hidden items, or only non-hidden items.


'''

import os
import getch
from types import FunctionType

class Directory():
    '''
        Directory Class to be inherited / manipulated

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
            Attributes:
                self.Path: absolute path to the current working directory
                self.Target_Extension: optional extension to search for in directory
                self.Changed_Directory: defaults to false, only changed to true if a new path is used
                self.Files: list containing files targeted
                self.File_Dict: dictionary to select one file from many, only needed if there is > 1 file
        '''
        os.system('clear')
        self.__directory_path = os.getcwd()
        if target_extension:
            print(f'\nSearching for {target_extension} files inside of {self.Directory_Path}...')
        else:
            print(f'\nSearching for all files inside of {self.Directory_Path}...')
        self.__target_extension = target_extension
        self.__changed_directory = False 
        self.__files = self.parse_directory()
        if len(self.Files) > 1:
            self.__file_dict = self.form_file_dict()

    @property
    def Directory_Path(self):
        return self.__directory_path
    @Directory_Path.setter
    def Directory_Path(self, new_path:str):
        self.__directory_path = new_path

    @property
    def Target_Extension(self):
        return self.__target_extension
    @Target_Extension.setter
    def Target_Extension(self, new_extension:str):
        self.__target_extension = new_extension
    
    @property
    def Changed_Directory(self):
        return self.__changed_directory
    @Changed_Directory.setter
    def Changed_Directory(self, value:bool):
        self.__changed_directory = value

    @property
    def Files(self):
        return self.__files
    @Files.setter
    def Files(self, new_files:list|str):
        self.__files = new_files

    @property
    def File_Dict(self):
        return self.__file_dict
    @File_Dict.setter
    def File_Dict(self, new_dict:dict):
        self.__file_dict = new_dict

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

    def parse_directory(self) -> list:
        '''
            Determines the number of files within the current directory. 
            If there are no target files, then you can choose to search
            from a new path. At that point, self.Changed_Directory will
            flip to True, self.Path, self.Files, and self.File_Dict will
            be reassigned accordingly.
        '''
        extension_name = self.Target_Extension
        if not extension_name: # if extension is not provided
            extension_name = '*'
        file_list = self.list_files()
        if len(file_list) == 0:
            self.get_key_press('\nNo matching files found in the current working directory. Press enter to input a custom file-path or any other key to quit...')
            new_path = input('\nEnter new directory path: ')
            if new_path:
                self.Changed_Directory = True
                file_list = self.reset_directory_attributes(new_path)
        elif len(file_list) == 1:
            self.get_key_press(f'\nThere is only one {extension_name} file in the directory \n\n    {file_list[0]}\n\nPress enter to continue or any other key to quit...')
        else:
            print(f'\nThere is more than one {extension_name} file in the current working directory:\n')
        return file_list

    def list_files(self) -> list:
        '''Forms a list of target files and returns the list.'''
        if self.Target_Extension: # if parameter is provided
            if type(self.Target_Extension) is list: # if a list of extensions is provided
                file_list = []
                for extension in self.Target_Extension:
                    file_list.extend([x for x in os.listdir(self.Directory_Path) if extension == x.split('.')[-1]])
            else: # if only one extension is provided
                file_list = [x for x in os.listdir(self.Directory_Path) if self.Target_Extension == x.split('.')[-1]] # list of files in cwd if extension == target extenstion
        else: # if no parameter is provided 
            file_list = os.listdir(self.Directory_Path)
            print('\nPress enter to list only visible files or any other key to list all files...')
            key = getch.getch()
            if key == '\n':
                file_list = [x for x in file_list if x[0] != '.']
        return file_list

    def reset_directory_attributes(self, new_path:str) -> list:
        '''If a new path is provided, then reset self.Path and extract new target files'''
        self.Directory_Path = new_path
        new_files = self.parse_directory()
        return new_files

    def get_key_press(self, message:str='Press enter to continue...', func:FunctionType=quit) -> bool:
        '''
            Obtain key press to determine whether or not to continue in the script.
            Pressing enter will continue, and any other input will terminate the script.

            Parameters:
                - message : Optional string to be printed before the input request is initiated.
                            If not supplied, 'Press enter to continue...' will print.
                    ex : 'Press enter to continue or any other button to quit...'
                - func : Optional function to be executed upon pressing enter, default is quit().
        '''
        def inner_function(*args, **kwargs):
            '''Inner function to process function arguments.'''
            print(message)
            key = getch.getch()
            if key == '\n':
                return True
            else:
                print('\nTerminating...\n')
                func(*args, **kwargs)
        return inner_function

    def input_new_file_path(self) -> str:
        '''
            Optionally input a new file path. First, check that it exists. If it does, return it. Otherwise
            you can decided whether to retry or terminate the script.
        '''
        while True:
            fpath = input('\nEnter new path to directory: ')
            try:
                os.listdir(fpath)
            except NotADirectoryError:
                self.get_key_press('\nDirectory path not found. Press enter to retry or any other key to quit...')
            else:
                return fpath

    def form_file_dict(self, count:int=1) -> dict:
        '''Form a dictionary containing all target files as values and an associated integer as the key and returns it.'''
        file_dict = {}
        for f in self.Files:
            if file_dict.get(count, 'DNE') == 'DNE':
                file_dict[count] = f
                print(f'{count: >{4+len(str(len(self.Files)))}} : {f}') 
                count += 1
        return file_dict

    def choose_one_item(self) -> str:
        '''If there is only one file, return it. Otherwise, print formatted dictionary and allow the user to select the file.'''
        if len(self.Files) > 1:
            acceptable_numbers = self.File_Dict.keys()
            while True:
                try:
                    selection = int(input('\nEnter number to choose corresponding file: '))
                    if selection not in acceptable_numbers:
                        self.get_key_press('\nNot an acceptable value. Press enter to retry or any other key to quit...')
                    else:
                        return self.File_Dict[selection]
                except ValueError:
                    self.get_key_press('\nNot an acceptable value. Press enter to retry or any other key to quit...')
        else:
            return self.Files[0]
        
    def choose_multiple_items(self) -> list | str:
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
                        self.get_key_press(f'{', '.join(invalid_values)} are not acceptable values. Press enter to retry or any other key to quit...')
                    else:
                        return valid_files
                except ValueError:
                    self.get_key_press('\nNot an acceptable list of values. Press enter to retry or any other key to quit...')
                selections.clear()
        else:
            return self.files[0]