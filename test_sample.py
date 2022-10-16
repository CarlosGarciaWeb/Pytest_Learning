# usually pytest searches for files with the name test in it. This can be configures and modified. Starting with __name__ == "__main__" does not allow pytest to find what to test.
import pytest




def test_our_first_test() -> None:
    assert 1 == 1



@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2



@pytest.mark.skipif(0 > 1, reason="Skipped because 4 > 1")
def test_should_be_skipped_if() -> None:
    assert 1 == 2


@pytest.mark.xfail
def test_does_not_matter_if_fails() -> None:
    assert 1 == 2


@pytest.mark.slow
def test_with_custom_mark() -> None:
    assert 1 == 1