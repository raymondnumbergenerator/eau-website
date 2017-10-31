# eau-website

## Requirements
- virtualenvironment
- Python 3

If you don't have python3 or virtualenvironment run `pip install venv` and `brew install python3`.

If you don't have pip or brew just do some Googling to figure it out.

## Development Setup

1. Fork this repository and clone your fork.
2. Add this repository as the upstream remote with `git remote add upstream <URL for this repository>`.

## First-time setup
1. `cd` into the directory and set up the virtual environment with `virtualenv -p python3 venv`.
2. Activate the virtual environment with `source venv/bin/activate`.
3. `pip install -r requirements.txt`.

## Running the website
1. Make sure you're in the virtual environment. If not, run `source venv/bin/activate`.
2. `python run.py` to start the website.

## Workflow

#### Keeping your fork updated
1. `git fetch upstream` to fetch changes from this repository.
2. `git checkout master` to switch back to your master branch.
3. `git merge upstream/master` to merge changes from this repository to your fork.

#### Making changes
1. Make a new branch for the feature you are working on with `git checkout -b feature`.
2. Make all your changes on this branch.
3. Update your fork with `git fetch upstream` and `git rebase upstream/master`.
4. Push your changes to your fork with `git push origin feature`.
5. Make a pull request using the `feature` branch.
