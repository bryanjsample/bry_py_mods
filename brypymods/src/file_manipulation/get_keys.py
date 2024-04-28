from _sitebuiltins import Quitter
from typing import Callable, Any
import getch

def get_key_press(message:str='\n    ENTER : continue\n    ANY OTHER KEY : terminate...', pressed_enter:bool|Callable=True, pressed_any_other:bool|Callable=quit) -> bool|Any:
    '''
        Obtain key press to determine how to proceed in the script.
        Pressing enter will return pressed_enter:bool|func, and any other input will return pressed_any_other:bool|func.

        Parameters:
            - message : Optional string to be printed before the input request is initiated.
                        If not supplied, '\\n    ENTER : continue\\n    ANY OTHER KEY : terminate...' will print.
            - pressed_enter : Boolean value or lambda function to be executed upon pressing the enter key.
                                If not supplied, return value defaults to True to allow user to run an if statement in their main function.
            - pressed_any_other : Boolean value or lambda function to be executed upon pressing any key other than enter, default is quit().
                                If not supplied, return value defaults to quit to terminate the python terminal.
    '''

    def eval_key_press(key:str, *args, **kwargs) -> bool|Any:
        '''Inner function to process function arguments.'''
        if key == 'q' or key == '\x1b':
            print('\nTerminating...')
            quit()
        elif key == '\n':
            if type(pressed_enter) is bool:
                return pressed_enter
            else:
                return_val = pressed_enter(*args, **kwargs)
        else:
            if type(pressed_any_other) is bool:
                return pressed_any_other
            else:
                if type(pressed_any_other) == Quitter:
                    print('\nTerminating...')
                return_val = pressed_any_other(*args, **kwargs)
        return return_val

    print(message)
    key = getch.getch()
    return eval_key_press(key)

def hidden_input(message:str) -> str:
    hidden_string = ''
    print(message)
    while True:
        hidden_char = getch.getch()
        if hidden_char == '\n':
            return hidden_string
        elif hidden_char == '\x7f':
            hidden_string = hidden_string[:-1]
        else:
            hidden_string += hidden_char


def main():
    string = hidden_input('Tell me your darkest secret: ')
    print(string)

if __name__ == "__main__":
    main()