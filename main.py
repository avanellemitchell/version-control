from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("../version.md", "w") as f:
    f.write(f"Last updated: {current_time}\n")

print("version.md updated successfully!")

