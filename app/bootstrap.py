'''
    启动程序
'''
from PySide6.QtWidgets import QMessageBox;
from PySide6.QtUiTools import QUiLoader;
from pathlib import Path;
from app.calculator import Calculator;

class Bootstrap:

    # 主窗口
    mainWindow = None;

    calculator = None;

    # construct
    def __init__( self ):
        # ui路径
        uiFilePath =  Path(__file__).resolve().parent/ "calculator.ui";
        # print( uiFilePath );
        # 载入ui文件
        self.mainWindow = QUiLoader().load( uiFilePath );

        # previewLabel调整
        self.mainWindow.previewLabel.setStyleSheet(
            '''
                #previewLabel {
                    margin-left: 10px;
                    margin-right: 10px;
                }
            '''
        );

        # resultLabel调整
        self.mainWindow.resultLabel.setStyleSheet(
            '''
                #resultLabel {
                    margin-left: 10px;
                    margin-right: 10px;
                }
            '''
        );

        # 初始化计算
        self.calculator = Calculator();

        # 数字和加减乘除绑定
        for num in self.calculator.numberList :
            if( num != '.' ):
                numberButton = getattr( self.mainWindow, f'number{num}' );
                numberButton.clicked.connect( lambda checked = False, n = num: self.calculator.preview( self.mainWindow, n ) );

        self.mainWindow.decButton.clicked.connect( lambda: self.calculator.preview( self.mainWindow, '.' ) );
        self.mainWindow.modButton.clicked.connect( lambda: self.calculator.preview( self.mainWindow, '%' ) );
        self.mainWindow.addButton.clicked.connect( lambda: self.calculator.preview( self.mainWindow, '+' ) );
        self.mainWindow.subButton.clicked.connect( lambda: self.calculator.preview( self.mainWindow, '-' ) );
        self.mainWindow.mulButton.clicked.connect( lambda: self.calculator.preview( self.mainWindow, '*' ) );
        self.mainWindow.divButton.clicked.connect( lambda: self.calculator.preview( self.mainWindow, '÷' ) );

        # 操作绑定
        self.mainWindow.delButton.clicked.connect( lambda: self.calculator.delete( self.mainWindow ) );
        self.mainWindow.acButton.clicked.connect( lambda: self.calculator.reset( self.mainWindow ) );
        self.mainWindow.equalButton.clicked.connect( lambda: self.calculator.calsResult( self.mainWindow ) );

        

    # 运行程序
    def run( self ):
        self.mainWindow.show();
        