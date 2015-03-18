#!/usr/bin/env python
# encoding: utf-8

import json
from datetime import date
import random

class Bill():

    def __init__(self, billId, userId):
        self.billId = billId
        self.userId = userId

    # Eventually this should pull from a database instead of generating random
    # or pre-generated data.
    def getDictionary(self):
        startDate = date.today().replace(day=1, month=1).toordinal()
        endDate = date.today().replace(day=30, month=12).toordinal()
        randomDay = date.fromordinal(random.randint(startDate, endDate))
        return {
            'billId' : self.billId,
            'imageUrl' : 'http://i2.cdn.turner.com/cnn/dam/assets/130704041649-sesame-street-muppet-elmo-horizontal-gallery.jpg',
            'translations' : [{'title' : 'Bill 1 with a really really really really long name', 'upvotes' : 200, 'author' : 'Bill Nye'},
                              {'title' : 'Bill • 1.1', 'upvotes' : 100, 'author' : 'Doron'},
                              {'title' : 'Bill 1.2', 'upvotes' : 50, 'author' : 'Daniel'}],
            'voteDate' : randomDay.strftime('%Y,%m,%d'),
            'scope' : random.randint(1, 3), #figure out enums in python
            'govVote' : random.randint(1, 3),
            'userVote' : random.randint(1, 3),
        }