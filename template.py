import os
from pathlib import Path

list_of_files = [
     ".env",
     ".env.example",
     "requirements.txt",
     "src/__init__.py",
     "src/create_sql_db.py",
     "src/helpers.py",
     "src/config/__init__.py",
     "src/config/config.py",
     "database/__init__.py",
     "frontend.py"
]


for filepath in list_of_files:
     filepath = Path(filepath)
     filedir, filename = os.path.split(filepath)
     if filedir != "":
          os.makedirs(filedir, exist_ok=True)
     if not os.path.exists(filepath):
          with open(filepath, "w") as f:
               pass
     else:
          print(f"The file {filepath} already exists.")