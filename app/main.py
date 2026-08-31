'''
    bootstrap 入口程序
'''
import sys;
from PySide6.QtWidgets import QApplication, QMessageBox;
from app.bootstrap import Bootstrap;

def main():
    app = QApplication( sys.argv );
    bootstrap = Bootstrap();
    bootstrap.run();
    return app.exec();

if __name__ == "__main__":
    sys.exit( main() );