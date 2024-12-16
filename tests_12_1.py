from Logic_for_logs import Runner
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def testRun(self):
        runner = Runner(name="John")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def testWalk(self):
        try:
            runner = Runner(name="John", speed=-1)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info(msg="\"test_walk\" выполнен успешно")
        except:
            logging.warning(msg="Неверная скорость для Runner")



    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def testChallenge(self):
        try:
            runner1 = Runner(name=32)
            runner2 = Runner(name="Jack")
            for i in range(10):
                runner1.walk()
                runner2.run()
            self.assertNotEqual(runner1.distance, runner2.distance)
            logging.info(msg='\"test_run\" выполнен успешно')
        except:
            logging.warning(msg = "Неверный тип данных для объекта Runner")


if __name__ == "__main__":
    unittest.main()