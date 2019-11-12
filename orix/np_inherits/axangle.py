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
from transforms3d.euler import axangle2euler


class AxAngle():
    """
    Class storing rotations in the axis-angle convention. Each row reads
    as [vx,vy,vz,theta], where [vx,vy,vz] is the rotation axis (normalised)
    and theta is the rotation angle in UNITS
    """

    def __init__(self, data):
        self.data = data.astype('float')
        # check the dimensions
        # normalise
        return None

    def _check_data(self):
        """ Checks the data within AxAngle is acceptable, having the correct dimensions,
        acceptable angles and normalised vectors """
        if self.data.shape[1] != 4:
            raise ValueError("Your data is not in the correct shape")
        if np.any(self.data[:, 3] < 0) or np.any(self.data[:, 3] > np.pi):
            raise ValueError("Some of your angles lie outside of the range (0,pi)")
        if not np.allclose(np.linalg.norm(self.data[:, :3], axis=1), 1):
            raise ValueError("You no longer have normalised direction vectors")
        return None

    def remove_large_rotations(self, threshold_angle):
        """

        Parameters
        ----------
        thereshold_angle : float
            angle in radians

        Returns
        -------

        None, this function operates in place
        """
        self._check_data()
        self.data = self.data[self.data[:, 3] < threshold_angle]
        return None

    def to_Euler(self, axis_convention):
        from orix.np_inherits.euler import Euler
        self._check_data()
        stored_euler = np.ones((self.data.shape[0], 3))
        for i, row in enumerate(self.data):
            a_array = axangle2euler(row[:3], row[3], axis_convention)
            for j in [0, 1, 2]:
                stored_euler[i, j] = a_array[j]

        stored_euler = np.rad2deg(stored_euler)
        return Euler(stored_euler, axis_convention)
