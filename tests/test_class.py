import pytest

from strup import Unpack


# The class Unpack is implicitly tested in "test_funs.py" too...


def test_class_1():
    decode = Unpack('.f..s')
    for line in ['go 3.14  back 4 more',
                 'not 2.71 in my dream',
                 'this 6 is way to much']:
        xval, txt = decode(line)
        assert txt in ["more", "dream", "to"]


def test_class_2():
    decode = Unpack('.f..s', sep=',')
    for line in ['go,3.14,back,4,more',
                 'not,2.71,in,my,dream',
                 'this,6,is,way,to,much']:
        xval, txt = decode(line)
        assert txt in ["more", "dream", "to"]


def test_class_3():
    decode = Unpack('.s..f', quote='"')
    for line in ['5.3 "Donald Duck" 2 yes 5.4',
                 '-2.2 "Uncle Sam" 4  no 1.5',
                 '3.3  "Clint Eastwood" 7 yes 6.5']:
        name, score = decode(line)
        assert name in ["Donald Duck", "Uncle Sam", "Clint Eastwood"]
