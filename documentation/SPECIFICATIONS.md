# Specifications' document
## The intended problem to be solved
Easily generating randomized dungeons for Dungeons & Dragons homebrew campaigns with monsters, loot and puzzles specified by the dungeon master.
## Programming language used
Python
## Other programming languages I'm capable in
Java, C#, web development languages like HTML and JavaScript
## Intended algorithm and data structure
A modified randomized Prim's algorithm to generate hallways between pseudorandomly placed rooms, adjacency lists to list the connections of a single cell to other adjacent cells.
Depth-first search to prune dead ends out of the generated maze, leaving winding hallways.
## Inputs and their usage
The user can specify what kind of monsters, loot and puzzles will be featured in the generated dungeon. The user can also add flavor text or descriptions to different rooms in an already generated dungeon. These will all be saved into a separate document for future referral.

The user can specify the likelihood of dead ends in the dungeon, i.e., how likely it is that a single room in the dungeon has only one entrance and exit. Normally Prim's algorithm creates a perfect maze with only one solution but that creates quite boring dungeons so letting the user control this aspect is important.
## Goal time complexity
The time complexity of depth-first search is O(n), while Prim's algorithm utilizing adjacency lists has the time complexity of O(n<sup>2</sup>). Hence the goal time complexity is O(n<sup>2</sup>).
## Goal space complexity
O(n) as the generated dungeon will only feature a specified number (width x height) of cells.
## Sources
[Idea](https://journal.stuffwithstuff.com/2014/12/21/rooms-and-mazes/)

[Time complexity of Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm#Time_complexity)

[Maze generation with randomized Prim's algorithm](https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e)
## Curriculum
Bachelor's in computer science (Tietojenkäsittelytieteen kandidaatti, TKT)
## Language used in documentation
English