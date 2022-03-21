from drive import *
from files import *
import random

total_files = 0

class FS:
    def __init__(self):
        global total_files
        self.driveA = Drive("A")
        self.driveB = Drive("B")
        self.driveC = Drive("C")
        self.populate_drives()

    def populate_drives(self):
        global total_files
        for x in range(1, 3):
            self.driveA.add_file_to_drive(Files(x))
            total_files += 1 
        self.driveB.add_directory()
        for x in range(3, 6):
            self.driveB.add_file_to_drive(Files(x))
            total_files += 1
            self.driveB.move_filenum_to_dir(0, x)
        self.driveC.add_file_to_drive(Files(6))
        total_files += 1

    def display(self):
        self.driveA.display()
        self.driveB.display()
        self.driveC.display()


if __name__ == "__main__":
    pass
