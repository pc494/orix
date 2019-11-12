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
    @pytest.fixture()
    def good_array(self):
        return np.asarray([[1,0,0,1],
                             [0,1,0,1.1]])

    def test_good_array__init__(self,good_array):
        assert isinstance(AxAngle(good_array),AxAngle)

    def test_remove_large_rotations(self,good_array):
        axang = AxAngle(good_array)
        axang.remove_large_rotations(1.05) #removes 1 rotations
        assert axang.data.shape == (1,4)

    @pytest.mark.xfail(raises = ValueError, strict=True)
    class TestCorruptingData:
        @pytest.fixture()
        def axang(self,good_array):
            return AxAngle(good_array)

        def test_bad_shape(self,axang):
            axang.data = axang.data[:,:2]
            axang._check_data()

        def test_dumb_angle(self,axang):
            axang.data[0,3] = -0.5
            axang._check_data()

        def test_denormalised(self,axang):
            axang.data[:,0] = 3
            axang._check_data()

class TestEuler:
    @pytest.fixture()
    def good_array(self):
        return np.asarray([[32,80,21],
                           [40,10,11]])
    def test_good_array__init__(self,good_array):
        assert isinstance(Euler(good_array),Euler)

    def test_toAxangle(self,good_array):
        """ Conventions are grim, so only test the code elements """
        axang = Euler(good_array,axis_convention='szxz').to_AxAngle()
        assert isinstance(axang,AxAngle)
        axang._check_data()

    @pytest.mark.xfail(raises = ValueError, strict=True)
    class TestCorruptingData:
        @pytest.fixture()
        def euler(self,good_array):
            return Euler(good_array)

        def test_bad_shape(self,euler):
            euler.data = euler.data[:,:2]
            euler._check_data()

        def test_dumb_angle(self,euler):
            euler.data[0,0] = 700
            euler._check_data()

def test_interconversion_euler_axangle():
    """
    This function checks (with random numbers) that .to_Axangle() and .to_Euler()
    go back and forth correctly
    """
    axes = np.random.random_sample((1000,3))
    axes = np.divide(axes,np.linalg.norm(axes,axis=1).reshape(1000,1))
    assert np.allclose(np.linalg.norm(axes,axis=1),1) #check for input normalisation
    angles = np.multiply(np.random.random_sample((1000,1)),np.pi)
    axangle   = AxAngle(np.concatenate((axes,angles),axis=1))
    transform = AxAngle(np.concatenate((axes,angles),axis=1))
    e = transform.to_Euler(axis_convention='szxz')
    transform_back = e.to_AxAngle()
    assert np.allclose(transform_back.data,axangle.data)
