def celtofah(vcel):
    fah = 1.4*float(vcel)+32.0
    var = str(fah)
    return var
def celtokel(vcel):
    kel = float(vcel)+273.15
    var = str(kel)
    if kel < 0:
        return False
    else:
        return var