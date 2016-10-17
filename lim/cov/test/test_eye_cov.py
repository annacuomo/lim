from __future__ import division

import numpy.testing as npt

from numpy.random import RandomState
from numpy import exp

from optimix import check_grad

from lim.cov import EyeCov
from lim.util.fruits import Oranges
from lim.util.fruits import Apples


def test_eye_value():
    cov = EyeCov()
    cov.scale = 2.1
    o = Oranges(None)
    npt.assert_almost_equal(2.1, cov.value(o, o))
#
#
# def test_eye_gradient_1():
#     cov = EyeCov()
#     cov.scale = 2.1
#     a = Apples(None)
#     cov.set_data((a, a))
#
#     def func(x):
#         cov.scale = exp(x[0])
#         return as_data_function(cov).value()
#
#     def grad(x):
#         cov.scale = exp(x[0])
#         return as_data_function(cov).gradient()
#
#     npt.assert_almost_equal(check_grad(func, grad, [0.1]), 0)
#
#
# def test_eye_gradient_2():
#     cov = EyeCov()
#     cov.scale = 2.1
#     a = Apples(5)
#     cov.set_data((a, a))
#
#     def func(x):
#         cov.scale = exp(x[0])
#         return as_data_function(cov).value()
#
#     def grad(x):
#         cov.scale = exp(x[0])
#         return as_data_function(cov).gradient()
#
#     npt.assert_almost_equal(check_grad(func, grad, [0.1]), 0)
#
#
# def test_eye_gradient_3():
#     cov = EyeCov()
#     cov.scale = 2.1
#     a = Apples(5)
#     o = Oranges(4)
#     cov.set_data((a, o))
#
#     def func(x):
#         cov.scale = exp(x[0])
#         return as_data_function(cov).value()
#
#     def grad(x):
#         cov.scale = exp(x[0])
#         return as_data_function(cov).gradient()
#
#     npt.assert_almost_equal(check_grad(func, grad, [0.1]), 0)
#

if __name__ == '__main__':
    __import__('pytest').main([__file__, '-s'])