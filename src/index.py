from entities.map import Map
from services.room_generation_service import RoomGenerationService
from services.maze_generation_service import MazeGenerationService
from services.drawing_service import DrawingService
from repositories.map_repository import MapRepository

def main():
    cell_width = 20
    cell_height = 20
    map_obj = Map()
    room_gen = RoomGenerationService(cell_width, cell_height)
    room_gen.generate_room((1,1), 4, 5)
    room_gen.generate_room((8,8), 2, 7)
    drawing = DrawingService(room_gen, map_obj, (cell_width, cell_height))
    drawing.draw_rooms()
    maze_gen = MazeGenerationService(map_obj)
    maze_gen.init_maze()
    maze_gen.generate_perfect_maze()
    drawing.draw_corridors()
    drawing.draw_grid()
    MapRepository(drawing.get_image()).save("demo/test")
    print(map_obj)

if __name__ == "__main__":
    main()
