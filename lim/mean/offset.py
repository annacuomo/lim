from numpy import full
from numpy import ones

from ..func import Learnable
from ..func import Scalar

class OffsetMean(Learnable):
    def __init__(self):
        self._offset = Scalar(1.0)
        Learnable.__init__(self, offset=self._offset)

    @property
    def offset(self):
        return self._offset.value

    @offset.setter
    def offset(self, offset):
        self._offset.value = offset

    def value(self, size):
        return full(size, self.offset)

    def derivative_offset(self, size):
        return ones(size)