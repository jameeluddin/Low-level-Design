from Design_patterns.proxyDesignPattern.EmployeeDaoProxy import EmployeeDaoProxy
from Design_patterns.proxyDesignPattern.EmployeeDaoimpl import EmployeeDo


def main():
    try:
        emp_table_obj = EmployeeDaoProxy()
        # emp_table_obj.create("ADMIN", EmployeeDo())
        emp_table_obj.get("ADMIN", 1)
        print("Operation Successful")
    except Exception as e:
        print("Error is e ===>", e)


if __name__ == "__main__":
    main()