from files import Files

total_files = 0

class Drive:
    def __init__(self, name):
        self.file_counter = 0
        self.name = name
        self.tree_depth = 0
        self.storage = []

    def add_file_to_drive(self, file):
        global total_files
        self.storage.append(file)
        self.file_counter += 1
        total_files += 1

    def remove_file_from_drive(self, file_name):
        found = False
        for x in self.storage:
            if file_name == x.__repr__():
                self.storage.remove(x)
                self.file_counter -= 1
                total_files -= 1
                found = True
        if found is False:
            print("File", file_name, "not found. Nothing has been deleted.")

    def remove_filnum_from_drive(self, file_num):
        global total_files
        found = False
        for x in self.storage:
            if isinstance(x, Files) and file_num == x.file_number:
                self.storage.remove(x)
                self.file_counter -= 1
                total_files -= 1
                found = True
        if found is False:
            print("File", file_num, "in drive", self.name, "not found. Nothing has been deleted.")

    def print_file(self, file_num):
        found = False
        for x in self.storage:
            if isinstance(x, Files) and file_num == x.file_number:
                x.display()
                found = True

        if found is True:
            pass

    def add_directory(self):
        self.tree_depth += 1
        self.storage.append(list())

    def add_file_to_dir(self, directory_index, file_num):
        self.storage[directory_index].append(Files(file_num))
        self.file_counter += 1
        total_files += 1

    def move_to_dir(self, directory_index, file_name):
        found = False
        for x in self.storage:
            if file_name == x.name:
                self.storage[directory_index].append(x)

    def move_filenum_to_dir(self, directory_index, file_num):
        found = False
        for x in self.storage:
            if isinstance(x, Files) and file_num == x.file_number:
                self.storage[directory_index].append(x)
                self.storage.remove(x)

    def display(self):
        print("|| Drive", self.name, "-- Files:", self.file_counter, "||")
        for x in self.storage:
            if isinstance(x, Files):
                print("/", end="")
                print(x)

            else:
                print("/dir/")
                # print("/dir/",x)
                for dir_file in x:
                    print("  ^  ", dir_file)
        print()


if __name__ == "__main__":
    pass