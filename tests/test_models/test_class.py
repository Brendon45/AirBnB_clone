#!/usr/bin/python3
"""
Test class modules for testing documentations
"""
import pep8
import inspect

class TestClassDocumentation():
    """
    Class for testing multiple classes.
    """

    def __init__(self, tests, _class):
        """
        Initialize the TestClassDocumentation instance.
        """
        self.tests = tests
        self.name = _class

        self.functions = inspect.getmembers(self.name, inspect.isfunction)

    def pep8(self, files):
        """
        Test the PEP 8 compliance of the specified files
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(files)
        self.tests.assertEqual(result.total_errors, 0,
                                'Found code style errors (and warnings)."')

    def check_documentation(self):
        """Documentation of the methods and classes
        """
        # Test methods
        with self.tests.subTest(msg='Testing methods'):
            for f in self.functions:
                with self.tests.subTest(msg='Documentation method {}'
                                        .format(f[0])):
                    doc = f[1].__doc__
                    self.tests.assertGreaterEqual(len(doc), 1)

        with self.tests.subTest(msg='Testing class'):
            # Retrieve module docstring
            doc = self.name.__doc__
            self.tests.assertGreaterEqual(len(doc), 1)

if __name__ == '__main__':
    unittest.main()
