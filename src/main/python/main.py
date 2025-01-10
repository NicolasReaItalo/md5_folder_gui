from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2 import QtWidgets
from PySide2.QtCore import QObject, QThread, Signal


import hashlib
import os
from pathlib import Path
import sys

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class StartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.dir_path = ''
        # Widgets
        self.folder_button =  QtWidgets.QPushButton("Choose folder")
        self.folder_button.clicked.connect(self.choose_folder)


        self.console = QtWidgets.QPlainTextEdit()
        self.console.resize(600,600)

        self.start_button = QtWidgets.QPushButton("Start")
        self.start_button.clicked.connect(self.start)

        #layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.folder_button)
        self.main_layout.addWidget(self.console)
        self.main_layout.addWidget(self.start_button)

        # window setup
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)
        self.resize(700,700)
        self.setWindowTitle("🇨🇭🧀 Calcul de checksum pour la Cinémathèque suisse 🧀🇨🇭")

    def print_to_console(self,text):
        self.console.appendPlainText(f"{text}\n")

    def choose_folder(self):
        self.dir_path = QtWidgets.QFileDialog.getExistingDirectory(self,"Choose Directory")
        print(self.dir_path)
        print(type(self.dir_path))

    def start(self):
        if self.dir_path == '':
            QtWidgets.QMessageBox.about(self, "Error", "You must choose a direcyory")
            return
        else:
            self.scan_folder(self.dir_path)

    def scan_folder(self, folder_path):
        file_count = 0
        current_file = 1
        folder = Path(folder_path)
        report_path = folder / "md5_report.md5"
        if report_path.exists():
            os.remove(report_path.absolute())

        if not folder.is_dir():
            return
        a = folder.iterdir()
        for element in a:
            if not element.is_dir():
                file_count += 1

        self.print_to_console(f"STARTING CHECKSUM ON FOLDER : {folder.name} \n {file_count} files to calculate"
                              f"\n #################################################################")
        for file in sorted(folder.iterdir()):
            if not file.is_dir():
                analysis = f"{file.name} {md5(file.absolute())} "
                self.print_to_console(f"file {current_file}/{file_count} --> {analysis}")
                if current_file < file_count:
                    self.print_to_console("still in progress...")
                current_file += 1
                with report_path.open('a') as fp:
                    fp.write(f"{analysis}\n")
                QtWidgets.QApplication.processEvents()
        self.print_to_console("😃😃 Done 😃😃")




if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    stylesheet = appctxt.get_resource('style.qss')
    appctxt.app.setStyleSheet(open(stylesheet).read())
    window = StartWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
