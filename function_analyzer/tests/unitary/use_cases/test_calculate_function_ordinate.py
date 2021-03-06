from function_analyzer.infrastracture.operation_finder import (
    OperationFinder,
)
from function_analyzer.infrastracture.operation_sorter import (
    OperationSorter,
)
from function_analyzer.infrastracture.subexpression_finder.subexpression_finder import (
    SubexpressionFinder,
)
from function_analyzer.use_cases.calculate_function_ordinate import (
    calculate_function_ordinate,
)


def test_calculate_function_ordinate_for_two_addends_addition():
    abscissa = 1
    function_string = "x+1"
    expected_ordinate = 2
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_many_addends_addition():
    abscissa = 1
    function_string = "x+x+x+1"
    expected_ordinate = 4
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_two_operands_substraction():
    abscissa = 1
    function_string = "x-1"
    expected_ordinate = 0
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_many_operands_substraction():
    abscissa = 1
    function_string = "x-x-x-1"
    expected_ordinate = -2
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_two_operands_multiplication():
    abscissa = 2
    function_string = "x*x"
    expected_ordinate = 4
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_three_operands_multiplication_bug():
    abscissa = 2
    function_string = "8.0*2*1"
    expected_ordinate = 16
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_many_operands_multiplication():
    abscissa = 2
    function_string = "x*x*x*x*1"
    expected_ordinate = 16
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_two_operands_division():
    abscissa = 2
    function_string = "x/x"
    expected_ordinate = 1
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_many_operands_division():
    abscissa = 2
    function_string = "x/x/x/x"
    expected_ordinate = 0.25
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_two_operands_exponentiation():
    abscissa = 2
    function_string = "xpx"
    expected_ordinate = 4
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_many_operands_exponentiation():
    abscissa = 2
    function_string = "xpxpxpx"
    expected_ordinate = 256
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_expression_with_multiplication_and_subtraction():
    abscissa = 2
    function_string = "x*x-x"
    expected_ordinate = 2
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_expression_with_one_subexpression():
    abscissa = 2
    function_string = "x*(x-x)"
    expected_ordinate = 0
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_expression_with_many_subexpressions():
    abscissa = 2
    function_string = "x*(x-x)+x*(x+1)"
    expected_ordinate = 6
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_expression_subexpressions_inside_subexpressions():
    abscissa = 2
    function_string = "x*((x-1)*(x+1))"
    expected_ordinate = 6
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_expression_many_subexpressions_inside_subexpressions():
    abscissa = 2
    function_string = "x*((x-1)*(x*(x+1)))"
    expected_ordinate = 12
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def test_calculate_function_ordinate_for_0_valued_abscissa_bug():
    abscissa = 0
    function_string = "x*(x-1)"
    expected_ordinate = 0
    assert_solving_expression_returns_expected_ordinate(
        abscissa, function_string, expected_ordinate
    )


def assert_solving_expression_returns_expected_ordinate(
    abscissa: float, function_string: str, expected_ordinate: float
):
    subexpression_finder = SubexpressionFinder()
    operation_finder = OperationFinder()
    operation_sorter = OperationSorter()
    returned_ordinate = calculate_function_ordinate(
        subexpression_finder,
        operation_finder,
        operation_sorter,
        abscissa,
        function_string,
    )
    assert returned_ordinate == expected_ordinate
