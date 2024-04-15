---
title: "file_maniplation/README.md"
author: Bryan Sample
date: "4/14/24"
keywords: [python, package, file_manipulation, readme]
---

## file_manipulation

>**Collection of modules to interact with directories and files in the command line.**

### EXTERNAL DEPENDENCIES

- [**Getch**](https://pypi.org/project/getch/)
  - `$ pip install getch`
  - Python package to wait for a single key press input
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

#### MODULES

- **[File Manipulation](/python_modules/file_manipulation)**
  - [directory.py](/python_modules/file_manipulation/directory.py)
    - Contains parent class Directory, which obtains contents from the current working directory and forms them into a dictionary which can then be used to select one or more files.
  - [markdown_funcs.py](/python_modules/file_manipulation/markdown_funcs.py)
    - Child of Directory. Allows the user to select one or more markdown files to convert to pdf.
  - [sort_files.py](/python_modules/file_manipulation/sort_files.py)
    - Child of Directory. Allows the user to sort files into sub-directories based on their extension
  - [open_markup_file.py](/python_modules/file_manipulation/open_markup_file.py)
    - Not implemented.
- [**Timing**](/python_modules/timing/)
  - [timers.py](/python_modules/timing/timers.py)
    - Contains decorator function time_it() to measure execution / failure times