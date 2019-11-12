# -*- coding: utf-8 -*-
# Copyright 2018-2019 The pyXem developers
#
# This file is part of orix.
#
# orix is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# orix is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with orix.  If not, see <http://www.gnu.org/licenses/>.

import pytest
import numpy as np

from orix.np_inherits.axangle import AxAngle
from orix.np_inherits.euler import Euler

class TestAxAngle:
    def test_good_array__init__(self):
        good_array = np.asarray([1,0,0,1])
        assert isinstance(AxAngle(good_array),AxAngle)

class TestEuler:
    def test_good_array__init__(self):
        good_array = np.asarray([1,0,0])
        assert isinstance(Euler(good_array),Euler)
