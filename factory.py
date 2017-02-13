
from variable import DdExpression


class XADDFactory:

    pass


class Node:

    def __init__(self,
                 val_func: DdExpression,
                 low_node: 'Node'=None,
                 high_node: 'Node'=None) -> None:
        self.val_func = val_func
        self.low_node = low_node
        self.high_node = high_node
