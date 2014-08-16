import unittest

import bokeh.plotting as plt
from bokeh.objects import Grid, LinearAxis

class TestPlotting(unittest.TestCase):

    def test_reset_output(self):
        plt._default_document = 10
        plt._default_session = 10
        plt._default_file = 10
        plt._default_notebook = 10
        plt.reset_output()
        self.assertTrue(isinstance(plt._default_document, plt.Document))
        self.assertEqual(plt._default_session, None)
        self.assertEqual(plt._default_file, None)
        self.assertEqual(plt._default_notebook, None)

    def test_figure(self):
        self.assertEqual(plt.curplot(), None)
        plt.figure()
        self.assertEqual(plt.curplot(), None)
        p = plt.circle([1,2,3], [1,2,3])
        self.assertEqual(plt.curplot(), p)
        plt.figure()
        self.assertEqual(plt.curplot(), None)

    def test_xaxis(self):
        plt.figure()
        p = plt.circle([1,2,3], [1,2,3])
        self.assertEqual(len(plt.xaxis()), 1)

        expected = set(plt.xaxis())

        ax = LinearAxis()
        expected.add(ax)
        p.above.append(ax)
        self.assertEqual(set(plt.xaxis()), expected)

        ax2 = LinearAxis()
        expected.add(ax2)
        p.above.append(ax2)
        self.assertEqual(set(plt.xaxis()), expected)

        p.left.append(LinearAxis())
        self.assertEqual(set(plt.xaxis()), expected)

        p.right.append(LinearAxis())
        self.assertEqual(set(plt.xaxis()), expected)

    def test_yaxis(self):
        plt.figure()
        p = plt.circle([1,2,3], [1,2,3])
        self.assertEqual(len(plt.yaxis()), 1)

        expected = set(plt.yaxis())

        ax = LinearAxis()
        expected.add(ax)
        p.right.append(ax)
        self.assertEqual(set(plt.yaxis()), expected)

        ax2 = LinearAxis()
        expected.add(ax2)
        p.right.append(ax2)
        self.assertEqual(set(plt.yaxis()), expected)

        p.above.append(LinearAxis())
        self.assertEqual(set(plt.yaxis()), expected)

        p.below.append(LinearAxis())
        self.assertEqual(set(plt.yaxis()), expected)

    def test_axis(self):
        plt.figure()
        p = plt.circle([1,2,3], [1,2,3])
        self.assertEqual(len(plt.axis()), 2)

        expected = set(plt.axis())

        ax = LinearAxis()
        expected.add(ax)
        p.above.append(ax)
        self.assertEqual(set(plt.axis()), expected)

        ax2 = LinearAxis()
        expected.add(ax2)
        p.below.append(ax2)
        self.assertEqual(set(plt.axis()), expected)

        ax3 = LinearAxis()
        expected.add(ax3)
        p.left.append(ax3)
        self.assertEqual(set(plt.axis()), expected)

        ax4 = LinearAxis()
        expected.add(ax4)
        p.right.append(ax4)
        self.assertEqual(set(plt.axis()), expected)

    def test_xgrid(self):
        plt.figure()
        p = plt.circle([1,2,3], [1,2,3])
        self.assertEqual(len(plt.xgrid()), 1)
        self.assertEqual(plt.xgrid()[0].dimension, 0)

    def test_ygrid(self):
        plt.figure()
        p = plt.circle([1,2,3], [1,2,3])
        self.assertEqual(len(plt.ygrid()), 1)
        self.assertEqual(plt.ygrid()[0].dimension, 1)

    def test_grid(self):
        plt.figure()
        p = plt.circle([1,2,3], [1,2,3])
        self.assertEqual(len(plt.grid()), 2)



