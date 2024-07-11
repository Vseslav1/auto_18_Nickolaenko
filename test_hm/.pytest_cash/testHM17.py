import pytest

from hm5 import generate_squares
from pytest import mark, fixture
from hm5 import get_longest_word
from hm6 import func_square
from hm6 import output_numbers


class TestHm5Exercise3():
    @pytest.mark.Hm5
    def test_1(self):
        assert generate_squares(1, 2, 3) == [1, 4, 9]

    @pytest.mark.Hm5
    def test_2(self):
        assert generate_squares(-1, -2, -3) == [1, 4, 9]

    @pytest.mark.Hm5
    def test_3(self):
        assert generate_squares(0) == [0]


    @pytest.mark.parametrize('argument,expected', [('1' '2' '3', 'Error')])
    @pytest.mark.Hm5
    def test_4(self, argument, expected):
        assert generate_squares(argument) == expected

    @pytest.mark.Hm5
    @pytest.mark.xfail
    def test_5(self):
        assert generate_squares(False) == 'ERR'


    @pytest.mark.Hm5
    def test_6(self):
        assert (generate_squares(100000000000000000000000000000000) ==
                [10000000000000000000000000000000000000000000000000000000000000000])


    @pytest.mark.Hm5
    def test_7(self):
        assert generate_squares(1.34, 2.55, 4.55) == 'Error'


    @pytest.mark.Hm5
    def test_8(self):
        assert generate_squares(1, 4, 6, 9, 100, 500, 1.22, 55.01111, '1', '4') == "Error"


class TestHm5Exercise4():
    @pytest.mark.parametrize('argument,expected', [('Hello my name is Vseslav , I am from Belarus', 'Vseslav'),
                                                   (' ', 'Error'),
                                                   (True, 'Error'),
                                                   ('1 2 3 4', '1')])


    def test_1_1(self, argument, expected):
        assert get_longest_word(argument) == expected


    @pytest.mark.Hm5
    def test_1_2(self):
        assert get_longest_word('Hello my name is Vseslav , I am from Belarus Vitebsk') == 'Vseslav', 'Vitebsk'


    @pytest.mark.Hm5
    def test_1_3(self):
        assert get_longest_word(1, 2, 3, 4) == 'ERR'






class TestHm6Exercise1():
    @pytest.mark.improved_code
    @pytest.mark.hm6
    def test1(self):
        assert output_numbers(1, 2) == 'ERR'


    @pytest.mark.improved_code
    @pytest.mark.hm6
    def test2(self):
        assert output_numbers('1', '2', '3', '4', '5') == (1, 2, 4, 5)


    @pytest.mark.improved_code
    @pytest.mark.hm6
    def test3(self):
        assert output_numbers('1', '2', '3') == 'ERR'


    @pytest.mark.improved_code
    @pytest.mark.hm6
    def test4(self):
        assert output_numbers(' ') == 'ERR'


    @pytest.mark.improved_code
    @pytest.mark.hm6
    def test5(self):
        assert output_numbers(1, 2, 3, 4) == (1, 2, 3, 4)


    @pytest.mark.improved_code
    @pytest.mark.hm6
    def test6(self):
        assert output_numbers(1, 2, 3) == 'ERR'


    @pytest.mark.improved_code
    @pytest.mark.hm6
    def test6(self):
        assert output_numbers(False) == 'ERR'

    @pytest.mark.hm6
    def test7(self):
        assert output_numbers('SRTOKI STROKI STROKI') == 'ERR'


@pytest.fixture
def file_data():
    with open('vesh.txt', 'r') as file:
        yield file.read()


class TestHm6Exercise3():
    @pytest.mark.hm6
    def test_error1(self, file_data):
        with open('vesh.txt', 'w') as file:
            file.write('Vseslav')
        assert func_square() == 'ERROR'

    @pytest.mark.hm6
    def test_successful(self, file_data):
        with open('vesh.txt', 'w') as file:
            file.write('1.0 2.0 3.0')
        assert func_square() == '1.0 4.0 9.0'

    @pytest.mark.hm6
    def test_negative_number(self, file_data):
        with open('vesh.txt', 'w') as file:
            file.write('-1 -2 -3 -4')
        assert func_square() == '1.0 4.0 9.0 16.0'

    @pytest.mark.hm6
    def test_empty_value(self, file_data):
        with open('vesh.txt', 'w') as file:
            file.write(' ')
        assert func_square() == ''

    @pytest.mark.hm6
    def test_zero(self, file_data):
        with open('vesh.txt', 'w') as file:
            file.write('0')
        assert func_square() == '0.0'

    @pytest.mark.hm6
    def test_large_values(self, file_data):
        with open('vesh.txt', 'w') as file:
            file.write('100000000.1000000000000 200000.2000000000000')
        assert func_square() == '1.0000000019999998e+16 40000080000.04'

    @pytest.mark.hm6
    @pytest.mark.xfail
    def test_bool_value(self, file_data):
        with open('vesh.txt', 'w') as file:
            file.write(False)
        assert func_square() == TypeError
