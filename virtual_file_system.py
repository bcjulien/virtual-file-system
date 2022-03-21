import random
from file_system import *

total_files = 6

class VFS:
    def __init__(self):
        global total_files
        self.vnode = FS()

    def add_file(self):
        global total_files
        target = random.choice([self.vnode.driveA, self.vnode.driveB, self.vnode.driveC])
        target.add_file_to_drive(Files(total_files+1))
        total_files += 1

    def delete_file(self, file_num):
        global total_files
        self.vnode.driveA.remove_filnum_from_drive(file_num)
        self.vnode.driveB.remove_filnum_from_drive(file_num)
        self.vnode.driveC.remove_filnum_from_drive(file_num)

    def print_file(self, file_num):
        self.vnode.driveA.print_file(file_num)
        self.vnode.driveB.print_file(file_num)
        self.vnode.driveC.print_file(file_num)
        print()

    def display(self):
        print("~~ VIRTUAL FILE SYSTEM ~~")
        self.vdisplay()
        print("_"*80)
        print("~~ FILE SYSTEM ~~")
        self.fsdisplay()

    def vdisplay(self):
        for x in self.vnode.driveA.storage:
            if isinstance(x, Files):
                print("/", x.__repr__())
            else:
                print("/dir/")
                for xx in x:
                    print("  ^  ", xx.__repr__())

        for y in self.vnode.driveB.storage:
            if isinstance(y, Files):
                print("/", y.__repr__())
            else:
                print("/dir/")
                for yy in y:
                    print("  ^  ", yy.__repr__())

        for z in self.vnode.driveC.storage:
            if isinstance(z, Files):
                print("/", z.__repr__())
            else:
                print("/dir/")
                for zz in z:
                    print("  ^  ", zz.__repr__())

    def fsdisplay(self):
        self.vnode.display()


def menu():
    print("[1] ADD NEW FILE - [2] DELETE FILE - [3] PRINT FILE - [0] EXIT")


def main():
    global total_files
    vfs = VFS()
    while True:
        vfs.display()
        menu()
        choice = int(input("    Enter: "))
        print()
        if choice == 1:
            vfs.add_file()
        elif choice == 2:
            target = int(input("Delete which File Number:"))
            vfs.delete_file(target)
        elif choice == 3:
            target = int(input("Display which File Number:"))
            vfs.print_file(target)
        elif choice == 0:
            break
        elif choice not in {'1','2','3','0'}:
            choice = int(input("Invalid choice. Enter: "))

if __name__ == "__main__":
    main()
