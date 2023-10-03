import pytest
from calculadora_00_notypehint import NoTypeHint

calculadora = NoTypeHint()

''' Tests '''
class TestClassNoTypeHint:
    def test_soma_inteiros(self):
        assert calculadora.soma(2,3) == 5
        # return 5 <int>

    def test_soma_strings_num(self):
        assert calculadora.soma("2", "3") == "23"
        # return 23 <str>

    def test_soma_string_int(self):
        with pytest.raises(TypeError) as e_info:
            calculadora.soma("2", 3)
        assert 'can only concatenate str (not "int") to str' == str(e_info.value.args[0])
        # return error

    def test_soma_strings(self):
        assert calculadora.soma("dois", "tres") == "doistres"
        # doistres <str>
