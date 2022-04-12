from firebase import firebase

class BancoDadosSingleton:

    _instance = None

    def __init__(self):
        self.firebase = firebase.FirebaseApplication("https://central-care-a0c23-default-rtdb.firebaseio.com/", None)
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance