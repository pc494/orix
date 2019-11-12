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

import numpy as np

from basic_grid_utils import create_linearly_spaced_array_in_szxz, select_fundemental_zone, reduce_to_fundemental_zone


def get_local_grid(center,max_rotation,resolution):
    """

    Parameters
    ----------
    center : 3 angle tuple
        The orientation that acts as the center of the grid, specified in the
        'rzxz' convention (degrees)

    max_rotation : float
        The largest rotation away from 'center' that should be included in the grid (degrees)

    resolution : float
        The 'resolution' of the grid (degrees)

    Returns
    -------
    """
    raw_grid = create_linearly_spaced_array_in_szxz(resolution)
    # convert to AxAngle
    # Remove the big angles
    # rotate to the center (check this doesn't reduce our volume saving from szxz)
    # convert to rzxz
    return None

def get_fundemental_zone_grid(space_group_number,resolution,center=(0,0,0)):
    """
    Parameters
    ----------

    space_group_number : int


    resolution : float
        The 'resolution' of the grid (degrees)

    center : 3 angle tuple
        The orientation that acts as the center of the grid, specified in the
        'rzxz' convention (degrees)

        Returns
    """
    raw_grid = create_linearly_spaced_array_in_szxz(resolution)
    raw_grid_ax_angle = raw_grid.to_AxAngle()
    fz = select_fundemental_zone(space_group_number)
    fz_grid = reduce_to_fundemental_zone(raw_grid_axangle,fz)
    # rotate to the center
    # convert to rzxz
    return None
