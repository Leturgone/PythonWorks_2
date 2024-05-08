# #Второй вариант
# from struct import *


# FMT = dict(
#     char='c',
#     int8='b',
#     uint8='B',
#     int16='h',
#     uint16='H',
#     int32='i',
#     uint32='I',
#     int64='q',
#     uint64='Q',
#     float='f',
#     double='d'
# )

# def read(buf, offs, ty, order='<'):
#     pattern = FMT[ty]
#     size = calcsize(pattern)
#     value = unpack_from(order + pattern, buf, offs)[0]
#     return value, offs + size

# def read_struct_D(data,offset):
#     d1, offset = read(data,offset, 'float')
#     d2 = []
#     for _ in range(7):
#         elem, offset = read(data, offset,'int16')
#         d2.append(elem)
#     d3, offset = read(data, offset, 'uint8')
#     return dict(D1 = d1, D2 = d2, D3 = d3), offset

# def read_struct_C(data, offset):
#     c1_size, offset = read(data, offset, 'uint16')
#     c1_offset, offset = read(data, offset, 'uint32')
#     c1 = []
#     for _ in range(c1_size):
#         val, c1_offset = read(data, c1_offset, 'char')
#         c1.append(val)
#     c1 = b''.join(c1).decode()
#     c2, offset = read(data, offset, 'uint64')
#     c3, offset = read(data, offset, 'uint32')
#     return dict(C1 = c1, C2 = c2, C3 = c3), offset

# def read_struct_B(data, offset):
#     b1, offset = read(data, offset, 'uint8')
#     b2_offset, offset = read(data, offset, 'uint32')
#     b2,_ = read_struct_C(data, b2_offset)
#     b3, offset = read(data, offset, 'uint16')
#     b4, offset = read(data, offset, 'int64')
#     b5, offset = read(data, offset, 'int16')
#     b6, offset = read(data, offset, 'uint64')
#     b7, offset = read(data, offset, 'double')
#     b8_size, offset = read(data, offset, 'uint16')
#     b8_offset, offset = read(data, offset, 'uint16')
#     b8 = []
#     for _ in range(b8_size):
#         val, b8_offset = read(data, b8_offset, 'char')
#         b8.append(val)
#     b8 = c1 = b''.join(b8).decode()
#     return dict(B1 = b1, B2 = b2, B3 = b3, B4 = b4, B5 = b5, B6 = b6, B7 = b7, B8 = b8 ), offset

# def read_struct_A(data, offset):
#     a1, offset = read_struct_B(data, offset)
#     a2, offset = read(data, offset, 'int16')
#     a3, offset = read(data, offset, 'uint64')
#     a4_size, offset = read(data, offset, 'uint32')
#     a4_offset, offset = read(data, offset, 'uint32')
#     a4 = []
#     #Размер (uint32) и адрес (uint32) массива адресов (uint32) структур D
#     for _ in range(a4_size):
#         d_offset, a4_offset = read(data, a4_offset, 'uint32')
#         val, _= read_struct_D(data, d_offset)
#         a4.append(val)
#     return dict(A1 = a1, A2 = a2, A3 = a3, A4 = a4), offset


# def main(stream):
#     res, _ = read_struct_A(stream, 5)
#     return res

# data = (b'pJKUE\x01>\x00\x00\x00\xa0r\xcb\xcfx\'\xb90\xf8\xb6\xdc("x\x9c\xdct1'
#         b'O\x16\x06\x96to\xaa\x93\xe1\xbf\x04\x00P\x00\xd5J\xc1\xa9\x17m'
#         b'\xb2\xc8\xfc\xcf\x02\x00\x00\x00z\x00\x00\x00vn\x02\x00<\x00\x00\x00'
#         b'\x83.\xf3p>\x1a\x08kD\xaa\xa0\rsnjl\xa2\xbbg\xbe\xe6J\x97\xa2\x8dN\xe88'
#         b'\x01+1\xdda\xfd)\\\xa6"\xbe)\xdd\xe0\xdc\xbe\x8cp\xeb;9@\xe7\xd6'
#         b'\xdf\xf5T\x00\x00\x00g\x00\x00\x00')

# print(main(data))

#Первый вариант
import struct


def read_char(data, offset):
    return struct.unpack_from('<c', data, offset)[0], offset + 1

def read_int8(data, offset):
    return struct.unpack_from('<b', data, offset)[0], offset + 1

def read_int64(data, offset):
    return struct.unpack_from('<q', data, offset)[0], offset + 8

def read_uint32(data, offset):
    return struct.unpack_from('<I', data, offset)[0], offset + 4

def read_float(data, offset):
    return struct.unpack_from('<f', data,offset)[0], offset + 4

def read_uint16(data, offset):
    return struct.unpack_from('<H', data, offset)[0], offset + 2

def read_uint8(data, offset):
    return struct.unpack_from('<B', data, offset)[0], offset + 1

def read_uint64(data, offset):
    return struct.unpack_from('<Q', data, offset)[0], offset + 8

def read_int16(data, offset):
    return struct.unpack_from('<h', data, offset)[0], offset + 2

def read_double(data, offset):
    return struct.unpack_from('<d', data, offset)[0], offset + 8

def read_struct_D(data,offset):
    d1, offset = read_float(data,offset)
    d2 = []
    for _ in range(7):
        elem, offset = read_int16(data, offset)
        d2.append(elem)
    d3, offset = read_uint8(data, offset)
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset

def read_struct_C(data, offset):
    c1_size, offset = read_uint16(data, offset)
    c1_offset, offset = read_uint32(data, offset)
    c1 = []
    for _ in range(c1_size):
        val, c1_offset = read_char(data, c1_offset)
        c1.append(val)
    c1 = b''.join(c1).decode()
    c2, offset = read_uint64(data, offset)
    c3, offset = read_uint32(data,offset)
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset

def read_struct_B(data, offset):
    b1, offset = read_uint8(data, offset)
    b2_offset, offset = read_uint32(data, offset)
    b2,_ = read_struct_C(data, b2_offset)
    b3, offset = read_uint16(data, offset)
    b4, offset = read_int64(data, offset)
    b5, offset = read_int16(data,offset)
    b6, offset = read_uint64(data, offset)
    b7, offset = read_double(data, offset)
    b8_size, offset = read_uint16(data, offset)
    b8_offset, offset = read_uint16(data, offset)
    b8 = []
    for _ in range(b8_size):
        val, b8_offset = read_char(data, b8_offset)
        b8.append(val)
    b8 = c1 = b''.join(b8).decode()
    return{ 'B1': b1, 'B2': b2, 'B3': b3, 'B4':b4, 
           'B5': b5, 'B6': b6, 'B7': b7, 'B8': b8}, offset

    
def read_struct_A(data, offset):
    a1, offset = read_struct_B(data,offset)
    a2, offset = read_int16(data, offset)
    a3, offset = read_uint64(data, offset)
    a4_size, offset = read_uint32(data, offset)
    a4_offset, offset = read_uint32(data, offset)
    a4 = []
    #Размер (uint32) и адрес (uint32) массива адресов (uint32) структур D
    for _ in range(a4_size):
        d_offset, a4_offset = read_uint32(data, a4_offset)
        val, _= read_struct_D(data, d_offset)
        a4.append(val)
    return{'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}

def main(data):
    if data[:5] != b'pJKUE':
        raise ValueError("Invalid data signature")
    offset = 5
    return read_struct_A(data,offset)


data = (b'pJKUE\x01>\x00\x00\x00\xa0r\xcb\xcfx\'\xb90\xf8\xb6\xdc("x\x9c\xdct1'
        b'O\x16\x06\x96to\xaa\x93\xe1\xbf\x04\x00P\x00\xd5J\xc1\xa9\x17m'
        b'\xb2\xc8\xfc\xcf\x02\x00\x00\x00z\x00\x00\x00vn\x02\x00<\x00\x00\x00'
        b'\x83.\xf3p>\x1a\x08kD\xaa\xa0\rsnjl\xa2\xbbg\xbe\xe6J\x97\xa2\x8dN\xe88'
        b'\x01+1\xdda\xfd)\\\xa6"\xbe)\xdd\xe0\xdc\xbe\x8cp\xeb;9@\xe7\xd6'
        b'\xdf\xf5T\x00\x00\x00g\x00\x00\x00')

print(main(data))