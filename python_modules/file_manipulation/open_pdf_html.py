from directory import Directory

class MarkupFiles(Directory):
    '''

    '''
    def __init__(self, target_extension:bool | str=False):
        Directory.__init__(self, target_extension)

def main():
    markup_files = MarkupFiles()
    

if __name__ == "__main__":
    main()