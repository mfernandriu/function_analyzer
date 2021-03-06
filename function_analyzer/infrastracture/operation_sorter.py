from function_analyzer.domain.operation.operation import Operation


class OperationSorter:
    @staticmethod
    def sort_by_priority(operations: [Operation]):
        operations = sorted(
            operations, key=lambda x: (x.sign_priority, x.sign_position)
        )
        return operations
