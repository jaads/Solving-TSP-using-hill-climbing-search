# Solving Traveling-salesman problem using simple hill-climbing search
This project is about finding a solution to the traveling-salesman problem (TSP) using a so called **goal-based AI agent**. 
The goal is to find a cycle (a roundtrip) which visits every city once, while traveling the minimal possible distance.

A search algorithm called **first-choice hill-climbing search** has been used, which is a algorithms from the family of **local search** algorithms.
This search evaluates and modifies one current state rather than systematically exploring paths from an initial state to a goal state, as it is done in classical search.
This path to reach the goal is not of interest. Thus, no data structure representing the search space needs to be maintained. 
Only the current node needs to record the state and the value of the objective function, here the distance.

The current sate is a sequence of cities along with the distance. 
The search creates new randomly sequences and checks if the new sequences has a shorter distance compared to the current sequence. 
As soon as any  shorter distance is found, take this as the new current state and repeat.
It resets the best sequence five times in total - every time after 2000 iterations. Hence it checks overall 10,000 sequences. 
The best sequence within all is the solution and is printed out to the command line in the end. 

An alternative version of the hill-climbing algorithm being used is called the **steepest-ascent version**.
# How to use
1. Install dependencies using `pip install -r requirements.txt`
2. Using Python 3 execute `Hill_climbing_simple.py` with a text file containing the cities with their coordinates like `python3 Hill_climbing_simple.py --filename data/49_cities.txt` assuming you are in the `src` directory.

# Properties of the task environment 
- Fully observable
- Single agent
- Stochastic
- Episodic
- Static
- Discrete
- Known

# Deliverables
* The final solution is printed at the end of a `log.*.txt` file in the `results` folder.
* Also a plot diagram will be created after search which visualizes the results of the algorithm. 
It's storeed in `results/plots/diagramm.*.png`. 
