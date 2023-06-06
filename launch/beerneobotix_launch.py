import subprocess

launch_files = [
    "neo_mpo_500-2 bringup.launch.py",
    "neo_mpo_500-2 navigation.launch.py",
    "neo_nav2_bringup rviz_launch.py"
]

for launch_file in launch_files:
    subprocess.Popen(["ros2", "launch", launch_file])

