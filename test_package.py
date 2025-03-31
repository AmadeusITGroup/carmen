import pytest
from package import square


@pytest.mark.parametrize(
    "x,res",
    [(1, 1), (2, 4), (-1, 1), (0, 0)],
)
def test_square(x: int, res: int) -> None:
    assert square(x) == res
