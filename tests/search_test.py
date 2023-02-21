import pytest
from vk import search
settings = {'city': '2', 'sex': '2', 'age_min': '18', 'age_max': '23'}

@pytest.mark.parametrize("city, sex, age_min, age_max",
                         [('2', '1', '18', '33'),
                          ('1', '1', '30', '40')])
def test_search(city, sex, age_min, age_max):
    res = search.search(city, sex, age_min, age_max)
    assert len(res)>0