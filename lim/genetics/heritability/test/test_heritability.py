from __future__ import division

from numpy.random import RandomState
from numpy.testing import assert_allclose

from lim.genetics.heritability import bernoulli_estimate
from lim.random.canonical import bernoulli as bernoulli_sampler

from lim.genetics.heritability import binomial_estimate
from lim.random.canonical import binomial as binomial_sampler


def test_heritability_bernoulli_estimate():
    random = RandomState(1)
    N = 50
    X = random.randn(N, N+1)
    y = bernoulli_sampler(0.0, X, random_state=random)
    # assert_allclose(bernoulli_estimate(y, X), 0.627441483331, rtol=1e-5)
    assert_allclose(bernoulli_estimate(y, X), 3.705859167105969e-07, atol=1e-4)


def test_heritability_binomial_estimate():
    random = RandomState(1)
    N = 50
    X = random.randn(N, N+1)
    ntrials = random.randint(1, 100, size=N)
    y = binomial_sampler(ntrials, 0.1, X, random_state=random)
    assert_allclose(binomial_estimate(y, ntrials, X), 0.38072991066,
                    rtol=1e-5)


if __name__ == '__main__':
    __import__('pytest').main([__file__, '-s'])
