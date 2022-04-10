# udp header pack/unpack


import socket
import struct
import binascii


class Udphdr:
    def __init__(self, sport, dport, length, check):
        self.sport = sport
        self.dport = dport
        # self.ver_len = 0x45
        # self.tos = 0
        self.length = length
        # self.id = 0
        # self.frag_off = 0
        # self.ttl = 127
        # self.protocol = 17 #TCP(6)/UDP(17)
        self.check = check

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!4H', self.sport, self.dport,
                              self.length, self.check)
        return packed


def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!4H', buffer[:8])
    return unpacked


def getSrcPort(unpacked_udpheader):
    return unpacked_udpheader[0]  # sport


def getDstPort(unpacked_udpheader):
    return unpacked_udpheader[1]  # dport


def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]  # length


def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]  # check


udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()  # pack 해서 저장
print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}' .format(getSrcPort(unpacked_udphdr),
                                                                         getDstPort(unpacked_udphdr), getLength(unpacked_udphdr), getChecksum(unpacked_udphdr)))
