#!/usr/bin/env python3
"""
Python function to list all documents in a collection using PyMongo.
"""

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: A PyMongo collection object.

    Returns:
        A list of documents in the collection.
    """
    documents = []

    for document in mongo_collection.find():
        documents.append(document)

    return documents
