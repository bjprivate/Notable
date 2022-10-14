#--------------------------------------------------------------------------------------------------------
# Author: Bill Johnson
# Purpose: A renewed attempt at solving the problem from the interview on 10/13/2022 at 4pm Central
#--------------------------------------------------------------------------------------------------------
class OrderRule:
    """
    OrderRule is the class that contains the various 'rules' for when an order applies
    """
    OrderRuleCollection = []

    def __init__(self, reason, order, min_age=0, max_age=1000, insurance_allowed = [], insurance_disallowed = []):
        """
        Simple constructor for an OrderRule

        Parameters:
        reason - The reason string for the visit e.g. annual_exam
        order - An order string that will come out of this reason if all conditions are met
        min_age - Minimum age of the patient, 0 is effectively no minimum
        max_age - Maximum age of the patient, default of 1000 is effectively  no maximu
        insurance_allowed - An array of qualifed insurances, empty array means ANY
        insurance_disallowed - An array of insurances that do not qualify
        """
        self.order = order
        self.reason = reason
        self.min_age = min_age
        self.max_age = max_age
        self.insurance_allowed = insurance_allowed
        self.insurance_disallowed = insurance_disallowed

    def AddOrderRule(orderRule):
        """
        AddOrderRule
        Simple helper method to add an order rule to the OrderRulesCollection
        """
        OrderRule.OrderRuleCollection.append(orderRule)

    def DumpRules(reason):
        """
        DumpRules
        Simple helper method to dump rules for a given 'reason'

        Parameters:
        reason - The reason for the visit e.g. annual_exam
        """
        print(f"Orders for {reason}")
        for order in filter(lambda x: x.reason == reason, OrderRule.OrderRuleCollection ):
            print(f"   {order.order} Min {order.min_age} Max {order.max_age} Ins: {order.insurance_allowed} Dis: {order.insurance_disallowed}")        

    