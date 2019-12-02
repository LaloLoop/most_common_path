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

