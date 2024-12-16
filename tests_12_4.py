import logging
from tests_12_1 import *

logging.basicConfig(level=logging.INFO, filemode='w',filename="runner_tests.log", format="[%(asctime)s] {%("
                                                                                         "pathname)s:%(lineno)d} %("
                                                                                         "levelname)s - %(message)s")

if __name__ == "__main__":
    unittest.main()
