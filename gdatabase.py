from datetime import datetime, timedelta

import uuid

from google.cloud import firestore

from util import setup_credentials


def get_client():
    setup_credentials()
    return firestore.Client()


def remove_source_by_ref(col_ref, batch_delete_size=100):
    while 1:
        docs = col_ref.limit(batch_delete_size).get()

        docs_deleted = 0

        for doc in docs:
            doc.reference.delete()
            docs_deleted += 1

        # if more docs to delete
        if docs_deleted < batch_delete_size:
            break


def get_data_from_source_ref(source_ref, query):
    """
    Gets data from a particular source ref

    :param source_ref: A source to get from
    :param query: A query function
    """
    return convert_query_to_dict(query(source_ref).stream())


def convert_query_to_dict(query_stream):
    """
    Converts the results of a raw query to a dict
    :param query_stream: The result of a query
    :return: A list of dicts
    """
    formatted_docs = []
    for doc in query_stream:
        formatted_docs.append(doc.to_dict())
    return formatted_docs


def get_data_from_source_refs(source_refs,
                              query):
    """
    Gets data from many sources
    :param source_refs: A list of source refs
    :param query: A query to execute
    :return: A dict of source to response dict
    """
    response = ***REMOVED******REMOVED***
    for source_ref in source_refs:
        response[source_ref.id] = get_data_from_source_ref(source_ref=source_ref, query=query)
    return response


class google_db:
    def __init__(self):
        """
        Initializes a connection to cloud firestore database.
        """
        self.db = get_client()

    def store_data(self, data: dict, data_id: str = None, source: str = u'default'):
        """
        Stores data in the database.

        :param data_id: The id of the data to insert. Must be unique or will overwrite data. By default is random
        :param data: The data to insert. The data must have a 'timestamp'
        :param source: The source of the data to store under. Ex. twitter
        """
        if 'timestamp' not in data and type(data['timestamp']) == datetime:
            raise IndexError('Data must have a timestamp')

        if data_id is None:
            data_id = uuid.uuid4().hex

        doc_ref = self.db.collection(source).document(data_id)
        doc_ref.set(data)

    def validate_db(self):
        if self.db is None:
            self.db = get_client()

    def remove_source(self, source: str, batch_delete_size=100):
        """
        Removes a single source from the db

        :param source: A string representing a source name
        :param batch_delete_size: The batch delete size
        """

        col_ref = self.db.collection(source)

        remove_source_by_ref(col_ref, batch_delete_size)

    def remove_sources(self, sources: list, batch_delete_size=100):
        """
        Removes all the sources in a list of sources
        :param sources: A list of strings with each representing a source
        :param batch_delete_size: The batch delete size
        """

        for source in sources:
            self.remove_source(source=source, batch_delete_size=batch_delete_size)

    def get_data_from_source(self, source, query):
        """
        Gets data from a particular source

        :param source: A source to get from
        :param query: A query function
        """
        return get_data_from_source_ref(source_ref=self.db.collection(source), query=query)

    def get_data_from_source_in_range(self,
                                      source: str,
                                      timestamp1: datetime,
                                      timestamp2: datetime,
                                      additional_query=None):
        """
        Gets data from a source
        :param source: The source to pull data from
        :param timestamp1: A timestamp older than timestamp2
        :param timestamp2: A timestamp more recent than timestamp1
        :param additional_query: Any additional query to add.
        Any additional query to add (a function that takes an input and filters eg x.where(...)
        :return: A response from the google api
        """
        if additional_query is None:
            def query(doc):
                return doc.where('timestamp', '>=', timestamp1).where('timestamp', '<=', timestamp2)

            return self.get_data_from_source(source=source, query=query)
        else:
            def query(doc):
                return additional_query(doc.where('timestamp', '>=', timestamp1).where('timestamp', '<=', timestamp2))

            return self.get_data_from_source(source=source, query=query)

    def get_data_from_all(self, query):
        """
        Gets the data from all the collections
        :param query: A query to filter data by
        :return A dictionary of source_ref to response
        """
        sources = self.db.collections()
        response = ***REMOVED******REMOVED***
        for source_ref in sources:
            response[source_ref] = get_data_from_source_ref(source_ref=source_ref, query=query)
        return response

    def get_data_from_sources_in_range(self,
                                       sources: list,
                                       timestamp1: datetime,
                                       timestamp2: datetime,
                                       additional_query=None):
        """
        Gets data from a list of sources
        :param sources: A list of strings to get data for
        :param timestamp1: A timestamp older than timestamp2
        :param timestamp2: A timestamp more recent than timestamp1
        :param additional_query: Any additional query to add (a function that takes an input and filters eg x.where(...)
        :return: A dict of source to response dict
        """
        if additional_query is None:
            def query(doc):
                return doc.where('timestamp', '>=', timestamp1).where('timestamp', '<=', timestamp2)
        else:
            def query(doc):
                return additional_query(doc.where('timestamp', '>=', timestamp1).where('timestamp', '<=', timestamp2))

        source_refs = []
        for source in sources:
            source_refs.append(self.db.collection(source))
        return get_data_from_source_refs(source_refs, query=query)

    def get_data_from_all_in_range(self,
                                   timestamp1: datetime,
                                   timestamp2: datetime,
                                   additional_query=None):
        """
        Gets data from a source
        :param timestamp1: A timestamp older than timestamp2
        :param timestamp2: A timestamp more recent than timestamp1
        :param additional_query: Any additional query to add (a function that takes an input and filters eg x.where(...)
        :return: A dict of source to response dict
        """
        if additional_query is None:
            def query(doc):
                return doc.where('timestamp', '>=', timestamp1).where('timestamp', '<=', timestamp2)
        else:
            def query(doc):
                return additional_query(doc.where('timestamp', '>=', timestamp1).where('timestamp', '<=', timestamp2))

        sources = self.db.collections()
        return get_data_from_source_refs(sources, query=query)

    def clear_database(self):
        """
        REMOVES ALL COLLECTIONS DO NOT USE!!
        """
        sources = self.db.collections()
        for source_ref in sources:
            remove_source_by_ref(source_ref)


if __name__ == '__main__':
    # pass
    gdb = google_db()

    # for i in range(300):
    #     gdb.store_data(***REMOVED***'timestamp': datetime.now(), 'sentiment': 'angry'***REMOVED***, source='sentiment')

    # gdb.remove_source(source='twitter')

    # def filterer(x):
    #     return x.where('timestamp', '==', datetime.now())

    # docs = gdb.get_data_from_source_in_range('twitter', datetime.now() - timedelta(days=1), datetime.now())
    # docs = gdb.get_data_from_all_in_range(datetime.now() - timedelta(days=1), datetime.now(), filterer)

    # i = 0
    # for doc in docs:
    #     i += 1
    #     print(docs)
    #     # print(doc, docs[doc])
    #
    # print(i)

    # gdb.clear_database()
