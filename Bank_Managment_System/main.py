from bank import Bank
from operationManager import OperationManager

if __name__ == "__main__":
    bank = Bank('Bank of America', 'New York', 1000000)
    operation = OperationManager()
    operation.main_menu(bank)


