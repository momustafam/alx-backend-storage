#!/user/bin/env python3
'''Simple module since it has a simple function `list_all(collection)`.'''


def list_all(mongo_collection):
    '''Lists all documents in a mongo collection.

    Parameters:
        - model_collection: the collection that contains the documents

    Return: List all documents of a the given collection
    '''
    return mongo_collection.find()
