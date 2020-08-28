from function_analyzer.domain.operation.operation import Operation


def test_substitute_operands_and_operation_for_partial_result():
    function_string = '1+2'
    left_operand_position = 0
    right_operand_tail = 3
    partial_result = 3
    returned_function_string = Operation.substitute_operation_for_partial_result(function_string,
                                                                                 left_operand_position,
                                                                                 right_operand_tail,
                                                                                 partial_result)

    expected_function_string = '3'
    assert returned_function_string == expected_function_string