#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log():
    """provides some stats about Nginx logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    total = logs_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    doc_counts = []
    for a in methods:
        doc_counts.append(logs_collection.count_documents({"method": a}))
    path = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {doc_counts[0]}")
    print(f"\tmethod POST: {doc_counts[1]}")
    print(f"\tmethod PUT: {doc_counts[2]}")
    print(f"\tmethod PATCH: {doc_counts[3]}")
    print(f"\tmethod DELETE: {doc_counts[4]}")
    print(f"{path} status check")


if __name__ == "__main__":
    log()
