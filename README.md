# COMP7010 Assignement 2
## Randomized Algorithms: Random Quicksort, Random Select, Karger's Min Cut
#### David Costa | 10/6/2026

1. To run tests and verifications, first clone this repository into your desired directory using `git clone https://github.com/costad3atwit/COMP7010_A2.git` 
2. cd to the local repository and setup a python virtual environment with `python -m venv venv`
3. Source the activate script with `source venv/bin/activate` (on linux), then run `pip install pytest`
4. Finally run tests with `pytest a1.py -s`
    1. The -s here ensures that print statements aren't captured by pytest, that way you can see the actual comparison counts and trial counts for part B

Test output will be in your terminal and pytests for all 3 algorithms should pass.
If you wish to duplicate the inputs used to gather my timings ensure that the seed in line 4 is set to 1234: `random.seed(1234)`
