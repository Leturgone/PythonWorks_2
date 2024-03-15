def main(x):
    u1 = (x>>0) & 0b1111_1111
    u2 = (x>>8) & 0b1111_1111
    u3 = (x>>16) & 0b1
    u4 = (x>>17) & 0b1111_111
    result = (hex(u1),hex(u2),hex(u3),hex(u4))
    return result

print(main(11116542))