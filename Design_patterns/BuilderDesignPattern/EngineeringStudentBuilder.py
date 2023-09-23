from Design_patterns.BuilderDesignPattern.StudentBuilder import StudentBuilder


class EngineeringStudentBuilder(StudentBuilder):

    def __init__(self):
        self.subjects = None

    def set_subjects(self):
        subj = list()
        subj.append("DSA")
        subj.append("OS")
        subj.append("Computer Architecture")
        self.subjects = subj
        return self

