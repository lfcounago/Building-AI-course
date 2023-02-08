
import math
import random
import numpy as np
import io
from io import StringIO
import random

def main():
    prob = random.random()
    if prob < 0.1:
        favourite = "bats"
    if prob < 0.2 and prob > 0.1:
        favourite = "cats"
    if prob > 0.2:
        favourite = "dogs"
      # change this
    print("I love " + favourite) 


main()
  