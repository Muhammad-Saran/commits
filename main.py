import os
import subprocess
from datetime import datetime, timedelta
import random

# Initial setup
start_date = datetime(2024, 4, 1)
end_date = datetime(2024, 10, 22)
file_name = "dummy.txt"

# Create a dummy file if it does not exist
if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        f.write("Initial content")

# Set the probability to skip (40%)
skip_probability = 0.2

# Iterate over each date from start_date to end_date
current_date = start_date
while current_date <= end_date:
    # Decide randomly whether to skip this date
    if random.random() > skip_probability:
        # Modify the file to make each commit unique
        with open(file_name, "a") as f:
            f.write(f"Commit on {current_date.strftime('%Y-%m-%d')}\n")

        # Format the date for the commit
        date_str = current_date.strftime('%Y-%m-%dT12:00:00')

        # Run the git commit command with the specific date
        subprocess.run(["git", "add", file_name])
        subprocess.run(["git", "commit", "--date", date_str, "-m", "dump"])

    # Move to the next day
    current_date += timedelta(days=1)
