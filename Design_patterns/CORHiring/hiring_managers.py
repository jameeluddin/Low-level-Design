from Design_patterns.CORHiring.managers import Managers


class HiringManager(Managers):
    def __init__(self, approval_limit, manager_name):
        super().__init__()
        self.approval_limit = approval_limit
        self.manager_name = manager_name

    def process_salary(self, employee_salary):
        print(f"{self.manager_name} has approved the salary at level 1, for salary amount {employee_salary}")
