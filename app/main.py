'''
    bootstrap 入口程序
'''
from PySide6.QtWidgets import QApplication, QMessageBox;
from app.bootstrap import Bootstrap;

def main():
    app = QApplication();
    bootstrap = Bootstrap();
    bootstrap.run();
    app.exec();



    