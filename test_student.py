import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\033[34m setUpClass \033[00m')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


    def setUp(self):
        print('\033[1;32m setUp \033[00m')
        self.student = Student('John', 'Snow')

    def tearDown(self):
        print('\033[1;31m tearDown \033[00m')    


    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Snow')


    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)


    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, 'john.snow@email.com')


    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))
        print('test_apply_extension')


    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!") 
         


if __name__ == '__main__':
    unittest.main()