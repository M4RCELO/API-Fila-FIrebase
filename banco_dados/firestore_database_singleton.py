import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class FirestoreDatabaseSingleton:
    _instance = None

    def __init__(self):
        self._cred = credentials.Certificate('./ServiceAccountKey.json')
        firebase_admin.initialize_app(self._cred)

        self.db = firestore.client()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
