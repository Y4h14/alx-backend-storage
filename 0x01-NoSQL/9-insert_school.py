#!/usr/bin/python3
"""defines a functio that inserts to a colection"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insetrts items into a mongo collection

    Parameters:
    mongo_colletction (Collection): mongo db collection
    kwargs (dict): documetn't items to insetrt into a dictionsary

    Returns:
    int: the id of the newely inserted documetns
    """
    return mongo_collection.insert_one(kwargs).inserted_id
