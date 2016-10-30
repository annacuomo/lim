from numpy.testing import assert_allclose

from lim.link import ProbitLink


def test_probit_link():
    lik = ProbitLink()
    assert_allclose(lik.value(lik.inv(3.2)), 3.2)