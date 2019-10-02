#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calculate_total_owed' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY actions as parameter.
#

def calculate_total_owed(actions):
    # Write your code here
    owed = 0
    invoices = {}
    for action in actions:
        if "create" in action.lower():
            inputs = re.search(r'id=(\d+)&amount=(\d+)&currency=([A-Z]+)', action)
            id, amount, currency = inputs.group(1), inputs.group(2), inputs.group(3)

            try:
                if id not in invoices:
                    invoices[id] = Invoice(id, amount, currency, "created")
                    owed += invoices[id].amount
            except AssertionError:
                pass
            
        elif "finalize" in action.lower():
            inputs = re.search(r'id=(\d+)&amount=(\d+)&currency=([A-Z]+)', action)
            try:
                id, amount, currency = inputs.group(1), inputs.group(2), inputs.group(3)
                assert(id in invoices and currency == 'USD' and invoices[id].state == 'created')
                curr = invoices[id]
                owed += int(amount) - curr.amount
                invoices[id] = Invoice(id, amount, currency, "finalized")
            except AssertionError:
                pass
        else:
            id = re.search(r'id=(\d+)', action).group(1)
            try:
                assert(id in invoices and invoices[id].state == 'finalized')
                owed -= invoices[id].amount
                invoices[id].paid()
            except AssertionError:
                pass

    return owed

class Invoice:
    customerIds = set()

    def __init__(self, id, amount, currency, state):
        assert(id not in self.customerIds and currency == 'USD')
        self.id = id
        self.amount = int(amount)
        self.currency = currency
        self.state = state

    def paid(self):
        self.state = 'paid'

        

if __name__ == '__main__':