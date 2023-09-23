from Design_patterns.design_vending_machine.inventory import Inventory
from Design_patterns.design_vending_machine.vendingStates.impl.idleState import IdleState


class VendingMachine:
    def __init__(self):
        self.vending_machine_state = IdleState()
        self.inventory = Inventory(10)
        self.coin_list = []

    def get_vending_machine_state(self):
        return self.vending_machine_state

    def set_vending_machine_state(self, vending_machine_state):
        self.vending_machine_state = vending_machine_state

    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory):
        self.inventory = inventory

    def get_coin_list(self):
        return self.coin_list

    def set_coin_list(self, coin_list):
        self.coin_list = coin_list
