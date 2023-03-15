#!/usr/bin/env python3
""" Task 9 """

def insert_school(mongo_collection, **kwargs):
    """ insert a document to a collection """
    args = {}
    for key,value in kwargs.items():
        args[key] = value
    mongo_collection.insert_one(args)
    return mongo_collection.id
