#!/usr/bin/env python3
"""Define a Python function that returns the list of school having a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """"Returns the list of school having a specific topic"""
    return list(mongo_collection.find({"topic": topic}))
