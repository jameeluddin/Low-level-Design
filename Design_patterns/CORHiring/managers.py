from abc import ABC, abstractmethod


class Managers(ABC):
    def __init__(self):
        self.manager = None
        self.approval_limit = 0
        self.manager_name = ""

    def set_manager(self, manager):
        self.manager = manager

    def approve_salary(self, employee_salary):
        if self.approval_limit > employee_salary:
            self.process_salary(employee_salary)
        elif self.manager is not None:
            self.manager.approve_salary(employee_salary)
        else:
            print("Cannot make the offer to candidate")

    @abstractmethod
    def process_salary(self, employee_salary):
        pass
