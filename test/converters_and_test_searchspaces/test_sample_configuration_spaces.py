# Copyright (c) 2014-2016, ConfigSpace developers
# Matthias Feurer
# Katharina Eggensperger
# and others (see commit history).
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the <organization> nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import unittest

import ConfigSpace
import ConfigSpace.util
import ConfigSpace.io.pcs as pcs_parser


class ExampleSearchSpacesTest(unittest.TestCase):
    pass


def generate(configuration_space_path):
    def run_test(self):
        with open(configuration_space_path) as fh:
            cs = pcs_parser.read(fh)

        # Sample a little bit
        for i in range(10):
            print(i)
            cs.seed(i)
            configurations = cs.sample_configuration(size=5)
            for j, c in enumerate(configurations):
                print(j)
                c.is_valid_configuration()
                neighborhood = ConfigSpace.util.get_one_exchange_neighbourhood(
                    c, seed=i)

                for shuffle, n in enumerate(neighborhood):
                    n.is_valid_configuration()
                    if shuffle == 10:
                        break
    return run_test


this_file = os.path.abspath(__file__)
this_directory = os.path.dirname(this_file)
configuration_space_path = os.path.join(this_directory,
                                        "..", "test_searchspaces")
configuration_space_path = os.path.abspath(configuration_space_path)
pcs_files = os.listdir(configuration_space_path)

for pcs_file in pcs_files:
    if '.pcs' in pcs_file:
        full_path = os.path.join(configuration_space_path, pcs_file)
        setattr(ExampleSearchSpacesTest, 'test_%s' % pcs_file.replace('.', '_'),
                generate(full_path))
