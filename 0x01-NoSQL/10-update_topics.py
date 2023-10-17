#!/usr/bin/env python3
"""
Python function to update topics of a school document based on the name.
"""

def update_topics(mongo_collection, name, topics):
    """
    Changes the topics of a school document based on the name.

    Args:
        mongo_collection: A PyMongo collection object.
        name (string): The name of the school to update.
        topics (list of strings): The list of topics approached in the school.

    Returns:
        None.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
