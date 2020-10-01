from function_analyzer.domain.sign import Sign
from function_analyzer.infrastracture.operand_finder.operand_finder import OperandFinder
from function_analyzer.infrastracture.operation.addition import Addition
from function_analyzer.infrastracture.operation.substraction import Substraction
from function_analyzer.infrastracture.operation.multiplication import Multiplication


class OperationFactory:
    @staticmethod
    def create(sign: str, sign_position: int):
        operand_finder = OperandFinder()
        if sign == Sign.MULTIPLICATION_CHARACTER:
            return Multiplication(operand_finder, sign_position, Sign.MULTIPLICATION_PRIORITY)
        if sign == Sign.SUBSTRACTION_CHARACTER:
            return Substraction(operand_finder, sign_position, Sign.SUBSTRACTION_PRIORITY)
        elif sign == Sign.ADDITION_CHARACTER:
            return Addition(operand_finder, sign_position, Sign.ADDITION_PRIORITY)
        else:
            raise NotImplementedError
