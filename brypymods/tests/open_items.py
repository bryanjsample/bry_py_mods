from file_manipulation.items_to_open import ItemsToOpen
import sys

def main():
    items = ItemsToOpen(sys.argv[1:])
    items.open_items()

if __name__ == "__main__":
    main()