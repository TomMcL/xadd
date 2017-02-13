import operator
from typing import Union, Callable


class DdExpression:
    def __init__(self, dd_id: Union[tuple, str], expression_chain: Callable = None) -> None:
        self.dd_id = dd_id if isinstance(dd_id, tuple) else (dd_id,)
        self.expression_chain = expression_chain if expression_chain else \
            lambda variable_values: variable_values.get(self.dd_id[0])

    def evaluate(self, variable_values: dict) -> Union[bool, float, int]:
        return self.expression_chain(variable_values)

    def _apply_op(self, other: Union['DdExpression', float, int], op: Callable) -> Union['DdExpression', bool]:
        if not isinstance(other, (DdExpression, float, int)):
            raise NotImplementedError('Addition only applicable between two DdExpression types, floats or ints')
        if not isinstance(other, DdExpression):
            other_node = DdExpression((), lambda variable_values: other)
        else:
            other_node = other
        return DdExpression(dd_id=tuple(set(self.dd_id).union(set(other_node.dd_id))),
                            expression_chain=lambda variable_values: op(self.evaluate(variable_values),
                                                                        other_node.evaluate(variable_values)))

    def __add__(self, other: Union['DdExpression', float, int]) -> 'DdExpression':
        return self._apply_op(other, operator.add)

    def __sub__(self, other: Union['DdExpression', float, int]) -> 'DdExpression':
        return self._apply_op(other, operator.sub)

    def __mul__(self, other: Union['DdExpression', float, int]) -> 'DdExpression':
        return self._apply_op(other, operator.mul)

    def __truediv__(self, other: Union['DdExpression', float, int]) -> 'DdExpression':
        return self._apply_op(other, operator.truediv)

    def __radd__(self, other: Union['DdExpression', float, int]) -> 'DdExpression':
        return self.__add__(other)

    def __rmul__(self, other: Union['DdExpression', float, int]) -> 'DdExpression':
        return self.__mul__(other)

    def __rsub__(self, other: Union['DdExpression', float, int]) -> 'DdExpression':
        return -1 * self.__sub__(other)

    # TODO Make rtruediv work
    def __rtruediv__(self, other: Union['DdExpression', float, int]) -> 'DdExpression':
        result = self.__truediv__(other)
        return result

    def __lt__(self, other: Union['DdExpression', float, int]) -> bool:
        return self._apply_op(other, operator.lt)

    def __gt__(self, other: Union['DdExpression', float, int]) -> bool:
        return self._apply_op(other, operator.gt)

    def __eq__(self, other: Union['DdExpression', float, int]) -> bool:
        return self._apply_op(other, operator.eq)

    def __ne__(self, other: Union['DdExpression', float, int]) -> bool:
        return not self.__eq__(other)

    def __le__(self, other: Union['DdExpression', float, int]) -> bool:
        return self._apply_op(other, operator.le)

    def __ge__(self, other: Union['DdExpression', float, int]) -> bool:
        return self._apply_op(other, operator.ge)
