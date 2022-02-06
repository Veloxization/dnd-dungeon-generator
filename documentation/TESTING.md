# Testing document
This program has been automatically tested using pytest. Always up-to-date testing coverage percentage is available in the [README](https://github.com/Veloxization/dnd-dungeon-generator/blob/master/README.md). Instructions on running the tests and creating the complete coverage report in [MANUAL](https://github.com/Veloxization/dnd-dungeon-generator/blob/main/documentation/MANUAL.md).

## Coverage report
<img src="https://github.com/Veloxization/dnd-dungeon-generator/blob/master/documentation/images/coveragereport.png">

## What has been tested?
### entities/map
- The constructor assigns the map's height and width correctly
    - Tested with width of 10 and height of 20
- Corners have only two neighbours
    - Tested with the top left corner
- Edges have only three neighbours
    - Tested with the top edge
- Other cells have four neighbours
    - Tested with the cell in coordinates (1,1)
- When a cell is marked occupied, its status changes correctly
    - Tested by changing the status of the top left corner
- When a cell is marked unoccupied, its status changes correctly
    - Tested by changing the status of the top left corner
- When a cell is unoccupied and it's changed to occupied, thet status changes correctly
    - Tested by changing the status of the top left corner to unoccupied and then occupied
- When a cell is marked occupied, the adjacent cells are marked with an adjacent occupied cell
    - Tested by changing the top left corner's status to occupied and then checking the status of the cell below it
- When a cell has an adjacent occupied cell, it can also become occupied
    - Tested by occupying the top left corner and checking if the cell below it also becomes occupied when changed
- When a cell is occupied, it can't be marked as having an adjacent occupied cell
    - Tested by first occupying the top left corner, then occupying the cell below it and checking that the top left corner's status does not change
- When a cell has one or less neighbours, it is considered a dead end
    - Tested by occupying cells (1,1) and (1,2), then checking that (1,2) is considered a dead end
- When a cell has more than one neighbour, it is not considered a dead end
    - Tested by occupying cells (1,1), (1,2) and (2,1) and checking that (1,1) is not considered a dead end
### services/drawing_service
- When a room's right edge extends beyond the right edge of the map, it's not drawn
    - Tested by drawing a 2x2 room to coordinates (49,1) on a 50x50 map and checking that it can't be drawn
- When a room's bottom edge extends beyond the bottom edge of the map, it's not drawn
    - Tested by drawing a 2x2 room to coordinates (1,49) and checking that it can't be drawn
- When an attempt is made to draw a room on top of an existing room, it fails
    - Tested by drawing 2x2 rooms to coordinates (1,1) and (2,2) and checking that the latter is not generated
- A room can be drawn on an unoccupied space
    - Tested by drawing a 2x2 room to coordinates (1,1)
- A cell's coordinates are converted to pixel coordinates correctly
    - Tested by checking that with 20x20-pixel cells, the given coordinates for cell (1,1) are given as (20,20)
- A valid room will be drawn on the map image
    - Tested by checking that a mock object's room drawing function is called when attempting to draw a 2x2 room at coordinates (1,1)
- An invalid room will not be drawn on the map image
    - Tested by checking that a mock object's room drawing function is not called when attempting to draw a 2x2 room at coordinates(1,49)
- The movement grid is drawn with the correct line thickness
    - Tested by checking that a mock object's grid drawing function is called with the correct line thickness of 2
- When trying to get the map image object, the function of the image generation service is called correctly
    - Tested by checking that a mock object's generated image getter function is called
### services/maze_generation_service
- When a maze is initialized, the rooms added on the map will appear in the maze surrounded by walls
    - Tested by checking that a room generated at coordinates (1,1) will also be marked at coordinates (1,1) and all the adjacent cells are marked as walls
- When a wall is added, it's correctly reflected in the maze cells
    - Tested by checking that the cell at (1,1) changes to a wall when it's added there
- When a passage is added, it's correctly reflected in the maze cells and surrounded by walls
    - Tested by checking that the cell at (1,1) changes into a passage when added, and that the adjacent cells are turned into walls
- Once a passage is placed, it cannot be replaced by a wall
    - Tested by placing a passage at (1,1) and trying to change the same cell into a wall
- Once a wall is placed, it can be replace by a passage
    - Tested by placing a wall at (1,1) and trying to replace it with a passage, making sure that the wall is removed from the list of walls
- The amount of non-diagnonally adjacent passages is calculated correctly
    - Tested by placing new passages around a certain point and checking that the amount increases accordingly
- When looking for a starting cell for a maze, it's correctly found
    - Tested with a maze filled with walls and cell (5,5) replaced by an unvisited marker, then checking that its coordinates are found correctly
- When there are no valid starting points, the starting point searching function returns _None_
    - Tested with a maze filled with walls and checking that the starting point searching function returns _None_
- When a full maze is generated, no passages will override an already placed room
    - Tested by occupying cell (2,2) and having that act as a room, then checking that a generated maze does not replace this cell
### services/room_generation_service
- When a room is added, it's correctly added into the list of rooms
    - Tested by generating a room in coordinates (1,2) with the width of 3 and height of 4, and checking that it's added to a list of rooms
