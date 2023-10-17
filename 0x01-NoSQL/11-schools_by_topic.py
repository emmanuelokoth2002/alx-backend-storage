#!/usr/bin/env python3
"""
Python function to return a list of schools having a specific topic.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have the specified topic.

    Args:
        mongo_collection: A PyMongo collection object.
        topic (string): The topic to search for.

    Returns:
        A list of school documents that have the specified topic.
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
