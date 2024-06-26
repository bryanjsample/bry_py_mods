from file_manipulation.markdown_files import MarkdownFiles
from file_manipulation.sorter import Sorter
from file_manipulation.get_keys import get_key_press
from file_manipulation.items_to_open import ItemsToOpen
from file_manipulation.items_to_move import ItemsToMove
from file_manipulation.screenshot_to_move import ScreenshotToMove
import sys
import os

def convert_md_to_pdf():
    '''Looks for markdown files in the current directory, and allows you to choose one or more. Once items are selected, they will be converted to a pdf.'''
    markdown_files = MarkdownFiles()
    markdown_files.convert_files()
    sort_files = get_key_press(message="\nAttempting to sort md and pdf files into directories...\n\n    ENTER : sort files\n    ANY OTHER KEY : quit...")
    if sort_files:
        extensions = ['md', 'pdf']
        for extension in extensions:
            items_to_sort = Sorter(extension, echo_dir_contents_at_init=False)
            items_to_sort.sort_items()

def open_items():
    '''
        Will list all items in the current directory with the listed extensions. If no arguments are provided, then an option will
        be given to show only unhidden items or all items.Once items are selected, you can choose to open them all at once or one at a time.
    '''
    items = ItemsToOpen(sys.argv[1:])
    items.open_items()

def move_items():
    files = ItemsToMove(sys.argv[1:])
    files.move_items()

def move_screenshots():
    screenies = ScreenshotToMove()
    screenies.move_items()

def sort_items():
    '''
        Will list all items in the current directory with the listed extensions. If no arguments are provided, then an option will be given to show
        only unhidden items or all items.Once items are selected, they will be sorted into sub-directories based on their extension.
    '''
    extensions = sys.argv[1:]
    if len(extensions) == 0:
        extensions = input('No extensions have been provided to sort!\n\n    Enter a single-space seperated series of extensions: ').split(' ')
    os.system('clear')
    for extension in extensions:
        items_to_sort = Sorter(extension)
        destination = items_to_sort.destination_path()
        get_key_press(message=f'Attempting to move files into {destination}\n\n    ENTER : move files\n    ANY OTHER KEY : quit...\n')
        items_to_sort.sort_items()