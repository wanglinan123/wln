import unittest

class IntegerArithmeticTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("用例前，只执行一次")

    @classmethod
    def tearDownClass(cls):
        print("用例后，只调用一次")

    # def setUp(self):
    #     #每个用例执行之前，先执行一次
    #     print("先打开浏览器")
    #
    # def tearDown(self):
    #     #用例执行完之后，调用一次
    #     print("关闭浏览器")

    def test_1(self):  # test method names begin with 'test'
        '''用例说明：111'''
        print("11111111")
        a="admin"  #实际结果
        b="admin1"  #期望结果
        self.assertNotIn(a,b)
        #self.assertNotEqual(a,b)
        #self.assertTrue(a != b)

    def test_a(self):
        '''用例说明：aaaaa'''
        print("2222222")
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

    def test_A(self):
        '''用例说明：AAAA'''
        print("333333")
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()