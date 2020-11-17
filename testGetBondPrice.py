

import GetBondPrice

def test_getBondPrice(y, face, couponRate, m,  ppy):
    x = GetBondPrice.getBondPrice(y, face, couponRate, m,  ppy)
    assert(round(x) == 2170604)
    x = GetBondPrice.getBondPrice(y, face, couponRate, m,  2)
    assert(round(x) == 2171686)
    return(x)