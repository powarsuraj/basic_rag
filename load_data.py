
from pathlib import Path

file_path = Path("data/dummy_hr_policy_data.txt")

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

print(text[:1000])
print("\nFile loaded successfully!")