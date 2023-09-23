from Design_patterns.CORHiring.director import Director
from Design_patterns.CORHiring.hiring_managers import HiringManager
from Design_patterns.CORHiring.senior_managers import SeniorManager


class ChainCreator:
    def create_chain(self):
        hiring_manager = HiringManager(10000, "Mike")
        senior_manager = SeniorManager(30000, "Bill")
        director = Director(50000, "Ayush")

        hiring_manager.set_manager(senior_manager)
        senior_manager.set_manager(director)

        return hiring_manager
