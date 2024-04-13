from directory import Directory
from target_files import TargetFiles

def main():
    pdfs = TargetFiles('pdf')
    pdfs.get_key_press(f'\nPress enter to move files into {pdfs.destination} or any other key to quit...\n')
    pdfs.move_files()

    mds = TargetFiles('md')
    mds.get_key_press(f'\nPress enter to move files into {mds.destination} or any other key to quit...\n')
    mds.move_files()

if __name__ == "__main__":
    main()