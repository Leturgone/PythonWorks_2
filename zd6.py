# import math


# # def main(input_set):
# #     # Calculate O
# #     oO = {math.ceil(p / 9) for p in input_set if not -79 < p < 67}
# #     # Calculate I
# #     iI = {p - p % 2 for p in input_set if -99999999999999999999 < p <= 34}
# #     # Calculate Z
# #     zZ = {5 * o - E ** 2 for o in oO for E in iI if o > E}
    
# #     sum1 = sum(math.fabs(E) for E in iI)
# #     sum2 = sum(E * C for E in iI for C in zZ)
# #     res = int(sum1 - sum2)
# #     return res

from math import fabs, floor


def main(fF):
    oO = {fabs(f) - floor(f/5) for f in fF if -78<f<91}
    lL = oO | fF
    wW = {i%3 - fabs(i) for i in lL if -61<=i<13 }
    delta = {o - 9*o for o in oO if -87<o<63}
    
    ooO =len(delta) - sum(fabs(w) for w in wW)
    return int(ooO)

print(main({-31, -29, 36, 5, -26, 47, -45, -9, -37, 62}))
print(main({-95, 37, 11, 76, 48, 21, -74, -68, -3, 30}))