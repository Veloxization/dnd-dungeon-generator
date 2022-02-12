import unittest
from unittest.mock import Mock
from services.drawing_service import DrawingService
from services.room_generation_service import RoomGenerationService
from services.image_generation_service import ImageGenerationService
from entities.map import Map
from entities.room import Room

class TestDrawingService(unittest.TestCase):
    def setUp(self):
        self.room_generation_service = RoomGenerationService()
        self.map = Map()
        self.test_drawing_service1 = DrawingService(self.room_generation_service, self.map)
        self.image_generation_service_mock = Mock(wraps=ImageGenerationService())
        self.test_drawing_service1._image_generation_service = self.image_generation_service_mock

    def test_room_is_not_drawn_if_it_extends_beyond_the_right_edge(self):
        room = Room((49,1))
        self.assertFalse(self.test_drawing_service1._can_draw_room(room))

    def test_room_is_not_drawn_if_it_extends_beyond_the_bottom_edge(self):
        room = Room((1,49))
        self.assertFalse(self.test_drawing_service1._can_draw_room(room))

    def test_room_is_not_drawn_on_top_of_an_existing_room(self):
        self.room_generation_service.generate_room((1,1))
        self.room_generation_service.generate_room((2,2))
        self.test_drawing_service1.draw_rooms()
        self.assertFalse(self.room_generation_service.rooms[1].is_generated)

    def test_room_can_be_drawn_in_an_unoccupied_space(self):
        room = Room((1,1))
        self.assertTrue(self.test_drawing_service1._can_draw_room(room))

    def test_cells_are_converted_to_coordinates_correctly(self):
        self.assertEqual(self.test_drawing_service1._get_coordinate_value(1,1), (20,20))

    def test_a_valid_room_will_be_drawn_successfully(self):
        self.room_generation_service.generate_room((1,1))
        self.test_drawing_service1.draw_rooms()
        self.image_generation_service_mock.draw_room.assert_called_with(20, 20, 40, 40)

    def test_an_invalid_room_will_not_be_drawn(self):
        self.room_generation_service.generate_room((1,49))
        self.test_drawing_service1.draw_rooms()
        self.image_generation_service_mock.assert_not_called()

    def test_grid_is_drawn_with_correct_line_thickness(self):
        self.test_drawing_service1.draw_grid(2)
        self.image_generation_service_mock.draw_grid.assert_called_with(20, 20, 2)

    def test_get_image_is_called_correctly(self):
        self.test_drawing_service1.get_image()
        self.image_generation_service_mock.get_generated_image.assert_called()

    def test_corridors_are_drawn_in_the_correct_position(self):
        self.map.occupy(1,1)
        self.test_drawing_service1.draw_corridors()
        self.image_generation_service_mock.draw_room.assert_called_with(20, 20, 20, 20)
        self.map.unoccupy(1,1)
        self.map.occupy(1,2)
        self.test_drawing_service1.draw_corridors()
        self.image_generation_service_mock.draw_room.assert_called_with(20, 40, 20, 20)