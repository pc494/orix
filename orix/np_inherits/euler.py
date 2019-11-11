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

import numpy
import transforms3d

class Euler(np.array):
    """
    Class storing rotations as euler angles.
    Each row reads as [alpha,beta,gamma], where alpha, beta and gamma are rotations
    in degrees in the convention specified by Euler.axis_conventions
    as defined in transforms3d, remember that Euler angles are difficult.
    """
    def __init__(self,data,axis_convention='rzxz'):
        # check the dimensions
        # check all angles less than 360
        # axis_convention
        return None

    def _check_data(self):
        """ Checks data within Euler is acceptable, to be used at the start
        of methods """
        # check dimensions
        # check angles are all less than 360
        return None

    def to_AxAngle(self):
        pass

    def to_Quat(self):
        pass
