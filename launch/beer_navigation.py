import subprocess

launch_files = [
    "path/to/launchfile1.launch.py",
    "path/to/launchfile2.launch.py",
    "path/to/launchfile3.launch.py"
]

for launch_file in launch_files:
    subprocess.Popen(["roslaunch", launch_file])

