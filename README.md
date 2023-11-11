# words-in-words
The new game where you get a revolutionary way to explore words inside other words!!1

All logics are coded using Python.

Some useful explanations to properly structure the repository.

.gitignore: This file is used to specify which files or folders should be ignored when making commits and pushing to GitHub. You should include patterns to ignore temporary files, automatically generated files, and anything else that should not be in the repository.
README.md: The README file is essential for documenting your repository. It provides information about the purpose of the repository, how to use it, and any other relevant information.
docs/: This folder can contain documentation related to your projects, such as manuals, tutorials, reports, and notes.
src/: Here are the source files of your projects. Each project should have its own folder to keep everything organized.
data/: This folder is useful for storing data used in your projects. Each project can have its own folder for specific data.
tests/: Contains the test files for your projects. Like with the other folders, each project should have its corresponding test folder.
scripts/: You can store useful scripts in this folder. This makes it easier to run automated tasks or custom commands.
assets/: This folder is suitable for images, graphics, or other visual resources used in your projects.
.github/workflows/: If you want to set up GitHub Actions to automate tasks, you can place the workflow files here.

# words-in-words

The purpose of this project is to host all the required code to make the logics and interaction related to a new game called words-in-words.

## Requirements

The project has the following requirements:

- Python 3.6 or higher
- Flask 2.0.1 or higher
- Jinja2 3.0.1 or higher

## Configuration

To configure the project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/words-in-words.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## How to Execute

To execute the project, follow these steps:

1. Navigate to the project directory: `cd words-in-words`
2. Run the Flask app: `flask run`

## Folder Structure

The folder structure of the project is as follows:

- `.gitignore`: This file is used to specify which files or folders should be ignored when making commits and pushing to GitHub. You should include patterns to ignore temporary files, automatically generated files, and anything else that should not be in the repository.
- `README.md`: The README file is essential for documenting your repository. It provides information about the purpose of the repository, how to use it, and any other relevant information.
- `docs/`: This folder can contain documentation related to your projects, such as manuals, tutorials, reports, and notes.
- `src/`: Here are the source files of your projects. Each project should have its own folder to keep everything organized.
- `data/`: This folder is useful for storing data used in your projects. Each project can have its own folder for specific data.
- `tests/`: Contains the test files for your projects. Like with the other folders, each project should have its corresponding test folder.
- `scripts/`: You can store useful scripts in this folder. This makes it easier to run automated tasks or custom commands.
- `assets/`: This folder is suitable for images, graphics, or other visual resources used in your projects.
- `.github/workflows/`: If you want to set up GitHub Actions to automate tasks, you can place the workflow files here.

## Useful tips

Use the command: 
'pip freeze > requirements.txt'
when located on the project repository, to automatically generate the requirements.txt doc containing all dependencies. 

