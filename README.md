# Pytest_Learning

Notes to self:

usually pytest searches for files with the name test in it. This can be configures and modified. Starting with __name__ == "__main__" does not allow pytest to find what to test.


Use pytest . to run pytest on the active project location. Remember that the file to test will have to start with the word test, in this case it is test_sample.py, you can also use pytest "filelocation" -v to obtain further details on the test for example being passed, skipped, failed.

You can use the decorator @pytest.mark.skip to skip a specific test. Remember to import pytest first.


Conditional Skip is an if decorator mark with @pytest.mark.skipif(x, reason="Skipped because x") being x anything that results into a boolean to look out for, if true it would be skipped and the reason printing x because we told it so.

XFAIL -> pytest out of the box function. It is basically a test that is not obligatory to have a passing grade. if fails it denotes an xfail and if passes it denotes an xpassed


Pytest allows to create marks. If you use a decorator mark that is not built in to pytest it will still test but it will provide a warning for you to declare what that mark does.

The pytest configuration in order to create the mark it in pytest.ini file


However, to ignore these warnings you can use -p no:warnings
Now in the other hand if you want to test particular mark tag you can use -m "marktaghere", the end result will tell you which tests from that mark skipped, failed or passed as well as the tests in your file that were not selected because they did not include the tag selected. i.e "pytest . -m skip" will only test 

@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2

You'd think it would test skipif as well but it does as it does not select marks on a contain mark condition it will search for the exact mark you type.






