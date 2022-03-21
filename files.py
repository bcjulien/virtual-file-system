import random


class Files:
    def __init__(self, file_number, extension=None):
        x = random.getrandbits(20)
        self.unique_data = x
        self.extension = extension
        if self.extension == None:
            self.extension = random.choice([".exe", ".py", ".cpp", ".h"])
        self.file_number = file_number

    def __repr__(self):
        return "F" + str(self.file_number) + self.extension

    def display(self):
        print(self.__repr__(), "<", self.unique_data, ">")


if __name__ == "__main__":
    pass
