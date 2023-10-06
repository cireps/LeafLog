# LeafLog

A simple and elegant task manager application built using Python and PyQt6.

### Features:

- **Add Tasks**: Quickly add tasks with a name, details, and timestamp.
- **View Tasks**: Tasks are displayed in a user-friendly interface with the ability to select them to view more details.
- **Delete Tasks**: Easily remove tasks from the list.
- **Data Persistence**: Tasks are saved to and loaded from a local CSV file, ensuring that your task data remains consistent across sessions.
- **Custom Design**: Features a frameless custom-styled GUI that can be moved around.

### Dependencies:

- PyQt6
- pandas
- csv
- time

### Usage:

1. Ensure you have the required dependencies installed.
2. Run the main Python script.
3. Use the GUI to create, view, and manage tasks.

### Structure:

- **Model class**: Contains the main data structure and styling for the application.
- **Task class**: Represents a task with properties like name, details, and timestamp.
- **ToDo class**: Contains methods to manipulate tasks like add, save, and load.
- **View class**: The main GUI class, with methods to manage and display tasks.

### Quick-start:

Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/cireps/LeafLog.git

```
Run the script:
```bash
python main.py
```

### Notes:
- Ensure you have the `./gui/tasks.ui` file and the `./gui/icons/icon.png` in the correct directories relative to the script.
- The tasks are saved in the `./save_data/save_data.log` file as a CSV.

### Contributions:
Contributions are welcome! Please open an issue or submit a pull request.

---

Developed by Eric Polanco
