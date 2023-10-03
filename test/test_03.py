import pytest
from pydantic_core import ValidationError
from calculadora_03_pydantic_strict_validator import PydanticStrictValidator

calculadora = PydanticStrictValidator()

''' Tests (não muda valores de de exemplo 00)'''
class TestClassPydanticStrictValidator:
    def test_soma_inteiros(self):
        assert calculadora.soma(2,3) == 5
        # return 5 <int>

    def test_soma_strings_num(self):
        with pytest.raises(ValidationError) as e_info:
            calculadora.soma("2", "3") == "23"
        assert 'should be a valid integer' in str(e_info.value)
        # return error

    def test_soma_string_int(self):
        with pytest.raises(ValidationError) as e_info:
            calculadora.soma("2", 3)
        assert 'should be a valid integer' in str(e_info.value)
        # return error

    def test_soma_strings(self):
        with pytest.raises(ValidationError) as e_info:
            calculadora.soma("dois", "tres")
        assert 'should be a valid integer' in str(e_info.value)
        # return error