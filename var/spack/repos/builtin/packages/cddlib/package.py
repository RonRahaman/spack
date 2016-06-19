##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################

from spack import *

class Cddlib(Package):
    """The C-library  cddlib is a C implementation of the Double Description 
    Method of Motzkin et al. for generating all vertices (i.e. extreme points)
    and extreme rays of a general convex polyhedron in R^d given by a system 
    of linear inequalities"""
    homepage = "https://www.inf.ethz.ch/personal/fukudak/cdd_home/"
    url      = "ftp://ftp.ifor.math.ethz.ch/pub/fukuda/cdd/cddlib-094h.tar.gz"

    version('094h', '1467d270860bbcb26d3ebae424690e7c')

    # Note: It should be possible to build cddlib also without gmp

    depends_on("gmp")
    depends_on("libtool")

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)
        make()
        make("install")
