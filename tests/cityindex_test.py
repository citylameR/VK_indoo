import pytest
import vk


@pytest.mark.parametrize("city, expected", [("Петербург", 2), ("Москва", 1)])
def test_cityindex(city, expected):
    res = vk.city.get_city_index(city)["id"]
    assert res == expected
