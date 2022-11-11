import unittest

from services.algo_service.db.data_db_api import save_history, load_history
from services.algo_service.db.tables import InvestItem


class MyTestCase(unittest.TestCase):
    def test_save_history(self):
        a = InvestItem(name='t1', country='q', id='id', history=[1])
        print("InvestItem crated")
        save_history(a)
        print("InvestItem saved")
        b = load_history(a)
        print("InvestItem loaded")
        self.assertEqual(a.id, b.id)  # add assertion here


if __name__ == '__main__':
    unittest.main()
