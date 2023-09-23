from Design_patterns.design_vending_machine.vendingStates.impl.HasMoneyState import HasMoneyState
from Design_patterns.design_vending_machine.vendingStates.state import State


class IdleState(State):

    def __init__(self, machine=None):
        print("Currently Vending machine is in IdleState")
        if machine:
            machine.set_coin_list([])

    def click_on_insert_coin_button(self, machine):
        machine.set_vending_machine_state(HasMoneyState())

    def click_on_start_product_selection_button(self, machine):
        raise Exception("First, you need to click on the insert coin button")

    def insert_coin(self, machine, coin):
        raise Exception("You cannot insert a coin in the idle state")

    def choose_product(self, machine, code_number):
        raise Exception("You cannot choose a product in the idle state")

    def get_change(self, return_change_money):
        raise Exception("You cannot get change in the idle state")

    def refund_full_money(self, machine):
        raise Exception("You cannot get refunded in the idle state")

    def dispense_product(self, machine, code_number):
        raise Exception("Product cannot be dispensed in the idle state")

    def update_inventory(self, machine, item, code_number):
        machine.get_inventory().add_item(item, code_number)
