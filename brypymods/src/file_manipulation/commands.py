from file_manipulation.markdown_files import MarkdownFiles
from file_manipulation.sorter import Sorter
from file_manipulation.get_keys import get_key_press
from file_manipulation.items_to_open import ItemsToOpen
import sys

def convert_md_to_pdf():
    markdown_files = MarkdownFiles()
    markdown_files.convert_files()

def open_items():
    items = ItemsToOpen(sys.argv[1:])
    items.open_items()

def sort_items():
    extensions = sys.argv[1:]
    if len(extensions) == 0:
        extensions = input('Enter a single-space seperated series of extensions to sort: ').split(' ')
    for extension in extensions:
        items_to_sort = Sorter(extension)
        destination = items_to_sort.destination_path()
        get_key_press(message=f'\nPress enter to move files into {destination} or any other key to quit...\n')
        items_to_sort.sort_items()