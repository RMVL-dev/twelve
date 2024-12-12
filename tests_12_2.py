from unittest import TestCase
import unittest

from LogicForTest import Runner, Tournament


class TournamentTest(TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = Runner("Усейн", 10)
        self.Andrey = Runner("Андрей", 9)
        self.Nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(f"{result} = {cls.all_results[result]}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def testTournament1(self):
        tournament = Tournament(90, self.Usain, self.Nick)
        finishers = tournament.start()

        self.all_results["first_test"] = f"1: {finishers[1]}, 2: {finishers[2]}"
        self.assertEqual(str(finishers[2]), "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def testTournament2(self):
        tournament = Tournament(90, self.Andrey, self.Nick)
        finishers = tournament.start()

        self.all_results["second_test"] = f"1: {finishers[1]}, 2: {finishers[2]}"
        self.assertEqual(str(finishers[2]), "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def testTournament3(self):
        tournament = Tournament(90, self.Usain, self.Nick, self.Andrey)
        finishers = tournament.start()

        self.all_results["third_test"] = f"1: {finishers[1]}, 2: {finishers[2]}, 3: {finishers[3]}"
        self.assertEqual(str(finishers[3]), "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def testTournament4(self):  # less test for Andrey
        tournament = Tournament(8, self.Andrey, self.Usain, self.Nick)
        finishers = tournament.start()

        self.all_results["fourth_test"] = f"1: {finishers[1]}, 2: {finishers[2]}, 3: {finishers[3]}"
        self.assertEqual(str(finishers[3]), "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def testTournament5(self):  # bound test for Andrey
        tournament = Tournament(9, self.Nick, self.Andrey, self.Usain)
        finishers = tournament.start()

        self.all_results["fifth_test"] = f"1: {finishers[1]}, 2: {finishers[2]}, 3: {finishers[3]}"
        self.assertEqual(str(finishers[3]), "Ник")

if __name__ == "__main__":
    unittest.main()
