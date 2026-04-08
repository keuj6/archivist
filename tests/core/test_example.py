from archivist.core.example import add


def test_should_return_sum_when_given_two_ints() -> None:
    assert add(2, 3) == 5


def test_should_return_zero_when_given_zeros() -> None:
    assert add(0, 0) == 0
