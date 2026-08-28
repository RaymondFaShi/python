'''
    bootstrap 入口程序
'''
from PySide6.QtWidgets import QApplication, QMessageBox;
from app.bootstrap import Bootstrap;

def main():
    try:
        app = QApplication();
        bootstrap = Bootstrap();
        bootstrap.run();
        app.exec();
    except:
        print( '未知错误' );



    