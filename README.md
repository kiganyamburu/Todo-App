# Flask Todo App

A simple Todo application built with Flask, allowing users to add, update, and delete tasks.

## Features

- Add new tasks
- Mark tasks as complete/incomplete
- Edit and delete tasks
- Persistent storage with SQLite

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/flask-todo-app.git
    cd flask-todo-app
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**
    ```bash
    flask run
    ```

2. Open your browser and go to `http://127.0.0.1:5000/`

## Project Structure

```
flask-todo-app/
├── app.py
├── requirements.txt
├── templates/
│   └── ...
└── static/
     └── ...
```

## License

This project is licensed under the MIT License.

---

*Feel free to contribute or open issues!*