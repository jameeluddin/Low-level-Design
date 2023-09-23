from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def click_on_insert_coin_button(self, machine):
        pass

    @abstractmethod
    def click_on_start_product_selection_button(self, machine):
        pass

    @abstractmethod
    def insert_coin(self, machine, coin):
        pass

    @abstractmethod
    def choose_product(self, machine, code_number):
        pass

    @abstractmethod
    def get_change(self, return_change_money):
        pass

    @abstractmethod
    def dispense_product(self, machine, code_number):
        pass

    @abstractmethod
    def refund_full_money(self, machine):
        pass

    @abstractmethod
    def update_inventory(self, machine, item, code_number):
        pass
