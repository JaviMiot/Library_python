import pytest

from basic import sum_two_numbers, f


def test_mytest(tmp_path):
    with pytest.raises(SystemExit):
        f()


def test_needsfiles(tmp_path):
    print(f'temporaly path: {tmp_path}')
    assert 0


class TestSum:
    def test_positive_number(self):
        assert sum_two_numbers(1, 1) == 2
        assert sum_two_numbers(3, 1) == 4
        assert sum_two_numbers(4, 1) == 5

    def test_negative_numbers(self):
        assert sum_two_numbers(-1, -1) == -2
        assert sum_two_numbers(-3, -1) == -4
        assert sum_two_numbers(-4, -1) == 9, "it's not a negative value"
