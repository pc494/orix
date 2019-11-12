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

from orix.np_inherits.euler import Euler
from orix.utils.grid_utils.basic_grid_utils import create_linearly_spaced_array_in_szxz,select_fundemental_zone,reduce_to_fundemental_zone


def test_linearly_spaced_array_in_szxz():
    """ From definition, a resolution of 3.75 will give us:
        Two sides of length = 96
        One side of length  = 48
        And thus a total of 96 * 96 * 48 = 442368 points
    """
    grid = create_linearly_spaced_array_in_szxz(resolution=3.75)
    assert isinstance(grid,Euler)
    assert grid.axis_convention == 'szxz'
    assert grid.data.shape == (442368,3) #is this the wrong way around?
