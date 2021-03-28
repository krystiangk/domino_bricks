# Domino Bricks

This is a small program simulating future and previous states <br> of falling domino bricks.

## Installation

Clone the repo to your local environment and then import domino_algorithm from domino module.


## Usage

```python
from domino import domino_algorithm

# Insert three parameters:
# - Raw string of domino bricks you want to simulate
# - Which option you want to test either "forward" or "backward"
# - Number of iterations to test 

domino_algorithm(r"|////|\\\||", "backward", 2) # returns '|//|||||\||'
domino_algorithm(r"||//||\||/\|", "forward", 1) # returns "||///\\||/\|"
```

