# Hardware Definitions for Py65816
# Scot W. Stevenson <scot.stevenson@gmail.com>
# First version: 22. Sep 2017
# This version: 22. Sep 2017

class Memory:
    """Complete memory range of the virtual system.
    """

    def __init__(self):
        self.blocks = []

    def __str__(self):
        """Print all memory blocks
        """
        msg = '\n'.join(str(b) for b in self.blocks)
        return msg

    def fetch08(self, addr):
        """Fetch a byte from the given address
        Throws index error if address is not available
        """

    def add(self, block):
        """Add a memory block to memory list
        """
        if not isinstance(block, Memblock):
            msg = 'Can only add memory blocks to memory list'
            raise TypeError(msg)

        self.blocks.append(block)



class Memblock:
    """Single continuous memory range, either RAM or ROM
    """

    def __init__(self, start, end, type='ram', source=''):
        self.start = start
        self.end = end
        self.type = type
        self.source = source
        self.size = end - start + 1
        self.data = bytearray(self.size)  # initializes as zero

        # TODO Load ROM file into memory if given
        if type == 'rom' and source:
            print('TODO: Load ROM file')

    def __contains__(self, addr):
        """See if address given is inside memory range
        """
        f = False

        if addr <= self.start and addr >= self.end:
            f = True

        return f

    def __repr__(self):
        """Print representantion of object
        """
        msg = "Memblock({0}, {1}, {2} {3})".format(self.start, self.end, self.type, self.source)
        return msg

    def __str__(self):
        """Print basic sizes when printed
        """
        msg = "{0:06x} {1:06x} {2} {3}".format(self.start, self.end, self.type, self.source)
        return msg

    def fetch08(self, addr):
        """Get one byte from memory
        """
        i = addr - self.start
        b = self.data[i]

        return b

    def store08(self, addr, b):
        """Store one byte at the given address. Does nothing if memory
        is of the type ROM
        """
        if type == 'rom':
            return

        i = addr - self.start
        self.data[i] = b

    def hexdump(self):
        """Print hexdump of memory block
        """
        print("TODO not coded yet")


# TODO Temporary testing routines

if __name__ == '__main__':
    test1 = Memblock(0x0000, 0x7fff, 'ram')
    test2 = Memblock(0x8000, 0xffff, 'rom', '/dev/null')
    mem = Memory()

    print(test1)
    print(repr(test1))
    print(test2)
    print(repr(test2))

    addr1 = 0x1000

    if addr1 in test1:
        print('Address 1 in test 1')

    print('Original byte: ', test1.fetch08(addr1))
    print('Saving byte 0xff')
    test1.store08(addr1, 0xff)
    print('New byte: ', test1.fetch08(addr1))

    mem.add(test1)
    mem.add(test2)
    print(mem)