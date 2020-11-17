

import GetBondPrice

def test_getBondPrice(y, face, couponRate, m,  ppy):
    assert round(GetBondPrice.getBondPrice(.03, 2000000, .04, 10,  1)) == 2170604
    assert round(GetBondPrice.getBondPrice(.03, 2000000, .04, 10,  2)) == 2171686
