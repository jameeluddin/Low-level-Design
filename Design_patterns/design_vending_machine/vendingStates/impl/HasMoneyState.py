from Design_patterns.design_vending_machine.vendingStates.state import State



class HasMoneyState(State):
    def __init__(self):
        print("Currently Vending machine is in HasMoneyState")

    def click_on_insert_coin_button(self, machine):
        return

    def click_on_start_product_selection_button(self, machine):
        from Design_patterns.design_vending_machine.vendingStates.impl.SelectionState import SelectionState
        machine.set_vending_machine_state(SelectionState())

    def insert_coin(self, machine, coin):
        print("Accepted the coin")
        machine.get_coin_list().append(coin)

    def choose_product(self, machine, code_number):
        raise Exception("You need to click on the start product selection button first")

    def get_change(self, return_change_money):
        raise Exception("You cannot get change in the hasMoney state")

    def dispense_product(self, machine, code_number):
        raise Exception("Product cannot be dispensed in the hasMoney state")

    def refund_full_money(self, machine):
        print("Returned the full amount back in the Coin Dispense Tray")
        from Design_patterns.design_vending_machine.vendingStates.impl.idleState import IdleState
        machine.set_vending_machine_state(IdleState(machine))
        return machine.get_coin_list()

    def update_inventory(self, machine, item, code_number):
        raise Exception("You cannot update inventory in hasMoney state")
