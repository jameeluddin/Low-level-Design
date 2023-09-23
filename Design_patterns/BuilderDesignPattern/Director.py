from Design_patterns.BuilderDesignPattern import StudentBuilder
from Design_patterns.BuilderDesignPattern.EngineeringStudentBuilder import EngineeringStudentBuilder
from Design_patterns.BuilderDesignPattern.MBAStudentBuilder import MBAStudentBuilder


class Director:

    def __init__(self, student_builder):
        self.student_builder = student_builder

    def create_student(self):
        if isinstance(self.student_builder, EngineeringStudentBuilder):
            return self.create_engg_student()

        elif isinstance(self.student_builder, MBAStudentBuilder):
            return self.create_MBA_student()

    def create_engg_student(self):
        # .set_father_name("vj").set_mother_name("pj")
        return self.student_builder.set_roll_number(1).set_age(22).set_name("sj").set_subjects().build()

    def create_MBA_student(self):
        return self.student_builder.set_roll_number(1).set_age(22).set_name("sj").set_father_name("Aj").set_mother_name(
            "mj").set_subjects().build()
