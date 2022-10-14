#--------------------------------------------------------------------------------------------------------
# Author: Bill Johnson
# Purpose: A renewed attempt at solving the problem from the interview on 10/13/2022 at 4pm Central
#
# Visit.py - Contains the Visit class definition
#--------------------------------------------------------------------------------------------------------
from OrderRules import OrderRule

class Visit:
    """
    Visit contains the logic of evaluating the OrderRules against a patients reason for a visit.

    Parameters:
    patient - Patient class filled with patient data
    reason - String containing the reason for the visit
    """
    def evaluatePatient(patient, reason):
        # Dictionary to contain orders that apply to this patient/reason
        orders = {}

        # Filter our collection for rules pertaining to this reason
        orders_for_reason = filter(lambda x: x.reason == reason, OrderRule.OrderRuleCollection )

        # Iterate our collection
        for order in orders_for_reason:
            
            # Skip if insurance plan is not allowed
            if patient.insurance in order.insurance_disallowed:
                continue

            # Skip if insurance plan doesn't qualify
            if len(order.insurance_allowed) > 0 and patient.insurance not in order.insurance_allowed:
                continue

            # Evalute patient age    
            if order.min_age <= patient.age:
                if order.max_age >= patient.age:

                    # If we get here, all qualifications have been met, add order to our dictionary
                    # Note: The dictionary essentially dedupes the orders
                    orders[order.order] = True

        # Return any orders in list form
        return list(orders.keys())