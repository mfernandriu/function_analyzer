from function_analyzer.domain.operation.operation import Operation


class Substraction(Operation):
    def calculate_partial_result(self, left_operand, right_operand):
        partial_result = float(left_operand.operand) - float(right_operand.operand)
        return str(partial_result)
