import aabb
import unittest

class TestAABB(unittest.TestCase):

    def setUp(self):
        self.box1 = aabb.AABB(0,0,2,2,2,1)
        self.box2 = aabb.AABB(4,1,2,3,0,0)

    def test_entry_exit_time(self):
        # test the values of [x/y]_time_[entry/exit]
        # self.assertEqual(aabb.AABB.sweptAABB(self.box1,self.box2), (1, 3))
        self.assertEqual(aabb.AABB.sweptAABB(self.box1,self.box2), (1, (-1,0)))

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAABB)
    unittest.TextTestRunner(verbosity=2).run(suite)