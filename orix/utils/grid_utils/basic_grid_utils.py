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
from itertools import product

from orix.numpy_inherits.euler import Euler

def create_linearly_spaced_array_in_szxz(resolution):
    """
    Notes
    -----
    We use angular ranges alpha [0,360], beta [0,180] and gamma [0,360] in
    line with Convention 4 described in Reference [1]

    References
    ----------
    [1]  D Rowenhorst et al 2015 Modelling Simul. Mater. Sci. Eng.23 083501
         https://iopscience.iop.org/article/10.1088/0965-0393/23/8/083501/meta
    """
    
    num_steps = 360/resolution
    alpha = np.linspace(0,360,step=num_steps,endpoint=False)
    beta  = np.linspace(0,180,step=num_steps/2,endpoint=False)
    gamma = np.linspace(0,360,step=num_steps,endpoint=False)
    z = np.asarray(list(product(alpha, beta, gamma)))
    return Euler(z,axis_convention='szxz')
