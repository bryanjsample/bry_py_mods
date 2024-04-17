from markdown_files import MarkdownFiles
from sorter import Sorter
from get_keys import get_key_press
from items_to_open import ItemsToOpen
from items_to_move import ItemsToMove
from screenshot_to_move import ScreenshotToMove
import sys

def convert_md_to_pdf():
    '''Looks for markdown files in the current directory, and allows you to choose one or more. Once items are selected, they will be converted to a pdf.'''
    markdown_files = MarkdownFiles()
    markdown_files.convert_files()

def open_items():
    '''
        Will list all items in the current directory with the listed extensions. If no arguments are provided, then an option will
        be given to show only unhidden items or all items.Once items are selected, you can choose to open them all at once or one at a time.
    '''
    items = ItemsToOpen(sys.argv[1:])
    items.open_items()

def move_items():
    files = ItemsToMove()
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
        extensions = input('Enter a single-space seperated series of extensions to sort: ').split(' ')
    for extension in extensions:
        items_to_sort = Sorter(extension)
        destination = items_to_sort.destination_path()
        get_key_press(message=f'\nPress enter to move files into {destination} or any other key to quit...\n')
        items_to_sort.sort_items()