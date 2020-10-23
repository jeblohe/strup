import pytest

from strup import unpack


def test_exception_1():
    with pytest.raises(ValueError):
        s = '4'
        res = unpack('i.f', s)


def test_exception_2():
    with pytest.raises(ValueError):
        s = 'doffen'
        res = unpack('f', s)


def test_exception_3():
    with pytest.raises(ValueError):
        s = "1 2 3 4"
        res = unpack('iX.f', s)


def test_exception_5():
    with pytest.raises(ValueError):
        s = "1 2 3 4"
        i, j, k, l, m, o = unpack('iiii', s)


def test_exception_6():
    with pytest.raises(ValueError):
        s = "1 2 3 4"
        res = unpack('iiii', s, sep='')


def test_exception_7():
    with pytest.raises(ValueError):
        s = "ole 'dole' doffen"
        res = unpack('sss', s, sep=' ', quote='#')


def test_exception_8():
    with pytest.raises(ValueError):
        s = "ole 'dole' doffen"
        res = unpack('sss', s, quote=' ')


def test_exception_9():
    with pytest.raises(ValueError):
        s = "ole 'dole' doffen"
        res = unpack('sss', s, sep='Q', quote='Q')


def test_exception_10():
    with pytest.raises(ValueError):
        s = "ole 'dole#s' doffen"
        res = unpack('sss', s, quote="'", quote_escape='#')


def test_exception_11():
    with pytest.raises(ValueError):
        s = "ole'donald duck'doffen"
        res = unpack('sss', s, sep="'", quote="'")


def test_exception_12():
    with pytest.raises(ValueError):
        s = "ole dole doffen"
        res = unpack('ifi', s)


def test_exception_13():
    with pytest.raises(ValueError):
        s = "ole 1.5 .true. doffen"
        res = unpack('sf?s', s)


def test_exception_14():
    with pytest.raises(ValueError):
        s = "ole 1.5 .true. doffen"
        res = unpack('s...', s)


def test_exception_15():
    with pytest.raises(ValueError):
        s = '2.3 """ " 12'
        # Sep is a white space. There should be space between the two strings
        res = unpack("fssi", s, quote='"', none=True)
