
from utils.arrs import get,my_slice


def test_get(array_fixture):
    assert get(array_fixture, 0) == 0
    assert get(array_fixture, 10) == 10
    assert get(array_fixture, -1) == None
    assert get(array_fixture,11) == None

def test_my_slice(array_fixture):
    assert my_slice(array_fixture) == [0,1,2,3,4,5,6,7,8,9,10]
    assert my_slice(array_fixture, 2, ) == [2,3,4,5,6,7,8,9,10]
    assert my_slice(array_fixture, 3, 5) == [3,4]
    assert my_slice(array_fixture, -1, -3) == []
    assert my_slice(array_fixture, None, 4) == [0,1,2,3]
    assert my_slice(array_fixture,5,3) == []
    assert my_slice(array_fixture, None, -3) == [0, 1, 2, 3, 4, 5, 6, 7]
    assert my_slice(array_fixture,-2) == [9,10]