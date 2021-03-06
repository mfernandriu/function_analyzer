from function_analyzer.domain.operand import Operand
from function_analyzer.infrastracture.operand_finder import OperandFinder


class Operation:
    def __init__(
        self, operand_finder: OperandFinder, sign_position: int, sign_priority: int
    ):
        self.operand_finder = operand_finder
        self.sign_position = sign_position
        self.sign_priority = sign_priority
        self.right_operation = None

    def do_operation(self, expression_string: str):
        left_operand = self.operand_finder.find_left_operand(
            expression_string, self.sign_position
        )
        right_operand = self.operand_finder.find_right_operand(
            expression_string, self.sign_position
        )
        partial_result = self.calculate_partial_result(left_operand, right_operand)
        expression_string = Operation.substitute_operation_for_partial_result(
            expression_string, left_operand, right_operand, partial_result
        )
        if self.right_operation is not None:
            post_substitution_shift_length = self.calculate_shift_length(
                left_operand, partial_result, right_operand
            )
            self.right_operation.update_positions_after_shift(
                post_substitution_shift_length
            )
        return expression_string

    def calculate_partial_result(
        self, left_operand: Operand, right_operand: Operand
    ) -> str:
        pass

    @staticmethod
    def calculate_shift_length(left_operand, partial_result, right_operand):
        post_substitution_shift_length = (
            len(left_operand.operand)
            + len(right_operand.operand)
            + 1
            - len(partial_result)
        )
        return post_substitution_shift_length

    @staticmethod
    def substitute_operation_for_partial_result(
        expression_string, left_operand, right_operand, partial_result
    ):
        function_string_left_to_operation = expression_string[: left_operand.position]
        function_string_right_to_operation = expression_string[right_operand.tail :]
        function_string = (
            function_string_left_to_operation
            + partial_result
            + function_string_right_to_operation
        )
        return function_string

    def set_right_operation(self, right_operation):
        self.right_operation = right_operation

    def update_positions_after_shift(self, shift_length):
        self.sign_position -= shift_length
        if self.right_operation:
            self.right_operation.update_positions_after_shift(shift_length)
