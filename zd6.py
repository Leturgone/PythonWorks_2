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