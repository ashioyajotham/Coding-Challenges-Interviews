Imagine that here at Check we have a service that tracks how much money has been withheld from employee paychecks in taxes over the past 30 days in memory. We have a web server that runs in front of this service and exposes two URLs: /tax_paid and /get_30day_amount. The /tax_paid URL maps to a function in our service called tax_paid, which takes an employee ID, dollar amount, and timestamp as parameters. This function does not return anything.

    def tax_paid(employee_id, amount, timestamp):

The /get_30day_amount URL maps to a function in our service called get_30day_amount, which takes an employee ID as a parameter and returns the total amount of taxes paid by that employee over the past 30 days.

    def get_30day_amount(employee_id):


Our job is to implement these two functions. Assume that we have access to standard library implementations of basic data structures. Assume that variables declared in the global scope are accessible inside both of these functions.




taxDict = {}
def tax_paid(employee_id, amount, timestamp):
    
    if employee_id in taxDict:
        taxDict[employee_id] += [(amount, timestamp)]
    else:
        taxDict[employee_id] = [(amount, timestamp)]
    


def get_30day_amount(employee_id):
    
    total = 0
    if employee_id in taxDict:
        
        for tx in taxDict[employee_id]:
            if withinlast30days(tx):
                total += tx[0]  


    return total