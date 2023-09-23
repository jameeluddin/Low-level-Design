from Design_patterns.BuilderDesignPattern.Director import Director
from Design_patterns.BuilderDesignPattern.EngineeringStudentBuilder import EngineeringStudentBuilder
from Design_patterns.BuilderDesignPattern.MBAStudentBuilder import MBAStudentBuilder


def main():
    dir_obj1 = Director(EngineeringStudentBuilder())
    dir_obj2 = Director(MBAStudentBuilder())
    engg_student = dir_obj1.create_student()
    mba_student = dir_obj2.create_student()
    print(engg_student)
    print(mba_student)


if __name__ == "__main__":
    main()
