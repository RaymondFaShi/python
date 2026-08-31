'''
    启动程序
'''
# from PySide6.QtWidgets import QMessageBox;
# from PySide6.QtUiTools import QUiLoader;
from PySide6.QtWidgets import QMainWindow
from app.calculator import Calculator;
# from app.common import resourcePath;
from app.resources.calculatorUI import Ui_Form;

class Bootstrap:

    # 主窗口
    mainWindow = None;

    # ui
    ui = None;

    calculator = None;

    # construct
    def __init__( self ):
        # # ui路径
        # uiFilePath = resourcePath( "app/ui/calculator.ui" );

        # # 载入ui文件
        # self.mainWindow = QUiLoader().load( uiFilePath );
        
        # 主窗口
        self.mainWindow = QMainWindow();

        # ui
        self.ui = Ui_Form();

        # 载入ui
        self.ui.setupUi( self.mainWindow );
        
        # previewLabel调整
        self.ui.previewLabel.setStyleSheet(
            '''
                #previewLabel {
                    margin-left: 10px;
                    margin-right: 10px;
                }
            '''
        );

        # resultLabel调整
        self.ui.resultLabel.setStyleSheet(
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
                numberButton = getattr( self.ui, f'number{num}' );
                numberButton.clicked.connect( lambda checked = False, n = num: self.calculator.preview( self.ui, n ) );

        self.ui.decButton.clicked.connect( lambda: self.calculator.preview( self.ui, '.' ) );
        self.ui.modButton.clicked.connect( lambda: self.calculator.preview( self.ui, '%' ) );
        self.ui.addButton.clicked.connect( lambda: self.calculator.preview( self.ui, '+' ) );
        self.ui.subButton.clicked.connect( lambda: self.calculator.preview( self.ui, '-' ) );
        self.ui.mulButton.clicked.connect( lambda: self.calculator.preview( self.ui, '*' ) );
        self.ui.divButton.clicked.connect( lambda: self.calculator.preview( self.ui, '÷' ) );

        # 操作绑定
        self.ui.delButton.clicked.connect( lambda: self.calculator.delete( self.ui ) );
        self.ui.acButton.clicked.connect( lambda: self.calculator.reset( self.ui ) );
        self.ui.equalButton.clicked.connect( lambda: self.calculator.calsResult( self.ui ) );

        

    # 运行程序
    def run( self ):
        self.mainWindow.show();

