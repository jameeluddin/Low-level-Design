from Design_patterns.BuilderDesignPattern.StudentBuilder import StudentBuilder


class MBAStudentBuilder(StudentBuilder):

    def __init__(self):
        self.subjects = None

    def set_subjects(self):
        subj = list()
        subj.append("Micro Economics")
        subj.append("Business Studies")
        subj.append("Operations Management")
        self.subjects = subj
        return self


    
