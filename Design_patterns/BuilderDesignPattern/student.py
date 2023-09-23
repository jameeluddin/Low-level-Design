class Student:
    def __init__(self, builder):
        self.roll_number = builder.roll_number
        self.age = builder.age if hasattr(builder, "age") else None
        self.name = builder.name if hasattr(builder, "name") else None
        self.father_name = builder.father_name if hasattr(builder, "father_name") else None
        self.mother_name = builder.mother_name if hasattr(builder, "mother_name") else None
        self.subjects = builder.subjects if hasattr(builder, "subjects") else None

    def __str__(self):
        subjects_str = ', '.join(self.subjects)
        return f"roll number: {self.roll_number}, age: {self.age}, name: {self.name}, " \
               f"father name: {self.father_name}, mother name: {self.mother_name}, subjects: {subjects_str}"

