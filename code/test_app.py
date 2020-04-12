import unittest
import app

class TestApp(unittest.TestCase):
    
    def test_result(self):
        result = (app.main({'height':168, 'weight':87}, "test_value"))
        self.assertEqual(result['bmi'],30.82)

if __name__ == '__main__':
    unittest.main()

