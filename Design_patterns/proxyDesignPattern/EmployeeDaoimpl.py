from Design_patterns.proxyDesignPattern.EmployeeDao import EmployeeDao


class EmployeeDo:
    pass


class EmployeeDaoImpl(EmployeeDao):

    def create(self, client, obj):
        print("Created new row in the table")

    def delete(self, client, empid):
        print("Deleted row with employee id ", empid)

    def get(self, client, empid):
        print("fetching data from DB")
        return EmployeeDo()
