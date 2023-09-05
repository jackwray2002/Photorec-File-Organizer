from os.path import isdir
from os import listdir
from shutil import move

class collection_directory_get():
    def __init__(self):
        self.collection_directory = input("Enter a directory for file collection: ")
        if isdir(self.collection_directory) == True:
            pass
        elif isdir(self.collection_directory) == False:
            print("Invalid Directory.")
            collection_directory_get()
    def __str__(self):
        return str(self.collection_directory)

class final_directory_get():
    def __init__(self):
        self.final_directory = input("Enter a directory to place organized files: ")
        if isdir(self.final_directory) == True:
            pass
        elif isdir(self.final_directory) == False:
            print("Invalid Directory.")
            final_directory_get()
    def __str__(self):
        return str(self.final_directory)

if __name__ == "__main__":
    collection_directory = str(collection_directory_get())
    final_directory = str(final_directory_get())
    file_type = input("Enter the file format for data collection: ")

    for directory in listdir(collection_directory):
        for file in listdir(collection_directory + "\\" + directory):
            if file.endswith(file_type):
                old_file_path = (collection_directory + "\\"
                + directory + "\\" + file)            
                new_file_path = (final_directory + "\\" + file)
                move(old_file_path, new_file_path)
