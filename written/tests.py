from django.test import TestCase
from written.models import DailyKnown
from datetime import datetime

# Create your tests here.
class DailyKnowsModelTest(TestCase):
    def setUp(self):
        main_class = DailyKnown()
        main_class.date = datetime.strptime('2020-03-02', '%Y-%m-%d')
        main_class.title = 'Teste test'
        self.main_class = main_class

    def  test_str(self):
        now = str(self.main_class)
        expected = 'Teste test - 2020-03-02'
        self.assertEquals(now, expected)
