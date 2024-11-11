from api.database.connection_database import Database
from unittest import TestCase

class TestDB(TestCase):
    def test_conextion_db(self):
        db_test = Database('sqlite:///test.db')
        self.assertIsNotNone(db_test)
    
