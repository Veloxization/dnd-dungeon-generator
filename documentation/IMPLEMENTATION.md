# Implementation document
## Core functionality in steps
1. Create a Map object of user-specified dimensions
2. Try to place as many rooms of user-specified dimensions as possible to the map. A room is not placed if it would go on top of another room or extends beyond the edges of the dungeon.
3. Start drawing the graphical representation of the map, drawing all the rooms placed in the previous step
4. Create an empty MazeGenerationService object, which is aware of the rooms placed in the previous step
5. Initialize MazeGenerationService by marking the cells that have **r**ooms as 'r', the cells surrounding the rooms as 'w' for **w**alls and all other cells as 'u' for **u**nvisited
6. Generate a perfect maze, filling the entirety of the available space between the rooms, utilizing randomized Prim's algorithm that starts generating new mazes on each available **u**nvisited cell
    - The generated **p**assages are marked as 'p' and surrounded by **w**alls
7. Connect the generated maze to the rooms, and the rooms to each other. All rooms have only one entrance and exit, unless a pseudorandom number [0, 1[ is less than the *odds\_of\_loops* variable at each possible additional entrance
8. All dead ends of the maze are pruned utilizing depth-first search, leaving winding corridors between the different rooms
9. The added corridors are drawn on the graphical representation of the map
10. A grid is drawn on top of the graphical representation of the map to make it easier to navigate in a tabletop setting
11. Numbers are placed in the top left corner of the rooms in order of generation
12. The generated graphical representation is saved as a PNG image
13. The Game Master's document is saved as a text file alongside the image