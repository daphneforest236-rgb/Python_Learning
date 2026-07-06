
#能通过的测试
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    #须以test_打头，会在运行test_name_function.py时自动运行
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()

# #不能通过的测试
# import unittest
# from name_function import get_formatted_name

# class NamesTestCase(unittest.TestCase):
#     def test_first_last_name(self):
#         formatted_name = get_formatted_name('janis','joplin')
#         self.assertEqual(formatted_name,'Janis Joplin')

# unittest.main()