# User manual
## Starting up
Once you've downloaded the files in this repository, follow these steps:
1. Install Poetry by the instructions [here](https://python-poetry.org/docs/#installation)
2. Navigate into the root directory of the project and run the following command
    - `poetry install`
## Usage
To make usage easier, tasks have been implemented to automatically run the key functionalities. More detailed usage is possible by following the instructions in [Poetry documentation](https://python-poetry.org/docs/).
### Run pytest
`poetry run invoke test`

All the implemented tests will be run.
### Generate a coverage report
`poetry run invoke coverage-report`

Generates the coverage report in-terminal. A directory called *htmlcov* is also generated in the root directory. By opening *index.html* within that folder, you get a more user-friendly coverage report.
### Code style check
`poetry run invoke lint`
### Demo the current version of the program
`poetry run invoke demo`

Currently the program only replaces the file within *demo/test.png* but future versions will do more.