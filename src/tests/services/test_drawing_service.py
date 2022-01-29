import unittest
from services.drawing_service import DrawingService
from services.room_generation_service import RoomGenerationService
from entities.map import Map
from entities.room import Room

class TestDrawingService(unittest.TestCase):
    def setUp(self):
        self.room_generation_service = RoomGenerationService()
        self.map = Map()
        self.test_drawing_service1 = DrawingService(self.room_generation_service, self.map)

    def test_room_is_not_drawn_if_it_extends_beyond_the_right_edge(self):
        room = Room((49,1))
        self.assertEqual(self.test_drawing_service1._can_draw_room(room), False)

    def test_room_is_not_drawn_if_it_extends_beyond_the_bottom_edge(self):
        room = Room((1,49))
        self.assertEqual(self.test_drawing_service1._can_draw_room(room), False)

    def test_room_can_be_drawn_in_an_unoccupied_space(self):
        room = Room((1,1))
        self.assertEqual(self.test_drawing_service1._can_draw_room(room), True)

    def test_cells_are_converted_to_coordinates_correctly(self):
        self.assertEqual(self.test_drawing_service1._get_coordinate_value(1,1), (20,20))
