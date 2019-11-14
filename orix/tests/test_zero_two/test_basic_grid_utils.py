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
    assert grid.data.shape == (442368,3)

def test_preservation_of_reduced_rotation_space():
    """ Pyxem's template matching implementation (from probably 0.11.0 onwards)
        has a major speed up based on reducing the data size due to a [a,b,c]
        and [a,b,c+d] being similar in the 'szxz' convention. This test confirms
        that that data reduction remains even after transfers between representations
    """
    grid = create_linearly_spaced_array_in_szxz(resolution=7)
    count_of_specials = np.unique(grid.data[:,:2],axis=0).shape[0]
    grid_axangle = grid.to_AxAngle()
    grid_back_forth = grid_axangle.to_Euler('szxz')
    count_of_specials_2 = np.unique(grid_back_forth.data.round(decimals=2)[:,:2],axis=0).shape[0]
    assert np.allclose(grid.data.shape,grid_back_forth.data.shape)
    assert np.allclose(count_of_specials,count_of_specials_2)

def test_select_fundemental_zone():
    """ Makes sure all the ints from 1 to 230 give answers """
    for _space_group in np.arange(1,231):
        fz_string = select_fundemental_zone(_space_group)
        assert fz_string in ['1','2','222','3','32','6','622','4','422','432','23']
