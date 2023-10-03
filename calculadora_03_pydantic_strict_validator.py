from pydantic import validate_call, StrictInt

class PydanticStrictValidator:
    @validate_call
    def soma(self, num1: StrictInt, num2: StrictInt) -> int:
        return num1 + num2