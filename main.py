#--------------------------------------------------------------------------------------------------------
# Author: Bill Johnson
# Purpose: A renewed attempt at solving the problem from the interview on 10/13/2022 at 4pm Central
#
# main.py - The main application containing the entry point
#--------------------------------------------------------------------------------------------------------

from OrderRules import OrderRule
from Visit import Visit
from Patient import Patient

def loadScenarioData():
    """
    LoadTestData loads the 4 provided scenarios into the OrderRule collection
    """
    print("Loading scenario data")

    # Scenario 1
    OrderRule.AddOrderRule(OrderRule("annual_exam", "folic acid", 20, 40))
    OrderRule.AddOrderRule(OrderRule("annual_exam", "complete blood count", 20, 40))

    # Scenario 2
    OrderRule.AddOrderRule(OrderRule("annual_exam", "complete blood count", 41, insurance_allowed=["medicare"]))
    OrderRule.AddOrderRule(OrderRule("annual_exam", "cancer screen", 41, insurance_allowed=["medicare"]))

    # Scenario 3
    OrderRule.AddOrderRule(OrderRule("annual_exam", "complete blood count", 41, insurance_disallowed=["medicare"]))
    OrderRule.AddOrderRule(OrderRule("annual_exam", "a1c", 41, insurance_disallowed=["medicare"]))
    OrderRule.AddOrderRule(OrderRule("annual_exam", "cancer screen", 41, insurance_disallowed=["medicare"]))

    # Scenario 3
    OrderRule.AddOrderRule(OrderRule("postop_hip", "xray, hip"))
    OrderRule.AddOrderRule(OrderRule("postop_hip", "stitch removal"))

    #OrderRule.DumpRules("annual_exam")

def testVisit(patient, reason):
    """
    testVisit tests a single patient/reason visit to determine the orders that would follow
    """
    print("-"*80)
    print(f"Evaluating {patient.name} visit for {reason}: age: {patient.age}, insurance: {patient.insurance}")
    orders = Visit.evaluatePatient(patient, reason)
    if len(orders) > 0:
        print(f"\tOrders: {orders}")
    else:
        print("No Orders")
# Entry point
print("Notable problem script running")

loadScenarioData()

testVisit(Patient("Patient 0-1", 55, "some ppo"), "postop_hip")
testVisit(Patient("Patient 0-2", 55, "medicare"), "postop_hip")

testVisit(Patient("Patient 1-1", 55, "some ppo"), "annual_exam")
testVisit(Patient("Patient 1-2", 40, "some ppo"), "annual_exam")
testVisit(Patient("Patient 1-3", 40, "medicare"), "annual_exam")
testVisit(Patient("Patient 1-4", 41, "some ppo"), "annual_exam")
testVisit(Patient("Patient 1-5", 41, "medicare"), "annual_exam")
testVisit(Patient("Patient 1-6", 10, "some ppo"), "annual_exam")
testVisit(Patient("Patient 1-7", 10, "medicare"), "annual_exam")

testVisit(Patient("Patient 2-1", 55, "some ppo"), "unknown_reason")

