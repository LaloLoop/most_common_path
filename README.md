# Most common path challenge

## Objective

To find the most common path for a user status change from different statuses in a given transaction log.

## Restrictions

To obtain a path, the user should have 3 different states on his journey.

## Example

If a user starts on the state A, then go to state B, then move forward to state C and finalize with state D. Then the 
user creates two different paths:

1. A->B->C
2. B->C->D

Input format: `[<userId>,<stateId>]`

## How to run this code

#### Main code

The main code has a sample test case hardcoded as an example of the functionality. It can be executed with the following 
command:

```shell script
python main.py
```

#### Unit tests

You can find test cases within the `test_most_common_path.py` file. The easiest way to run this is with the following 
command:

```shell script
python -m unittest
```

## Improvements

There are some edge cases that are not considered:

1. What happens if a user can somehow edit the path and add a new state in between (not an append only log)?
2. What happens if the user id or state id change to something other than number and letters? The current implementation 
may not be the best option memory wise.

## Another implementation

Another implementation could be achieved with a different data structure, like a weighted graph and the traversal on the
graph could help find out the different common paths.
