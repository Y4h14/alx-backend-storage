#!/usr/bin/env python3
"""defines a script that provides some stats about Nginx logs"""
from pymongo import MongoClient

client = MongoClient()
nginx_collection = client.logs.nginx

logs_num = nginx_collection.count_documents({})
print(f'{logs_num} logs')
print('Methods:')
get = nginx_collection.count_documents({'method': 'GET'})
post = nginx_collection.count_documents({'method': 'POST'})
put = nginx_collection.count_documents({'method': 'PUT'})
patch = nginx_collection.count_documents({'method': 'PATCH'})
delete = nginx_collection.count_documents({'method': 'DELETE'})

print(f'    method GET: {get}')
print(f'    method POST: {post}')
print(f'    method PUT: {put}')
print(f'    method PATCH: {patch}')
print(f'    method DELETE: {delete}')

status = nginx_collection.count_documents({"method": 'GET', "path": '/status'})
print(f'{status} status check')
