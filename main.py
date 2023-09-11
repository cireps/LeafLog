import time
from datetime import datetime
import pandas as pd
from PyQt6 import  QtWidgets, QtGui, uic, QtCore
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys
from model import Model
import csv

#Task object
class Task:
    def __init__(self, name, details, time):
        self.name = name
        self.details = details
        self.time = time
    
    def new_task(name, details) -> object:
        task = Task(name=name, details=details, time=Task.timestamp())
        return task

    #returns timestamp including the time of day
    def timestamp():
        unix_current_time = int(time.time())
        date_time = datetime.fromtimestamp(unix_current_time)
        formatted_date = date_time.strftime('%d/%m/%Y')
        day_of_week = date_time.strftime('%A')
        time_of_day = date_time.strftime('%H:%M')
        date_tag = f'{day_of_week}, {formatted_date}, {time_of_day}'
        return date_tag
    
    #returns the day of the week and date
    def date():
        unix_current_time = int(time.time())
        date_time = datetime.fromtimestamp(unix_current_time)
        formatted_date = date_time.strftime('%d/%m/%Y')
        day_of_week = date_time.strftime('%A')
        date_tag = f'{day_of_week}, {formatted_date}'
        return date_tag
        
#adds Tasks object properties to the model
class ToDo():       
    def add_todo(task):
        Model.tasks['Name'].append(task.name)
        Model.tasks['Details'].append(task.details)
        Model.tasks['Time'].append(task.time)

    #saves the contents of the model to the save_data.log file
    def save_data():
        try:
            df = pd.DataFrame(Model.tasks)
            df.to_csv(Model.save_file_path, index=False)
            print("File Saved")
        except:
            print("Save Failed")

    #loads the data from the save_data.log file into the model
    def load_data():
        try:
            with open(Model.save_file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    for key, value in row.items():
                        Model.tasks[key].append(value)
            
            print("Save Loaded")
        except:
            print("Load Save Failed")
            
        
class View(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./gui/tasks.ui', self) 
        self.initUi()

    #creates a new to-do by creating a task item using the text store in name and description boxes in the gui
    def create_task(self):
        self.lineEdit_2.clear()
        name = self.lineEdit.text()
        details = self.plainTextEdit.toPlainText() 
        ToDo.add_todo(task=Task.new_task(name=name, details=details))
        self.listWidget.addItem(Model.tasks['Name'][-1])
        self.clear_all()
        
    #gets data from the model with the index value of the item selected in the gui
    def on_index_changed(self):
        try:
            index = self.listWidget.currentRow()
            details = Model.tasks['Details'][index]
            name = Model.tasks['Name'][index]
            time = Model.tasks['Time'][index]
            self.clear_all()
            self.lineEdit.insert(name)
            self.lineEdit_2.insert(time)
            self.plainTextEdit.insertPlainText(details)
        except:
            print("error")

    #clear the field task name and description fields in the gui
    def clear_all(self):
        self.lineEdit_2.clear()
        self.plainTextEdit.clear()
        self.lineEdit.clear()

    #deletes a task item from the gui and the model using the index value of the selected item
    def delete_task(self):
        index = self.listWidget.currentRow()
        try:
            if(index == -1):
                self.clear_all()
                pass
            self.listWidget.takeItem(index)
            del Model.tasks['Name'][index]
            del Model.tasks['Details'][index]
            del Model.tasks['Time'][index]
        except:
              print("error")

    #loads the name data into the view from the model, this is done when the application first starts
    def load_view_from_save(self):
        try:
            for item in Model.tasks['Name']:
                self.listWidget.addItem(item)
            print("View loaded")
        except:
            print("Load Failed")
            
    #detects left mouse click and position, mousePressEvent and MoveWindow are responsible for the GUI's title bar to be relocated and moved       
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.offset = event.position()

    def MoveWindow(self, event):
        if self.offset is not None and event.buttons() == Qt.MouseButton.LeftButton:
            new_pos = event.globalPosition() - self.offset
            self.move(new_pos.toPoint())

    #the css styles associated with the gui
    def styles(self):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(660, 375)
        self.setStyleSheet("""
                           QMainWindow { 
                           background-color: #1A1D1A; 
                           }
                           """)
        self.icon.setStyleSheet("""
                                background: transparent;
                                """)
        self.title_txt.setStyleSheet("""
                                    background: transparent;
                                    border: none;
                                    color: white;
                                    font-family: Terminal;
                                    font-size: 10px;
                                     """)
        self.min_btn.setStyleSheet("""
                                    background: transparent;
                                    border: none;
                                    font-family: Terminal;
                                    font-size: 9px;
                                   """)
        self.close_btn.setStyleSheet("""
                                    background: transparent;
                                    border: none;
                                    font-family: Terminal;
                                    font-size: 9px;
                                   """)
        self.frame.setStyleSheet("""
                                    background-color: transparent;
                                 """)
        self.delete_button.setStyleSheet(Model.button_styling)
        self.clear_button.setStyleSheet(Model.button_styling)
        self.create_button.setStyleSheet(Model.button_styling)
        self.date_time_lin.setStyleSheet("""
                                        background-color: #252925;
                                        color: #979797;
                                        border: none;
                                        padding: 5 5 5 5;
                                        border-radius: 10px;
                                        font-family: Terminal;
                                        font-size: 9px;
                                         """)
        self.listWidget.setStyleSheet("""
                                      background-color: #252925;
                                      color: white;
                                      border: none;
                                      padding: 5 5 5 5;
                                      border-radius: 5px;
                                      font-family: Terminal;
                                      font-size: 9px;
                                      """)
        self.lineEdit.setStyleSheet("""
                                    color: white;
                                    border: none;
                                    background-color: #252925;
                                    padding: 0 0 0 3;
                                    border-radius: 5px;
                                    font-family: Terminal;
                                    font-size: 9px;
                                    """)
        self.lineEdit_2.setStyleSheet("""
                                    color: white;
                                    border: none;
                                    background-color: #252925;
                                    padding: 0 0 0 3;
                                    border-radius: 5px;
                                    font-family: Terminal;
                                    font-size: 9px;
                                    """)
        self.plainTextEdit.setStyleSheet("""
                                    color: white;
                                    border: none;
                                    background-color: #252925;
                                    padding: 0 3 0 3;
                                    border-radius: 5px;
                                    font-family: Terminal;
                                    font-size: 9px;
                                    """)
        try:
            self.setWindowIcon(QIcon('./gui/icons/icon.png'))
        except:
            print('No icon found')
    
    #inititalizing commands store in a function for better organization 
    def initUi(self):
        self.create_button.clicked.connect(self.create_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.clear_button.clicked.connect(self.clear_all)
        self.date_time_lin.insert(Task.date())
        self.date_time_lin.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.close_btn.clicked.connect(lambda: app.exit())
        self.min_btn.clicked.connect(lambda: self.showMinimized())
        self.listWidget.currentItemChanged.connect(self.on_index_changed)
        self.listWidget.clicked.connect(self.on_index_changed)
        self.frame.mouseMoveEvent = self.MoveWindow
        self.styles()
        self.load_view_from_save()
        
#runs the main method, loads save, creates app, shows view, and on exit stores the model data into the save_data.log   
if __name__ == '__main__':
    ToDo.load_data()
    app = QApplication(sys.argv)
    view = View()
    view.show()
    app.exec()
    ToDo.save_data()

