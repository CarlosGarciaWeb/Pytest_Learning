# usually pytest searches for files with the name test in it. This can be configures and modified. Starting with __name__ == "__main__" does not allow pytest to find what to test.
import pytest




def test_our_first_test() -> None:
    assert 1 == 1



@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2

    