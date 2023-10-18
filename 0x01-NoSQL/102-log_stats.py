#!/usr/bin/env python3
from pymongo import MongoClient

if __name__ == "__main":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Count the number of logs
    num_logs = logs_collection.count_documents({})

    print(f"{num_logs} logs")

    # Count the number of each method
    methods = [
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE"
    ]

    print("Methods:")
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Count the number of status checks
    status_check_count = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

    # Count the top 10 IPs
    pipeline = [
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 10
        }
    ]

    top_ips = list(logs_collection.aggregate(pipeline))

    print("IPs:")
    for ip in top_ips:
        print(f"    {ip['_id']}: {ip['count']}")
