from Design_patterns.design_vending_machine.vendingStates.impl.dispense_state import DispenseState
from Design_patterns.design_vending_machine.vendingStates.impl.idleState import IdleState
from Design_patterns.design_vending_machine.vendingStates.state import State


class SelectionState(State):
    def __init__(self):
        print("Currently Vending machine is in SelectionState")

    def click_on_insert_coin_button(self, machine):
        raise Exception("You cannot click on the insert coin button in the Selection state")

    def click_on_start_product_selection_button(self, machine):
        return

    def insert_coin(self, machine, coin):
        raise Exception("You cannot insert a coin in the selection state")

    def choose_product(self, machine, code_number):
        item = machine.get_inventory().get_item(code_number)
        paid_by_user = sum(coin.value for coin in machine.get_coin_list())

        if paid_by_user < item.get_price():
            print(f"Insufficient Amount, Product you selected is for price: {item.get_price()} and you paid: {paid_by_user}")
            self.refund_full_money(machine)
            raise Exception("Insufficient amount")
        elif paid_by_user >= item.get_price():
            if paid_by_user > item.get_price():
                self.get_change(paid_by_user - item.get_price())
            machine.set_vending_machine_state(DispenseState(machine, code_number))

    def get_change(self, return_extra_money):
        print("Returned the change in the Coin Dispense Tray:", return_extra_money)
        return return_extra_money

    def refund_full_money(self, machine):
        print("Returned the full amount back in the Coin Dispense Tray")
        machine.set_vending_machine_state(IdleState(machine))
        return machine.get_coin_list()

    def dispense_product(self, machine, code_number):
        raise Exception("Product cannot be dispensed in the Selection state")

    def update_inventory(self, machine, item, code_number):
        raise Exception("Inventory cannot be updated in the Selection state")
