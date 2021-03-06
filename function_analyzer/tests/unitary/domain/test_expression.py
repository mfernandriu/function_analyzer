from unittest.mock import Mock

from function_analyzer.domain.expression import Expression


class OperationFake:
    def do_operation(self, expression_string):
        return "4"

    def set_right_operation(self, operation):
        pass


class OperationFinderMock:
    def find_operations(self, expression_string):
        operation = OperationFake()
        return [operation, operation, operation]


class OperationSorterMock:
    def sort_by_priority(self, operations):
        return operations


def test_solve_for_abscissa():
    subexpression_finder = Mock()
    subexpression_finder.find_subexpressions = Mock(return_value=[])
    operation_finder = OperationFinderMock()
    operation_sorter = OperationSorterMock()
    expression_string = "x+x+x+x"
    expression = Expression(
        subexpression_finder, operation_finder, operation_sorter, expression_string
    )
    abscissa = 1
    returned_solved_expression = expression.solve_for_abscissa(abscissa)
    expected_solved_expression = 4
    assert returned_solved_expression == expected_solved_expression


def test_substitute_x_for_abscissa_substitutes_many_xs():
    abscissa = 1
    expression_string = "x+x+x+x"
    expression = Expression(None, None, None, expression_string)
    expression.substitute_x_for_abscissa(abscissa)
    returned_function_string = expression.expression_string
    expected_function_string = "1+1+1+1"
    assert returned_function_string == expected_function_string
