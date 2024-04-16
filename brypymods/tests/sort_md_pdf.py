from file_manipulation.sorter import Sorter
from file_manipulation.get_keys import get_key_press
import sys

def main():
    extensions = sys.argv[1:]
    if len(extensions) == 0:
        extensions = input('Enter a single-space seperated series of extensions to sort: ').split(' ')
    for extension in extensions:
        items_to_sort = Sorter(extension)
        destination = items_to_sort.destination_path()
        get_key_press(message=f'\nPress enter to move files into {destination} or any other key to quit...\n')
        items_to_sort.sort_items()



if __name__ == "__main__":
    main()