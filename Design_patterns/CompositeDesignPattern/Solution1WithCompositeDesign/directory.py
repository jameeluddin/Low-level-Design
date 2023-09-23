from Design_patterns.CompositeDesignPattern.Solution1WithCompositeDesign.FileSystem import FileSystem


class Directory(FileSystem):
    def __init__(self, name):
        self.directory_name = name
        self.file_system_list = list()

    def add(self, file_obj):
        self.file_system_list.append(file_obj)

    def ls(self):
        print("Directory Name", self.directory_name)
        for file_obj in self.file_system_list:
            file_obj.ls()
            

