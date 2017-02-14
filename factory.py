from typing import Union
from variable import DdExpression


class NodeManager:

    def __init__(self):
        self.node_cache = {}

    def new_node(self, node_expr: DdExpression, low_expr: DdExpression = None, high_expr: DdExpression = None):
        return self.node_cache.setdefault((node_expr,
                                           low_expr if low_expr is not None else None,
                                           high_expr if high_expr is not None else None),
                                          Node(node_expr))


class XADDFactory:

    def __init__(self):
        pass


class Node:

    def __init__(self,
                 val_func: Union[DdExpression,float,int],
                 low_node: 'Node'=None,
                 high_node: 'Node'=None) -> None:
        val_func = val_func if isinstance(val_func, DdExpression) else DdExpression(val_func)
        self.val_func = val_func
        self.low_node = low_node
        self.high_node = high_node
