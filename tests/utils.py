import unittest
from auairtools.utils import TimeStamp


class TestTimeStamp(unittest.TestCase):

    def setUp(self):
        self.time_dict_1 = {'year': 2019,
            'month': 11,
            'day': 7,
            'hour': 11,
            'min': 4,
            'sec': 3,
            'ms': 12000}



    def test_constructor(self):
        """ Test the default constructor """

        t = TimeStamp(self.time_dict_1)
        
        self.assertEqual(t.year, self.time_dict_1['year'], "Expected years to be equal.")
        self.assertEqual(t.month, self.time_dict_1['month'], "Expected months to be equal.")
        self.assertEqual(t.day, self.time_dict_1['day'], "Expected days to be equal.")
        self.assertEqual(t.hour, self.time_dict_1['hour'], "Expected hours to be equal.")
        self.assertEqual(t.mins, self.time_dict_1['min'], "Expected mins to be equal.")
        self.assertEqual(t.sec, self.time_dict_1['sec'], "Expected secs to be equal.")
        self.assertEqual(t.ms, self.time_dict_1['ms'], "Expected ms to be equal.")


    def test_print(self):
        t = TimeStamp(self.time_dict_1)
        self.assertEqual(str(t), 'TimeStamp: {\'year\': 2019, \'month\': 11, \'day\': 7, \'hour\': 11, \'min\': 4, \'sec\': 3, \'ms\': 12000}', "Expected strings to be same.")

if __name__ == '__main__':
    unittest.main()