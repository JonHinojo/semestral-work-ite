"""runs all the tests of the project"""

import os
import unittest

if __name__ == "__main__":
    project_dir = os.path.dirname(__file__)
    tests_dir = os.path.join(project_dir, "tests")
    suite = unittest.defaultTestLoader.discover(tests_dir, top_level_dir=project_dir)
    unittest.TextTestRunner(verbosity=2).run(suite)