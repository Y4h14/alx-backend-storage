#!/usr/bin/env python3
"""defines a fucntion that returns all students sorted by average score"""
import pymongo


def top_students(mongo_collection):
    """
    returns all students sorted by average score

    Parameters:
    mongo_collection (Collection): a mongodb collection

    Returns:
    (List): a list of all students sorted by avg score
    """
    top_students = [
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]

    # Execute the aggregation pipeline
    results = list(mongo_collection.aggregate(top_students))
    return results
