from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def testRun(self):
        runner = Runner(name="John")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def testWalk(self):
        runner = Runner(name="John")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def testChallenge(self):
        runner1 = Runner(name="John")
        runner2 = Runner(name="Jack")
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()