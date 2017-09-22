# Py65816 - A 65816 CPU Emulator in Python
# Scot W. Stevenson <scot.stevenson@gmail.com>
# First version: 22. Sep 2017
# This version: 22. Sep 2017

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Py65816 is an emulator for the 65816 MPU/CPU.
"""

import argparse
import sys

if sys.version_info.major != 3:
    print("FATAL: Python 3 required. Aborting.")
    sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='source', required=True,
        help='Assembler source code file (required)')



