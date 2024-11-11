from unittest import TestCase
from api.routes import car_routes

class TestCars(TestCase):
    def test_add_new_car(self) -> None:
        self.assertIn("Hello", car_routes.add_new_car({'name': 'uno com escada', 'status': 'veloz'}))