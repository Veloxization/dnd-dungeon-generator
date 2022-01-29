# User story document
This personal document serves as a way to prioritise different parts of the project. The higher a feature is on the list, the more likely it will be developed.

## Legend
**(U)**ndone

**(S)**tarted

**(D)**one

**(I)**nterrupted

## Definition of "Done"
The feature has to be developed as specified in this document and have a reasonable test coverage (i.e. important parts are tested, not getters and setters etc.)

## User stories
- The program can generate a movement grid **(S)**
- The program can generate rooms of various sizes **(S)**
- The program can generate hallways **(U)**
- The hallways are reasonably connected to the rooms **(U)**
- The user can specify the size of the dungeon **(U)**
    - The required GUI element **(U)**
- The user can specify the likelyhood of loops (the "imperfectness" of the maze) **(U)**
    - The required GUI element **(U)**
- The user can specify the average size of rooms **(U)**
    - The required GUI element **(U)**
- The program numbers the rooms **(U)**
    - Generated text file with room numbers and empty details **(U)**
- The user can specify the descriptions of different rooms **(U)**
    - The required GUI element **(U)**
- The user can specify loot tables that can appear in different rooms **(U)**
    - The loot tables appear under the room number in the generated text document **(U)**
    - The required GUI element **(U)**
- The user can specify the enemies that can appear in different rooms **(U)**
    - The enemies appear under the room number in the generated text document **(U)**
    - The required GUI element **(U)**
- The user can specify the puzzles that can appear in different rooms **(U)**
    - Miscellaneous puzzles (no special generation required) **(U)**
    - The puzzles appear under the room number in the generated text document **(U)**
    - The required GUI element **(U)**
- The user can specify the importance level of different loot tables **(U)**
- The user can specify the importance level of different enemy spawns **(U)**
- More puzzle types
    - Door puzzles
        - A locked door graphic appears on the map **(U)**
    - Loot puzzles
        - A loot table with the highest available priority is placed under this room in the text document **(U)**
- The user can manually specify the description of a specific room from withing the program **(U)**
    - The required GUI element **(U)**
- The user can manually specify the loot that appears within a specific room from within the program **(U)**
    - The required GUI element **(U)**
- The user can manually specify the enemies that appear within a specific room from within the program **(U)**
    - The required GUI element **(U)**
- The user can manually specify the puzzle that appears within a specific room from within the program **(U)**
    - A locked door graphic appears at one of the exits of a door puzzle room **(U)**
    - A room with a loot puzzle must have a loot table specified **(U)**
    - The required GUI element **(U)**