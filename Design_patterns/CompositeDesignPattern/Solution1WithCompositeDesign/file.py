from Design_patterns.CompositeDesignPattern.Solution1WithCompositeDesign.FileSystem import FileSystem


class File(FileSystem):
    def __init__(self, name):
        self.file_name = name

    def ls(self):
        print("File name is ", self.file_name)

