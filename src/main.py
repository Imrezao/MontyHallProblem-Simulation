import random
from typing import Tuple


def montyhaal(switch: bool) -> bool:
    """
    Simulate a single round of the Monty Hall problem.
    """
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)

    initial_door = random.choice(range(3))

    reveald_doors = [i for i in range(3) if i != initial_door and doors[i] != 'car']
    reveald_door = random.choice(reveald_doors)

    if switch:
        final_door = [i for i in range(3) if i != reveald_door and i != initial_door][0]
    else:
        final_door = initial_door     

    return doors[final_door] == 'car'    


def counter(num: int) -> Tuple :
    """
    Run multiple Monty Hall simulations and count wins for each strategy.
    """
    num_with_switching = sum([montyhaal(True) for _ in range(num)])
    num_no_switching = sum([montyhaal(False) for _ in range(num)])

    return num_with_switching, num_no_switching
  

if __name__ == '__main__':
    num = 1000
    num_with_switching, num_no_switching = counter(num)
    print(f"Winning percentage without switching doors: {(num_with_switching/num):.2%}")
    print(f"Winning percentage with    switching doors: {(num_no_switching/num):.2%}")
