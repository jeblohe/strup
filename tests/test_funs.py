import pytest

from strup import unpack


def test_fun_1():
    s = '4'
    res = unpack('i', s)
    assert len(res) == 1
    assert res[0] == 4


def test_fun_2():
    s = ' -.3 '
    res = unpack('f', s)
    assert len(res) == 1
    assert -0.3 == pytest.approx(res[0])


def test_fun_3():
    s = ' ole  '
    res = unpack('s', s)
    assert len(res) == 1
    assert res[0] == 'ole'


def test_fun_4():
    s = '"ole"'
    res = unpack('s', s)
    assert len(res) == 1
    assert res[0] == '"ole"'


def test_fun_5():
    s = '"ole"'
    res = unpack('s', s, quote='"')
    assert len(res) == 1
    assert res[0] == 'ole'


def test_fun_6():
    s = "'ole'"
    res = unpack('s', s, quote="'")
    assert len(res) == 1
    assert res[0] == 'ole'


def test_fun_7():
    s = '-3 and some trailing junk'
    res = unpack('i', s)
    assert len(res) == 1
    assert res[0] == -3


def test_fun_8():
    s = 'Positive: y Yes t True On 1    Negative: N no F false   Off 0'
    res = unpack('.??????.??????', s)
    assert len(res) == 12
    assert res[0] is True
    assert res[1] is True
    assert res[2] is True
    assert res[3] is True
    assert res[4] is True
    assert res[5] is True
    assert res[6] is False
    assert res[7] is False
    assert res[8] is False
    assert res[9] is False
    assert res[10] is False
    assert res[11] is False


def test_fun_9():
    s = '3 4.5  ole  no   dole -5 doffen'
    res = unpack('ifs?sis', s)
    assert len(res) == 7
    assert res[0] == 3
    assert 4.5 == pytest.approx(res[1])
    assert res[2] == "ole"
    assert res[3] is False
    assert res[4] == "dole"
    assert res[5] == -5
    assert res[6] == "doffen"


def test_fun_10():
    s = '25  "She\'s the best" -34.5'
    res = unpack('isf', s, quote='"')
    assert len(res) == 3
    assert res[0] == 25
    assert res[1] == "She's the best"
    assert -34.5 == pytest.approx(res[2])


def test_fun_11():
    s = '3,4.5,  ole,dole,5,doffen'
    res = unpack('.fs', s, sep=',')
    assert len(res) == 2
    assert 4.5 == pytest.approx(res[0])
    assert res[1] == "  ole"


def test_fun_12():
    s = '3 "A ""quote"" test" 93.4 knut ignored'
    res = unpack('isfs', s, sep=' ', quote='"', quote_escape='""')
    assert len(res) == 4
    assert res[0] == 3
    assert res[1] == 'A "quote" test'
    assert 93.4 == pytest.approx(res[2])
    assert res[3] == 'knut'


def test_fun_13():
    s = "3 'A ''quote'' test' 93.4 knut ignored"
    res = unpack('isfs', s, sep=' ', quote="'", quote_escape="''")
    assert len(res) == 4
    assert res[0] == 3
    assert res[1] == "A 'quote' test"
    assert 93.4 == pytest.approx(res[2])
    assert res[3] == 'knut'


def test_fun_14():
    s = "*ole*donald duck*doffen"
    res = unpack('sss', s, sep="*")
    assert len(res) == 3
    assert res[0] == ''
    assert res[1] == 'ole'
    assert res[2] == 'donald duck'


def test_fun_15():
    s = "*ole*  'donald duck'  * doffen"
    res = unpack('sss', s, sep="*", quote="'")
    assert len(res) == 3
    assert res[0] == ''
    assert res[1] == 'ole'
    assert res[2] == "  'donald duck'  "


def test_fun_16():
    s = ",ole,,,peter "
    res = unpack('sssss', s, sep=",")
    assert len(res) == 5
    assert res[0] == ''
    assert res[1] == 'ole'
    assert res[2] == ''
    assert res[3] == ''
    assert res[4] == 'peter '


def test_fun_17():
    s = " ole,,,peter"
    res = unpack('ssss', s, sep=",")
    assert len(res) == 4
    assert res[0] == ' ole'
    assert res[1] == ''
    assert res[2] == ''
    assert res[3] == 'peter'


def test_fun_18():
    s = "ole,,,peter,"
    res = unpack('sssss', s, sep=",")
    assert len(res) == 5
    assert res[0] == 'ole'
    assert res[1] == ''
    assert res[2] == ''
    assert res[3] == 'peter'
    assert res[4] == ''


def test_fun_19():
    s = '3,4.5,yes,  ole,dole,5,doffen'
    res = unpack('.f?s..s', s, sep=',')
    assert len(res) == 4
    assert 4.5 == pytest.approx(res[0])
    assert res[1] is True
    assert res[2] == "  ole"
    assert res[3] == "doffen"


def test_fun_20():
    s = ',, ,,'
    res = unpack('sssss', s, sep=',', none=True)
    assert len(res) == 5
    assert res[0] is None
    assert res[1] is None
    assert res[2] == " "
    assert res[3] is None
    assert res[4] is None


def test_fun_21():
    s = '2.3 "" " " 12'
    res = unpack("fssi", s, quote='"', none=True)
    assert len(res) == 4
    assert 2.3 == pytest.approx(res[0])
    assert res[1] is None
    assert res[2] == " "
    assert res[3] == 12


def test_fun_22():
    s = '1999,Chevy,"Venture ""Extended Edition, Very Large""","",5000.00'
    res = unpack('isssf', s, sep=',', quote='"', quote_escape='""')
    assert len(res) == 5
    assert res[0] == 1999
    assert res[1] == "Chevy"
    assert res[2] == 'Venture "Extended Edition, Very Large"'
    assert res[3] == ""
    assert res[4] == pytest.approx(5000.0)


def test_fun_23():
    s = '1997,Ford,E350,"ac, abs, moon",3000.00'
    res = unpack('isssf', s, sep=',', quote='"', quote_escape='""')
    assert len(res) == 5
    assert res[0] == 1997
    assert res[1] == "Ford"
    assert res[2] == "E350"
    assert res[3] == "ac, abs, moon"
    assert res[4] == pytest.approx(3000.0)


def test_fun_24():
    s = r'5 2 4.5     "ole is great \" but stupid!"    6'
    res = unpack('i.fsi', s, sep=None, quote='"', quote_escape=r'\"')
    assert len(res) == 4
    assert res[0] == 5
    assert res[1] == pytest.approx(4.5)
    assert res[2] == 'ole is great " but stupid!'
    assert res[3] == 6


def test_fun_25():
    s = r'5 <> 2 <> 4.5 <>"ole is great """" <> but stupid!"<>    6'
    res = unpack('i.fsi', s, sep='<>', quote='"', quote_escape='""')
    assert len(res) == 4
    assert res[0] == 5
    assert res[1] == pytest.approx(4.5)
    assert res[2] == 'ole is great "" <> but stupid!'
    assert res[3] == 6


def test_fun_26():
    s = r',,5,try,'
    res = unpack('ssiss', s, sep=',')
    assert len(res) == 5
    assert res[0] == ''
    assert res[1] == ''
    assert res[2] == 5
    assert res[3] == 'try'
    assert res[4] == ''


def test_fun_27():
    s = r',,5,try,"",'
    res = unpack('ssisss', s, quote='"', sep=',')
    assert len(res) == 6
    assert res[0] == ''
    assert res[1] == ''
    assert res[2] == 5
    assert res[3] == 'try'
    assert res[4] == ''
    assert res[5] == ''


def test_fun_28():
    s = '3 "A ""quote"" test" 93.4 knut ignored'
    res = unpack('isfs', s, sep=' ', quote='"', quote_escape='""')
    assert len(res) == 4
    assert res[0] == 3
    assert res[1] == 'A "quote" test'
    assert res[2] == pytest.approx(93.4)
    assert res[3] == 'knut'
