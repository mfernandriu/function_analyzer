from function_analyzer.domain.operation import Operation


class Addition(Operation):
    def calculate_partial_result(self, left_operand, right_operand) -> str:
        partial_result = float(left_operand) + float(right_operand)
        return str(partial_result)