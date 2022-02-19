from tkinter import *
from tkinter import ttk
from entities.map import Map
from services.room_generation_service import RoomGenerationService
from services.maze_generation_service import MazeGenerationService
from services.drawing_service import DrawingService
from repositories.map_repository import MapRepository

class MainGUI:
    """The main GUI class handling opening of the basic view of the GUI."""

    def __init__(self):
        root = Tk()
        root.title("D&D Dungeon Generator")
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        scaleframe = ttk.Frame(root, padding="3 3 12 12")
        scaleframe.grid(column=0, row=1, sticky=(N, W, E, S))
        buttonframe = ttk.Frame(root, padding="3 3 12 12")
        buttonframe.grid(column=0, row=2)
        errorframe = ttk.Frame(root, padding="3 3 12 12")
        errorframe.grid(column=0, row=3)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # INPUTS
        self.cell_dimensions = IntVar(value=5)
        cell_dimensions_entry = ttk.Entry(mainframe,
                                          width=7,
                                          textvariable=self.cell_dimensions)
        cell_dimensions_entry.grid(column=2, row=1, sticky=(W, E))

        self.map_width = IntVar(value=20)
        map_width_entry = ttk.Entry(mainframe,
                                    width=7,
                                    textvariable=self.map_width)
        map_width_entry.grid(column=2, row=2, sticky=(W, E))
        self.map_height = IntVar(value=20)
        map_height_entry = ttk.Entry(mainframe,
                                     width=7,
                                     textvariable=self.map_height)
        map_height_entry.grid(column=4, row=2, sticky=(W, E))

        self.room_min_width = IntVar(value=2)
        room_min_width_entry = ttk.Entry(mainframe,
                                         width=7,
                                         textvariable=self.room_min_width)
        room_min_width_entry.grid(column=2, row=3, sticky=(W, E))
        self.room_min_height = IntVar(value=2)
        room_min_height_entry = ttk.Entry(mainframe,
                                          width=7,
                                          textvariable=self.room_min_height)
        room_min_height_entry.grid(column=4, row=3, sticky=(W, E))

        self.room_max_width = IntVar(value=5)
        room_max_width_entry = ttk.Entry(mainframe,
                                         width=7,
                                         textvariable=self.room_max_width)
        room_max_width_entry.grid(column=2, row=4, sticky=(W, E))
        self.room_max_height = IntVar(value=5)
        room_max_height_entry = ttk.Entry(mainframe,
                                          width=7,
                                          textvariable=self.room_max_height)
        room_max_height_entry.grid(column=4, row=4, sticky=(W, E))

        self.loop_probability = DoubleVar(value=0.50)
        loop_probability_scale = ttk.Scale(scaleframe,
                                           orient=HORIZONTAL,
                                           length=200,
                                           from_=0.0,
                                           to=1.0,
                                           variable=self.loop_probability)
        loop_probability_scale.grid(column=3, row=1, sticky=(W, E))

        # ENTRY LABELS
        cell_dimensions_label = ttk.Label(mainframe, text="Square width and height")
        cell_dimensions_label.grid(column=1, row=1)

        map_dimensions_label = ttk.Label(mainframe, text="Map dimensions")
        map_dimensions_label.grid(column=1, row=2)

        room_min_dimensions_label = ttk.Label(mainframe, text="Room min dimensions")
        room_min_dimensions_label.grid(column=1, row=3)

        room_max_dimensions_label = ttk.Label(mainframe, text="Room max dimensions")
        room_max_dimensions_label.grid(column=1, row=4)

        loop_probability_label = ttk.Label(scaleframe, text="Likelihood of loops")
        loop_probability_label.grid(column=1, row=1)

        # DIVIDER LABELS
        map_dimensions_divider = ttk.Label(mainframe, text="x")
        map_dimensions_divider.grid(column=3, row=2)

        room_min_dimensions_divider = ttk.Label(mainframe, text="x")
        room_min_dimensions_divider.grid(column=3, row=3)

        room_max_dimensions_divider = ttk.Label(mainframe, text="x")
        room_max_dimensions_divider.grid(column=3, row=4)

        # UNIT LABELS
        cell_dimensions_unit = ttk.Label(mainframe, text="px")
        cell_dimensions_unit.grid(column=3, row=1)

        map_dimensions_unit = ttk.Label(mainframe, text="squares")
        map_dimensions_unit.grid(column=5, row=2)

        room_min_dimensions_unit = ttk.Label(mainframe, text="squares")
        room_min_dimensions_unit.grid(column=5, row=3)

        room_max_dimensions_unit = ttk.Label(mainframe, text="squares")
        room_max_dimensions_unit.grid(column=5, row=4)

        loop_probability_unit_left = ttk.Label(scaleframe, text="None")
        loop_probability_unit_left.grid(column=2, row=1)

        loop_probability_unit_right = ttk.Label(scaleframe, text="All")
        loop_probability_unit_right.grid(column=4, row=1)

        # SCALE VALUES
        loop_probability_value = ttk.Label(scaleframe, textvariable=self.loop_probability)
        loop_probability_value.grid(column=3, row=2)

        # BUTTONS
        generate_button = ttk.Button(buttonframe,
                                     text="Generate dungeon",
                                     command=self.validate_and_start)
        generate_button.grid(column=1, row=1)

        # ERROR MESSAGES
        self.error_message = StringVar()
        error_message_label = ttk.Label(errorframe,
                                        textvariable=self.error_message,
                                        foreground="red")
        error_message_label.grid(column=1, row=1)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        for child in scaleframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        root.mainloop()

    def validate_and_start(self):
        """Validate user inputs and start if they're correct"""
        try:
            cell_dimensions = self.cell_dimensions.get()
        except TclError as error:
            self.error_message.set(f"Square width and height: {error}")
        try:
            map_width = self.map_width.get()
            map_height = self.map_height.get()
        except TclError as error:
            self.error_message.set(f"Map dimensions: {error}")
        try:
            room_min_width = self.room_min_width.get()
            room_min_height = self.room_min_height.get()
        except TclError as error:
            self.error_message.set(f"Room min dimensions: {error}")
        try:
            room_max_width = self.room_max_width.get()
            room_max_height = self.room_max_height.get()
        except TclError as error:
            self.error_message.set(f"Room max dimensions: {error}")
        try:
            odds_of_loops = self.loop_probability.get()
        except TclError as error:
            self.error_message.set(f"Likelihood of loops: {error}")
        self.error_message.set("")
        self._start_generation(cell_dimensions,
                               map_width,
                               map_height,
                               room_min_width,
                               room_min_height,
                               room_max_width,
                               room_max_height,
                               100, # Temporary, waiting for the GUI setting
                               odds_of_loops)

    def _start_generation(self, cell_dim, map_w, map_h, room_min_w, room_min_h, room_max_w, room_max_h, room_gen_attempts, loop_odds):
        """Start the generation of the dungeon

        Args:
            cell_dim: The width and height of a cell will share the same value
            map_w: The width of the map in squares
            map_h: The height of the map in squares
            room_min_w: The minimum width of a room in squares
            room_min_h: The minimum height of a room in squares
            room_max_w: The maximum width of a room in squares
            room_max_h: The maximum height of a room in squares
            room_gen_attempts: How many rooms will the program attempt to generate
            loop_odds: The likelihood of loops in the dungeon, i.e. the imperfectness of the maze
        """
        map_obj = Map(map_w, map_h)
        room_gen = RoomGenerationService(cell_dim, cell_dim, map_w, map_h)
        room_gen.generate_random_rooms(room_gen_attempts,
                                       room_min_w,
                                       room_max_w,
                                       room_min_h,
                                       room_max_h)
        drawing = DrawingService(room_gen, map_obj, (cell_dim, cell_dim))
        drawing.draw_rooms()
        maze_gen = MazeGenerationService(map_obj)
        maze_gen.init_maze()
        maze_gen.generate_perfect_maze()
        maze_gen.connect_maze_to_rooms(loop_odds)
        maze_gen.prune_dead_ends()
        drawing.draw_corridors()
        drawing.draw_grid()
        MapRepository(drawing.get_image()).save("demo/test")
