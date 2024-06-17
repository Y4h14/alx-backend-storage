#!/usr/bin/env python3
"""defines a function that query a mongo db"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    finds schools in a collection with specified topic

    Parameters:
    mongo_collection (Collection): the pymongo collection.
    topic (string): the topic to be searched.

    Returns:
    List: a list of schools having a specific topic.
    """
    results = mongo_collection.find({'topics': topic})
    return [result['name'] for result in results]
