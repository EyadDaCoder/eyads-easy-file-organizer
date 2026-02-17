from time import sleep as delay

class organizer:
    def __init__(self):
        print("Eyads Easy File Organizer")
        self.keywords = []
        delay(2)
        self.directory = input("1: Enter the directory of the folder you want to organize -: ")
        self.type = input("2: Enter 'A' if you want to sort by filetype or 'B' if you want to sort by keywords -: ")
        if self.type == "B":
            keywords_raw = input("3: Enter a list of keywords seperated by semicolons -:")
            cache = []
            for i in keywords_raw:
                cache.append(i)
                if ';' in cache:
                    cache.remove(';')
                    self.keywords.append(''.join(cache))
                    cache = []
        print(f"Setup complete!")
