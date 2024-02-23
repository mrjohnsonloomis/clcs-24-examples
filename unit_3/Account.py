class Account:
    def __init__(self, owner, balance):
        self._owner = owner        # Protected member
        self.__balance = balance   # Private member

    def deposit(self, amount: int)->None:
        '''Adds the amount to the balance'''
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount} to the balance") # console output
        else:
            print("Deposit amount must be positive") # for debugging

    def withdraw(self, amount: int)->None:
        '''Subtracts the amount from the balance'''
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from the balance")
        else:
            print("Invalid withdrawal amount")

    def get_balance(self)->int:
        '''Returns the balance of the account'''
        return self.__balance

    def get_owner(self)->str:
        '''Returns the owner of the account'''
        return self._owner


