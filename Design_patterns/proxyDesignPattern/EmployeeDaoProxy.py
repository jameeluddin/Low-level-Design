from Design_patterns.proxyDesignPattern.EmployeeDao import EmployeeDao
from Design_patterns.proxyDesignPattern.EmployeeDaoimpl import EmployeeDaoImpl


class EmployeeDaoProxy(EmployeeDao):

    def __init__(self):
        self.employee_dao_obj = EmployeeDaoImpl()

    def create(self, client, obj):
        if client == "ADMIN":
            self.employee_dao_obj.create(client, obj)
        else:
            raise Exception("Access Denied")

    def delete(self, client, empid):
        if client == "ADMIN":
            self.employee_dao_obj.delete(client, empid)
        else:
            raise Exception("Access Denied")

    def get(self, client, empid):
        if client in ("ADMIN", "USER"):
            return self.employee_dao_obj.get(client, empid)
        else:
            raise Exception("Access Denied")


