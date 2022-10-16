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


Pytest also allows for a smart deselection of mark tests. If you want to run anything that is now skip then you can denote -m "not skip"


Pytest fixture is basically a function that the function might be used before or after test function. It can return whatever we want and print what we want from that particular function. In this case we are using the fixture to create a Car object from the declared class in line 35. It will have a car.type of "SUV" and a car.top_speed of 120 (no unit specified, I'm just trying to make myself learn and understand fixtures). Now in order to also print the return of the test function fixture you must denote -s. ie. pytest . -s

Pytest parametrize, means iterating through different imports to do tests.
@pytest.mark.parametrize(
    "car_type", ["Sports", "Mini-van", "Coupe"],
)
def test_parametrized(car_type) -> None:
    print(f'\nTest with {car_type}')

I sort of see it like a for loop of an item list where in the above code, the item from the item list will be iterated to be tested. Where the first parameter is the name you are giving to the list of values to be tested, this will allow pytest to recognize and look for the name of the list of values to then iterate through that particular's value list.

In other words, in the above code, test will look for the list of values named car_type and then iterate through it and test each value. 


 ----   Result of pytest . -v -p no:warnings -s ----------------
collected 9 items                                                                                                                                                                                                           

test_sample.py::test_our_first_test PASSED
test_sample.py::test_should_be_skipped SKIPPED (unconditional skip)
test_sample.py::test_should_be_skipped_if FAILED
test_sample.py::test_does_not_matter_if_fails XFAIL
test_sample.py::test_with_custom_mark PASSED
test_sample.py::test_fixture Print SUV:120 from fixture
PASSED
test_sample.py::test_parametrized[Sports]
Test with Sports
PASSED
test_sample.py::test_parametrized[Mini-van]
Test with Mini-van
PASSED
test_sample.py::test_parametrized[Coupe]
Test with Coupe
PASSED
            ----------------------------------------


You can further customize the parametrized result by including another parameter in the decorator labeled ids like the example below: 

@pytest.mark.parametrize(
    "car_type", ["Sports", "Mini-van", "Coupe"],
    ids=['Sports car test', 'Mini-van car test', 'Coupe car test']
)
def test_parametrized(car_type:str) -> None:
    print(f'\nTest with {car_type}')

 ----   Result of pytest . -v -p no:warnings -s ----------------
collected 9 items                                                                                                                                                                                                           

test_sample.py::test_our_first_test PASSED
test_sample.py::test_should_be_skipped SKIPPED (unconditional skip)
test_sample.py::test_should_be_skipped_if FAILED
test_sample.py::test_does_not_matter_if_fails XFAIL
test_sample.py::test_with_custom_mark PASSED
test_sample.py::test_fixture Print SUV:120 from fixture
PASSED
test_sample.py::test_parametrized[Sports]
Test with Sports
PASSED
test_sample.py::test_parametrized[Mini-van]
Test with Mini-van
PASSED
test_sample.py::test_parametrized[Coupe]
Test with Coupe
PASSED
            ----------------------------------------
collected 9 items                                                                                                                                                                                                           

test_sample.py::test_our_first_test PASSED
test_sample.py::test_should_be_skipped SKIPPED (unconditional skip)
test_sample.py::test_should_be_skipped_if FAILED
test_sample.py::test_does_not_matter_if_fails XFAIL
test_sample.py::test_with_custom_mark PASSED
test_sample.py::test_fixture Print SUV:120 from fixture
PASSED
test_sample.py::test_parametrized[Sports car test]
Test with Sports
PASSED
test_sample.py::test_parametrized[Mini-van car test]
Test with Mini-van
PASSED
test_sample.py::test_parametrized[Coupe car test]
Test with Coupe
PASSED

======================================================================================================== FAILURES ========================================================================================================= 
________________________________________________________________________________________________ test_should_be_skipped_if ________________________________________________________________________________________________ 

    @pytest.mark.skipif(0 > 1, reason="Skipped because 4 > 1")
    def test_should_be_skipped_if() -> None:
>       assert 1 == 2
E       assert 1 == 2

test_sample.py:21: AssertionError
================================================================================================= short test summary info ================================================================================================= 
FAILED test_sample.py::test_should_be_skipped_if - assert 1 == 2
==================================================================================== 1 failed, 6 passed, 1 skipped, 1 xfailed in 0.06s ==================================================================================== 


Testing for value errors can be done by functions that raise a defined ValueError.

Let's define the function that raises the error.

def raise_error_exception() -> None:
    raise ValueError('Error Exception')

Then when testing with pytest, you can directly call inside a function to test the following pytest function:

    with pytest.raises(ValueError) as e:
        raise_error_exception()

The above pytest.raises calls the function with ValueError as e which will then be evaluated to the result of the error function call and the specific error value desired, it will look like the below:

def raise_error_exception() -> None:
    raise ValueError('Error Exception')

def test_raise_error_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_error_exception()
    assert 'Error Exception' == str(e.value)

