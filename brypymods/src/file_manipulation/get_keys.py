from _sitebuiltins import Quitter
from typing import Callable
import getch

def get_key_press(message:str='Press enter to continue or any other key to quit...', pressed_enter:bool|Callable=True, pressed_any_other:bool|Callable=quit) -> bool|Callable:
    '''
        Obtain key press to determine whether or not to continue in the script.
        Pressing enter will return pressed_enter:bool|func, and any other input will return pressed_any_other:bool|func.

        Parameters:
            - message : Optional string to be printed before the input request is initiated.
                        If not supplied, 'Press enter to continue or any other key to quit...' will print.
            - pressed_enter : Boolean value or function to be returned if the user presses the enter key.
                                If not supplied, return value defaults to True to allow user to run an if statement in their main function.
            - func : Optional function to be executed upon pressing enter, default is quit().
    '''

    def eval_key_press(key:str, *args, **kwargs) -> bool|Callable:
        '''Inner function to process function arguments.'''
        if key == 'q' or key == '\x1b':
            print('\nTerminating...\n')
            quit()
        elif key == '\n':
            if type(pressed_enter) is bool:
                return pressed_enter
            else:
                pressed_enter(*args, **kwargs)
        else:
            if type(pressed_any_other) is bool:
                return pressed_any_other
            else:
                if type(pressed_any_other) == Quitter:
                    print('\nTerminating...\n')
                pressed_any_other(*args, **kwargs)

    print(message)
    key = getch.getch()
    return eval_key_press(key)