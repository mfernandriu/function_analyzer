from function_analyzer.domain.operation.operation import Operation


class Division(Operation):
    def calculate_partial_result(self, left_operand, right_operand) -> str:
        partial_result = float(left_operand.operand) / float(right_operand.operand)
        return str(partial_result)
