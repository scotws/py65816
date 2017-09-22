# Hardware Definitions for Py65816
# Scot W. Stevenson <scot.stevenson@gmail.com>
# First version: 22. Sep 2017
# This version: 22. Sep 2017

class Memory:
    """Complete memory range of the virtual system.
    """

    def __init__(self):
        self.blocks = []


class Memblock:
    """Single continuous memory range, either RAM or ROM
    """

    def __init__(self, start, end, type="ram"):
        self.start = start
        self.end = end
        self.type = type
        self.size = end - start + 1
        self.data = bytearray(size)  # initializes as zero

    def __contains__(self, addr):
        """See if address given is inside memory range
        """
        f = False

        if addr <= self.start and addr >= self.end:
            f = True

        return f
