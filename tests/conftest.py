import pytest

ARRAY = [0,1,2,3,4,5,6,7,8,9,10]
DICT = {
    'saske':'anti-hero',
    'naruto':'hero',
    'kakashi':'hero',
    'daidara':'villian',
    'zabuza':'villian',
    'madara':'villian',
}

@pytest.fixture
def array_fixture():
    return ARRAY.copy()

@pytest.fixture
def dict_fixture():
    return DICT.copy()