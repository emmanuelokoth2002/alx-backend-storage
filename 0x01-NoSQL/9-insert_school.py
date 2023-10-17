#!/usr/bin/env python3
"""
Python function to insert a new document into a collection based on kwargs.
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the MongoDB collection with the
    provided keyword arguments.

    Args:
        mongo_collection: A PyMongo collection object.
        **kwargs: Keyword arguments representing the document attributes.

    Returns:
        The new _id of the inserted document.
    """
    new_document = kwargs
    result = mongo_collection.insert_one(new_document)
    return result.inserted_id
