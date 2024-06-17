#!/usr/bin/env python3
"""defines a script that provides some stats about Nginx logs"""
from pymongo import MongoClient

if __name__ == '__main__':

    client = MongoClient()
    nginx_collection = client.logs.nginx

    logs_num = nginx_collection.count_documents({})
    print('{} logs'.format(logs_num))
    print('Methods:')
    get = nginx_collection.count_documents({'method': 'GET'})
    post = nginx_collection.count_documents({'method': 'POST'})
    put = nginx_collection.count_documents({'method': 'PUT'})
    patch = nginx_collection.count_documents({'method': 'PATCH'})
    delete = nginx_collection.count_documents({'method': 'DELETE'})

    print('    method GET: {}'.format(get))
    print('    method POST: {}'.format(post))
    print('    method PUT: {}'.format(put))
    print('    method PATCH: {}'.format(patch))
    print('    method DELETE: {}'.format(delete))

    status = nginx_collection.count_documents({"method": 'GET', "path": '/status'})
    print('{} status check'.format(status))
