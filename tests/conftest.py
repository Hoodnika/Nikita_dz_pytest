import pytest

ARRAY = [0,1,2,3,4,5,6,7,8,9,10]

@pytest.fixture
def array_fixture():
    return ARRAY.copy()