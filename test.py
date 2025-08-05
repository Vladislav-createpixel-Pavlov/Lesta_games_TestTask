import pytest
import allure
from src.boat import RowingBoat

@pytest.fixture(scope="module")
def boat():
    return RowingBoat()
@allure.story("Первый тест")
def test_load_passenger_success(boat):
    assert boat.load_passenger(70) is True
    assert boat.current_passengers == 1
@allure.story("Второй тест")
def test_load_passenger_failure(boat):
    for _ in range(4):
        boat.load_passenger(70)
        assert boat.load_passenger(70) is False
@allure.story("Третий тест")
def test_change_direction_valid(boat): 
    assert boat.change_direction("south") is True
    assert boat.direction == "south"
@allure.story("Четвертый тест")
def test_change_direction_invalid(boat):
    assert boat.change_direction("invalid") is False
    assert boat.direction != "invalid"
@allure.story("Пятый тест")
def test_check_status_initial_state(boat):
    status = boat.check_status()
    expected_status = {'is_floating': True, 'current_passengers': 0, 'speed': 0, 'direction': 'north'}
    assert status == expected_status
