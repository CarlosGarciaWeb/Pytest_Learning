# Pytest_Learning



usually pytest searches for files with the name test in it. This can be configures and modified. Starting with __name__ == "__main__" does not allow pytest to find what to test.


Use pytest . to run pytest on the active project location. Remember that the file to test will have to start with the word test, in this case it is test_sample.py, you can also use pytest "filelocation" -v to obtain further details on the test for example being passed, skipped, failed.

You can use the decorator @pytest.mark.skip to skip a specific test. Remember to import pytest first.
