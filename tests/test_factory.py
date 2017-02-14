from unittest import TestCase
from factory import XADDFactory, NodeManager, Node
from variable import DdExpression


class TestXADDFactory(TestCase):

    def test_build_tree(self):
        x1 = DdExpression('x1')
        x2 = DdExpression('x2')
        k = DdExpression('k')
        V = {x1 + k: x2}
        factory = XADDFactory()
        #tree = factory.build_tree(V)

    def test_new_node(self):
        x1 = DdExpression('x1')
        x2 = DdExpression('x2')
        n = Node(x1 + x2)
        self.assertEqual(n.val_func.expression_repr, '(x1)+(x2)')

    def test_node_manager(self):
        x1 = DdExpression('x1')
        x2 = DdExpression('x2')
        c  = DdExpression(5)
        nm = NodeManager()
        n1 = nm.new_node(c)
        n2 = nm.new_node(x1)
        n3 = nm.new_node(x2)
        self.assertEqual(n1.val_func.expression_repr, 5)
        self.assertEqual(n2.val_func.expression_repr, 'x1')
        self.assertEqual(n3.val_func.expression_repr, 'x2')
        self.assertEqual(len(nm.node_cache), 3)
        n4 = nm.new_node(x1+x2)
        self.assertEqual(n4.val_func.expression_repr, '(x1)+(x2)')
        self.assertEqual(len(nm.node_cache), 4)
        n5 = nm.new_node(x1+x2, c, x1)
        self.assertEqual(n5.val_func.expression_repr, '(x1)+(x2)')
        self.assertEqual(len(nm.node_cache), 5)
        n6 = nm.new_node(x1+x2, c, x1)
        self.assertEqual(len(nm.node_cache), 5)
        n7 = nm.new_node(x1+x2, c, x2)
        self.assertEqual(len(nm.node_cache), 6)



