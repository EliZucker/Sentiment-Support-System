from datetime import datetime

import os
import uuid

from google.cloud import firestore


def get_client():
    credential_path = "YHack-2019-a87246a5ff6d.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
    return firestore.Client()


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
        :param data: The data to insert. The data must have a 'timestamp' - error will be thrown if it doesn't
        :param source: The source of the data to store under. Ex. twitter
        """
        if 'timestamp' not in data and type(data['timestamp']) == datetime:
            raise IndexError('Data must have a timestamp')

        doc_ref = self.db.collection(source).document(data_id)
        doc_ref.set(data)

    def validate_db(self):
        if self.db is None:
            self.db = get_client()

    def remove_source(self, source: str, batch_delete_size=100):
        col_ref = self.db.collection(source)

        while 1:
            docs = col_ref.limit(batch_delete_size).get()

            docs_deleted = 0
            for doc in docs:
                doc.reference.delete()
                docs_deleted += 1

            # if more docs to delete
            if docs_deleted < batch_delete_size:
                break

    def remove_sources(self, sources: list, batch_delete_size=100):
        for source in sources:
            self.remove_source(source=source, batch_delete_size=batch_delete_size)


if __name__ == '__main__':
    gdb = google_db()
