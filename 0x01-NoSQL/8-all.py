#!/usr/bin/env python3
"""defines a function to list elements in a collectin"""
import pymongo
import pymongo.mongo_client


def list_all(mongo_collection):
    """
    lists all documents in a collection

    Parameters:
    mongo_collection (Collection): a mongo db collection

    Returns:
    a dict of all documents in a collection or {}

    """
    return mongo_collection.find()
