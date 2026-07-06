# import unittest
# from survey import AnonymousSurvey
# #"""针对AnonymousSurvey类的测试"""
# class TestAnonymousSurvey(unittest.TestCase):
#     def test_store_single_response(self):
#         """测试单个答案会被妥善地存储"""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response('English')
        
#         self.assertIn('English', my_survey.responses)
    
#     def test_store_three_responses(self):
#         """测试三个答案会被妥善地存储"""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         responses = ['English', 'Chinese', 'Spanish']
#         for response in responses:
#             my_survey.store_response(response)
        
#         for response in responses:
#             self.assertIn(response, my_survey.responses)

# if __name__ == '__main__':
#     unittest.main()



import unittest
from survey import AnonymousSurvey
#"""针对AnonymousSurvey类的测试"""
class TestAnonymousSurvey(unittest.TestCase):
    #unittest.TestCase类包含方法setUp()，让我们只需创建这些对象一次，并在每个测试方法中使用它们。
#如果你在TestCase类中包含了方法setUp()，Python将先运行它，再运行各个以test_打头的方法。
# 这样，在你编写的每个测试方法中都可使用在方法setUp()中创建的对象了。
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Chinese', 'Spanish']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()