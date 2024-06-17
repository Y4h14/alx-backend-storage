#!/usr/bin/env python3
"""defines a function that changes all topics of a documetn"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    updated a mongo collection document

    Parameters:
    mongo_collection (Collection): the db collection.
    name (string): the school name to update.
    topics (List[strings]): the list of topics apprached in shcool

    Returns:
    None.
    """
    mongo_collection.update_one({'name': name},
                                {'$set': {'topics': topics}})
