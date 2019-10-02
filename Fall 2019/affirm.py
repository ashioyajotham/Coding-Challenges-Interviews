#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'amounts_to_return_users' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY transaction_activities as parameter.
#
import datetime

class Card():
    def __init__(self, number):
        self.number = number
        self.transactions = []
    
    def add(self, tx):
        self.transactions += [tx]
        self.transactions.sort(key=lambda x: x.timestamp)
    


class Transaction():
    def __init__(self, txType, amount, timestamp):
        self.type = txType
        self.timestamp = timestamp


def amounts_to_return_users(transaction_activities):
    # Write your code here

    transaction_activities = [activity.split(',') for activity in transaction_activities]
    
    for i in range(len(transaction_activities)):
        i[3] = datetime.datetime.strptime(i[3], '%Y-%m-%d %H:%M:%S')

    transaction_activities.sort(key=lambda x: x[3])

    all_cards = {}
    for i in transaction_activities:
        card = i.split(',')

        if card[0] not in all_cards:
            all_cards[card[0]] = Card(card[0])

        all_cards[card[0]].add(Transaction(card[1], card[2], card[3]))
        
    
    




    

if __name__ == '__main__':