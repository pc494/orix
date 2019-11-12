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

from transforms3d.euler import euler2axangle

def convert_axangle_to_correct_range(vector,angle):
    """
    This repo uses axis-angle pairs between (0,pi) - however often wider
    ranges are used, most common are (0,2pi) and (-pi,pi), this function corrects
    for these
    """
    if (angle > 0) and (angle < np.pi): #input in the desired convention
        pass
    elif (angle > -np.pi) and (angle < 0):
        vector = np.multiply(vector,-1)
        angle  = angle * -1
    elif (angle > np.pi) and (angle < 2*np.pi):
        vector = np.multiply(vector,-1)
        angle = 2*np.pi - angle
    else:
        raise ValueError("You have an axis-angle angle outside of acceptable ranges")

    return vector,angle
class Euler():
    """
    Class storing rotations as euler angles.
    Each row reads as [alpha,beta,gamma], where alpha, beta and gamma are rotations
    in degrees in the convention specified by Euler.axis_conventions
    as defined in transforms3d, remember that Euler angles are difficult.
    """
    def __init__(self,data,axis_convention='rzxz'):
        self.data = data.astype('float')
        self.axis_convention = axis_convention
        # check the dimensions
        # check all angles less than 360
        return None

    def _check_data(self):
        """ Checks data within Euler is acceptable, to be used at the start
        of methods """
        if self.data.shape[1] != 3:
            raise ValueError("Your data is not in the correct shape")
        if np.any(self.data[:] > 360):
            raise ValueError("Some of your angles are greater 360")

        return None

    def to_AxAngle(self):
        from orix.np_inherits.axangle import AxAngle
        self._check_data()
        stored_axangle = np.ones((self.data.shape[0],4))
        self.data = np.deg2rad(self.data) #for the transform operation
        for i,row in enumerate(self.data):
            temp_vect, temp_angle = euler2axangle(row[0],row[1],row[2],self.axis_convention)
            if (temp_angle > np.pi) or (temp_angle < 0): #restricting to the range (0,pi)
                temp_vect,temp_angle  = convert_axangle_to_correct_range(temp_vect,temp_angle)
            for j in [0,1,2]:
                stored_axangle[i,j] = temp_vect[j]
            stored_axangle[i,3] = temp_angle #in radians!

        self.data = np.rad2deg(self.data) #leaves our eulers safe and sound
        return AxAngle(stored_axangle)

    def to_Quat(self):
        pass
