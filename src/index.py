from entities.map import Map
from services.room_generation_service import RoomGenerationService
from services.maze_generation_service import MazeGenerationService
from services.drawing_service import DrawingService
from repositories.map_repository import MapRepository

def main():
    cell_width = 10
    cell_height = 10
    map_width = 100
    map_height = 100
    rooms_to_generate = 100
    room_min_width = 5
    room_max_width = 10
    room_min_height = 5
    room_max_height = 10
    map_obj = Map(map_width, map_height)
    room_gen = RoomGenerationService(cell_width, cell_height, map_width, map_height)
    room_gen.generate_random_rooms(rooms_to_generate, room_min_width, room_max_width, room_min_height, room_max_height)
    drawing = DrawingService(room_gen, map_obj, (cell_width, cell_height))
    drawing.draw_rooms()
    maze_gen = MazeGenerationService(map_obj)
    maze_gen.init_maze()
    maze_gen.generate_perfect_maze()
    drawing.draw_corridors()
    drawing.draw_grid()
    MapRepository(drawing.get_image()).save("demo/test")

if __name__ == "__main__":
    main()
