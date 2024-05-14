#!/user/bin/env python3
'''Simple module since it has a simple function `list_all(collection)`.'''


def list_all(model_collection: [pymongo]) -> List[dict]:
    '''Lists all documents in a mongo collection.

    Parameters:
        - model_collection: the collection that contains the documents

    Return: List all documents of a the given collection
    '''
    return model_collection.find()
