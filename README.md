# Text-SQL-ChatBot

## Overview
Text-SQL-ChatBot is an intelligent chatbot application designed to interact with SQL databases using natural language. It allows users to query and manage their databases effortlessly by translating text-based inputs into SQL commands.

## Features
- **Natural Language Processing**: Converts user queries into SQL commands.
- **Database Management**: Supports querying, updating, and managing SQL databases.
- **User-Friendly Interface**: Simplifies database interactions for non-technical users.

## Project Structure
```
frontend.py          # Main application interface
LICENSE              # License information
README.md            # Project documentation
requirements.txt     # Python dependencies

template.py          # Template for project structure

database/            # Database files
    __init__.py
    students.db      # Example SQLite database

src/                 # Source code
    __init__.py
    create_sql_db.py # Script to create SQL databases
    helpers.py       # Helper functions
    config/          # Configuration files
        __init__.py
        config.py    # Application configuration
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MohammedHamza0/Text-SQL-ChatBot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Text-SQL-ChatBot
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the main application:
   ```bash
   streamlir run frontend.py
   ```
2. Interact with the chatbot to query or manage your SQL database.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your fork:
   ```bash
   git commit -m "Description of changes"
   git push origin feature-name
   ```
4. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
