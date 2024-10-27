import unittest
import test_mod_12_2 as test1

caseTS = unittest.TestSuite()

caseTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test1.TournamentTest))
caseTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test1.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(caseTS)