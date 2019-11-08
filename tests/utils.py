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

        self.time_dict_2 = {'year': 2019,
            'month': 11,
            'day': 7,
            'hour': 11,
            'min': 4,
            'sec': 3,
            'ms': 11800}    

        self.time_dict_3 = {'year': 2012,
            'month': 10,
            'day': 3,
            'hour': 12,
            'min': 2,
            'sec': 3,
            'ms': 11800} 

        self.time_dict_4 = {'year': 2012,
            'month': -10,
            'day': 3,
            'hour': -12,
            'min': 2,
            'sec': 3,
            'ms': -11800}         



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


    def test_sub(self):
        t1 = TimeStamp(self.time_dict_1)
        t2 = TimeStamp(self.time_dict_2)
        t3 = TimeStamp(self.time_dict_3)

        self.assertEqual(str(t1-t2), 'TimeStamp: {\'year\': 0, \'month\': 0, \'day\': 0, \'hour\': 0, \'min\': 0, \'sec\': 0, \'ms\': 200}', "Expected TimeStamps to be same.")
        self.assertEqual(str(t1-t3), 'TimeStamp: {\'year\': 7, \'month\': 1, \'day\': 4, \'hour\': -1, \'min\': 2, \'sec\': 0, \'ms\': 200}', "Expected TimeStamps to be same.")
        self.assertEqual(str(t2-t1), 'TimeStamp: {\'year\': 0, \'month\': 0, \'day\': 0, \'hour\': 0, \'min\': 0, \'sec\': 0, \'ms\': -200}', "Expected TimeStamps to be same.")
        self.assertEqual(str(t1-t1), 'TimeStamp: {\'year\': 0, \'month\': 0, \'day\': 0, \'hour\': 0, \'min\': 0, \'sec\': 0, \'ms\': 0}', "Expected TimeStamps to be same.")

    def test_abs(self):
        ''' Test absoluate overloaded function. '''
        t1 = TimeStamp(self.time_dict_1)
        t4 = TimeStamp(self.time_dict_4) 
        self.assertEqual(str(abs(t1)), 'TimeStamp: {\'year\': 2019, \'month\': 11, \'day\': 7, \'hour\': 11, \'min\': 4, \'sec\': 3, \'ms\': 12000}', "Expected TimeStamps to be same.")
        self.assertEqual(str(abs(t4)), 'TimeStamp: {\'year\': 2012, \'month\': 10, \'day\': 3, \'hour\': 12, \'min\': 2, \'sec\': 3, \'ms\': 11800}', "Expected TimeStamps to be same.")

    def test_le(self):
        ''' Test less or equal overloaded operation. '''
        t1 = TimeStamp(self.time_dict_1)
        t2 = TimeStamp(self.time_dict_2)
        t3 = TimeStamp(self.time_dict_3)        
        t4 = TimeStamp(self.time_dict_4) 
        self.assertTrue(t1>=t1)
        self.assertTrue(t1>=t2)
        self.assertTrue(t2>=t3)
        self.assertTrue(t3>=t4)


if __name__ == '__main__':
    unittest.main()