# Imports the Google Cloud client library
from google.cloud import datastore

def get_and_increment_visitor_counter():
    # Instantiates a client
    datastore_client = datastore.Client()

    # The kind for the new entity
    kind = "counter"


    query = datastore_client.query(kind=kind)

    ##print (help(query.fetch))
    query_results=query.fetch()
    for row in query_results:
        previous_visitor_count=list(row.values())[0]
        return previous_visitor_count




#TODO: add more granualar filter aka property id in filter: https://cloud.google.com/datastore/docs/concepts/queries\