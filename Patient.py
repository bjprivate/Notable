#--------------------------------------------------------------------------------------------------------
# Author: Bill Johnson
# Purpose: A renewed attempt at solving the problem from the interview on 10/13/2022 at 4pm Central
#--------------------------------------------------------------------------------------------------------
class Patient:
    """
    Simple class to encapsulate basic patient data for these scenarios
    """
    def __init__(self, name, age, insurance):
        self.name = name
        self.age = age
        self.insurance = insurance

