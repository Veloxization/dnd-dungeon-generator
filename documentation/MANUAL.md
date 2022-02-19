# User manual
## Starting up
Once you've downloaded the files in this repository, follow these steps:
1. Install Poetry by the instructions [here](https://python-poetry.org/docs/#installation)
2. Navigate into the root directory of the project and run the following command
    - `poetry install`
## Usage
To make usage easier, tasks have been implemented to automatically run the key functionalities. More detailed usage is possible by following the instructions in [Poetry documentation](https://python-poetry.org/docs/).
### Demo the current version of the program
`poetry run invoke demo`
### Run pytest
`poetry run invoke test`

All the implemented tests will be run.
### Generate a coverage report
`poetry run invoke coverage-report`

Generates the coverage report in-terminal. A directory called *htmlcov* is also generated in the root directory. By opening *index.html* within that directory, you get a more user-friendly coverage report.
### Code style check
`poetry run invoke lint`
## GUI
The GUI offers you various options for generating your dungeon. Be wary about inputting higher values as generating a large image can take a long time depending on your computer capabilities.
### Square width and height
How large one square on the generated map is, in pixels
### Map dimensions
The width and height of the map in squares
### Room min dimensions
The minimum width and height a single room on the map can take, in squares
### Room max dimensions
The maximum width and height a single room on the map can take, in squares
### Likelihood of loops
How likely is it that the generated dungeon contains loops. A likelihood of "None" means that there is only one way to move between two rooms, while a likelihood of "All" means all possible entrances to the room will be created.
### Generate dungeon button
Once you are happy with the settings, pressing this button will start the room generation. If you made any errors in the values you entered earlier, the program will tell about them now. The program may seem unresponsive during generation and will inform you once it's done.