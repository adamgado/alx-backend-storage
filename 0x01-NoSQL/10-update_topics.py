#!/usr/bin/env python3
"""changes all topics of school document based on name"""


def update_topics(mongo_collection, name, topics):
    """changes all topics"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
