# my_modules

## Library of Modules and Scripts for My Own Personal Use

### COMMAND LINE SCRIPTS

- `$ ofs "extension", "extension", ...`
  - Will list all items in the current directory with the listed extensions. If no arguments are provided, then an option will be given to show only unhidden items or all items.
  - Once items are selected, you can choose to open them all at once or one at a time.
- `$ sfs "extension", "extension", ...`
  - Will list all items in the current directory with the listed extensions. If no arguments are provided, then an option will be given to show only unhidden items or all items.
  - Once items are selected, they will be sorted into sub-directories based on their extension.
- `$ mfs "extension", "extension", ...`
  - Will list all items in the current directory with the listed extensions. If no arguments are provided, then an option will be given to show only unhidden items or all items.
  - Once items are selected, user will be prompted to input an existing directory path to move items into.
  - You can choose whether to move the items all at once or individually
- `$ mscr`
  - Inherits attributes from ItemsToMove class (used in mfs command)
  - Looks for png, jpg, or jpeg files in the DESKTOP directory
  - Operates identically to mfs
- `$ convmd`
  - Looks for markdown files in the current directory, and allows you to choose all of them or only select files.
  - Once items are selected, they will be converted to a pdf.
  - You will have the option to sort the files into directories after conversion is completed

#### EXTERNAL DEPENDENCIES

- [**Getch**](https://pypi.org/project/getch/)
  - `$ pip install getch`
  - Python package to wait for a single key press input

#### MODULES

- **[File Manipulation](/python_modules/file_manipulation)**
  - [commands.py](brypymods/src/file_manipulation/commands.py)
    - Contains functions to be run as command scripts
  - [directory.py](brypymods/src/file_manipulation/directory.py)
    - Contains parent class Directory, which obtains contents from the current working directory and forms them into a dictionary which can then be used to select one or more files.
  - [get_keys.py](brypymods/src/file_manipulation/get_keys.py)
    - Contains function to wait for a single key press from user.
  - [markdown_files.py](brypymods/src/file_manipulation/markdown_files.py)
    - Child of Directory. Select multiple markdown files and manipulate them each individually. Allows user to convert md to pdf.
    - Dependencies
      - [**TeX Live**](https://www.tug.org/texlive/)
        - `brew install texlive`
        - System binaries to interact with the TeX document production system.
      - [**Cairo**](https://cairographics.org/)
        - `brew install cairo`
        - 2D graphics library written in C
      - [**Pandoc**](https://pandoc.org/)
        - `brew install pandoc`
        - File conversion software
      - [**Eisvogel Latex Template for Pandoc**](https://github.com/Wandmalfarbe/pandoc-latex-template?tab=readme-ov-file)
        - [Wandmalfarbe](https://github.com/Wandmalfarbe)'s Pandoc template to convert markdown files to pdf
        - Installation
        1. Extract the latest version of the template from the [release page](https://github.com/Wandmalfarbe/pandoc-latex-template/releases/tag/2.4.2)
        2. **Move `eisvogel.latex` to your pandoc templates directory**
           - Unix / Linux / MacOS : `/Users/USERNAME/.local/share/pandoc/templates/`
           - Windows Vista or later : `C:\Users\USERNAME\AppData\Roaming\pandoc\templates`
  - [sorter.py](brypymods/src/file_manipulation/sorter.py)
    - Child of Directory. Allows the user to sort items into sub-directories based on their extension.
  - [items_to_open.py](/python_modules/file_manipulation/items_to_open.py)
    - Child of Directory. Allows the user to open items based on their extension.
  - [items_to_move.py](/python_modules/file_manipulation/items_to_move.py)
    - Child of Directory. Allows the user to move items based on their extension.
  - [screenshot_to_move.py](/python_modules/file_manipulation/screenshot_to_move.py)
    - Child of ItemsToMove. Allows the user to move screenshots from the desktop to a specified directory.
- [**Timing**](/python_modules/timing/)
  - [timers.py](/python_modules/timing/timers.py)
    - Contains decorator function time_it() to measure execution / failure times
