from lab_one import task_one
from lab_one import task_two
from lab_one import task_three
from lab_one import task_four
from lab_one import task_five


import unittest

class TestAssignmentOne(unittest.TestCase):

    def test_task_one(self):
        self.assertEqual(task_one('mobile'), 'mbl')
        self.assertEqual(task_one('MOBILE'), 'MBL')
        self.assertEqual(task_one('MobIlE'), 'Mbl')

    def test_task_two(self):
        self.assertEqual(task_two('This is javaScript','i'), [2, 5, 15])


    def test_task_three(self):
        self.assertEqual(task_three(3), [[1],[2,4],[3,6,9]])

    def test_task_four(self):
        self.assertEqual(task_four('t',5,10),25)
        self.assertEqual(task_four('T',5,10),25)
        self.assertEqual(task_four('r',5,10),50)
        self.assertEqual(task_four('R',5,10),50)
        self.assertEqual(task_four('c',10,1),314.1592653589793)
        self.assertEqual(task_four('C',10,1),314.1592653589793)
        self.assertEqual(task_four('s',10,1),100)
        self.assertEqual(task_four('S',10,1),100)
    def test_task_five(self):
        l1 = ["ahmed", "fatma", "ibrahim"]
        d1 = {'a':['ahmed'], 'f':['fatma'],'i':['ibrahim']}
        self.assertEqual(task_five(l1), d1)
if __name__ == '__main__':
    unittest.main()
