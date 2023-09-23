from Design_patterns.CORHiring.chain_creator import ChainCreator

if __name__ == "__main__":
    chain_creator = ChainCreator()
    manager = chain_creator.create_chain()

    # Test different salary approval requests
    manager.approve_salary(5000)
    manager.approve_salary(15000)
    manager.approve_salary(45000)
    manager.approve_salary(5000000)
