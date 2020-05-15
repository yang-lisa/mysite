import pytest
from DailyTest.data.ParasYaml import ParseYaml
from DailyTest.Calculator import Calculator


class TestCal:
    pyaml = ParseYaml()
    data = pyaml.parse_yaml()

    def setup(self):
        self.calc = Calculator()

    @pytest.mark.parametrize('a,b,expectresult', data['add'])
    def test_cal_add(self, a, b, expectresult):
        print('start add testing ...')
        result = self.calc.add(a, b)
        assert result == expectresult

    @pytest.mark.parametrize('a,b,expectresult', data['minus'])
    def test_cal_minus(self, a, b, expectresult):
        print('start add testing ...')
        result = self.calc.minus(a, b)
        assert result == expectresult

    @pytest.mark.parametrize('a,b,expectresult', data['multiplus'])
    def test_cal_multiplus(self, a, b, expectresult):
        print('start div testing ...')
        result = self.calc.multip(a, b)
        assert result == expectresult

    @pytest.mark.parametrize('a,b,expectresult', data['div'])
    def test_cal_div(self, a, b, expectresult):
        print('start div testing ...')
        result = self.calc.div(a, b)
        assert expectresult == result


if __name__ == "__main__":
    pytest.main(['-vs', 'CalTest.py'])
