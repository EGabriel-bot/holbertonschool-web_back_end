#!/usr/bin/env python3
""" Task 8 """

def list_all(mongo_collection):
    """List all documents inside a collection"""
    if mongo_collection is None or mongo_collection.find() is None:
        return []
    return mongo_collection.find()
