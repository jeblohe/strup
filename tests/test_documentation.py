import pytest

from strup import unpack, Unpack


def test_doc_1():
    line = "2.3 ole True 55  12"
    res = unpack("fs?ii", line)
    assert len(res) == 5
    assert res[0] == pytest.approx(2.3)
    assert res[1] == "ole"
    assert res[2] is True
    assert res[3] == 55
    assert res[4] == 12


def test_doc_2():
    res = unpack("f..s", " 2.3 ,ole,55,   dole", sep=',')
    assert len(res) == 2
    assert res[0] == pytest.approx(2.3)
    assert res[1] == '   dole'


def test_doc_3():
    res = unpack("f???s.????", "2.3 NO 0 F ole dole yes 1 ON TruE")
    assert len(res) == 9
    assert res[0] == pytest.approx(2.3)
    assert res[1] is False
    assert res[2] is False
    assert res[3] is False
    assert res[4] == 'ole'
    assert res[5] is True
    assert res[6] is True
    assert res[7] is True
    assert res[8] is True


def test_doc_4():
    res = unpack("isf", "100 'Donald Duck' 125.6", quote="'")
    assert len(res) == 3
    assert res[0] == 100
    assert res[1] == 'Donald Duck'
    assert res[2] == pytest.approx(125.6)


def test_doc_5():
    res1 = unpack("isf", "100 'She''s the best' 125.6", quote="'")
    res2 = unpack("isf", '3 "A ""quote"" test"  93.4 ignored', quote='"')
    assert len(res1) == 3
    assert res1[0] == 100
    assert res1[1] == "She's the best"
    assert res1[2] == pytest.approx(125.6)
    assert len(res2) == 3
    assert res2[0] == 3
    assert res2[1] == 'A "quote" test'
    assert res2[2] == pytest.approx(93.4)


def test_doc_6():
    res = unpack("isf", r"100 'She\'s the best' 125.6", quote="'", quote_escape=r"\'")
    assert len(res) == 3
    assert res[0] == 100
    assert res[1] == "She's the best"
    assert res[2] == pytest.approx(125.6)


def test_doc_7():
    mydecode = Unpack('.s..f', quote='"')
    res = []
    for line in ['5.3 "Donald Duck" 2 yes 5.4',
                 '-2.2 "Uncle Sam" 4  no 1.5',
                 '3.3  "Clint Eastwood" 7 yes 6.5']:
        res.append(mydecode(line))
    r = res[0]
    assert len(r) == 2
    assert r[0] == "Donald Duck"
    assert r[1] == pytest.approx(5.4)
    r = res[1]
    assert len(r) == 2
    assert r[0] == "Uncle Sam"
    assert r[1] == pytest.approx(1.5)
    r = res[2]
    assert len(r) == 2
    assert r[0] == "Clint Eastwood"
    assert r[1] == pytest.approx(6.5)
