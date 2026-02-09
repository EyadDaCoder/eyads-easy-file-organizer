from time import sleep as delay

class organizer:
    def __init__(self):
        print("Eyads Easy File Organizer")
        self.keywords = []
        self.file_extensions = {
            "image": [],
            "video": [],
            "audio": [],
            "languages": [],
            "markup": [],
            "special text": [],
            "config text": [],
            "binaries": []
        }
        delay(2)
        self.directory = input("1: Enter the directory of the folder you want to organize -: ")
        self.type = input("2: Enter 'A' if you want to sort by filetype or 'B' if you want to\nsort by keywords -:")
        if input == "B":
            keywords_raw = input("3: Enter a list of keywords seperated by backticks -:")
            cache = []
            for i in keywords_raw:
                cache.append(i)
                if '`' in cache:
                    cache.remove('`')
                    self.keywords.append(cache)
        print("Setup complete!")
