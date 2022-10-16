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



class Car:
    
    def __init__(self, type: str, top_speed: int):
        self.type = type
        self.top_speed = top_speed

    def __str__(self):
        return f'{self.type}:{self.top_speed}'



@pytest.fixture
def car() -> Car:
    return Car(type="SUV", top_speed="120")


def test_fixture(car: Car) -> None:
    print(f'Print {car} from fixture')


@pytest.mark.parametrize(
    "car_type", ["Sports", "Mini-van", "Coupe"],
    ids=['Sports car test', 'Mini-van car test', 'Coupe car test']
)
def test_parametrized(car_type:str) -> None:
    print(f'\nTest with {car_type}')


def raise_error_exception() -> None:
    raise ValueError('Error Exception')

def test_raise_error_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_error_exception()
    assert 'Error Exception' == str(e.value)
