import pytest
from pydantic_core import ValidationError
from calculadora_02_pydantic_validator import PydanticValidator

calculadora = PydanticValidator()

''' Tests (não muda valores de de exemplo 00)'''
class TestClassPydanticValidator:
    def test_soma_inteiros(self):
        assert calculadora.soma(2,3) == 5
        # return 5 <int>

    def test_soma_strings_num(self):
        assert calculadora.soma("2", "3") == 5
        # return 5 <int>

    def test_soma_string_int(self):
        assert calculadora.soma("2", 3) == 5
        # return 5 <int>

    def test_soma_strings(self):
        with pytest.raises(ValidationError) as e_info:
            calculadora.soma("dois", "tres")
        assert 'should be a valid integer' in str(e_info.value)
        # return error