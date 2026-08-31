'''
    Calculator 计算器类
'''
from PySide6.QtWidgets import QMessageBox;
# from simpleeval import simple_eval;
from sympy import sympify;

class Calculator:
    # 数字列表
    numberList = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '.' );

    # 操作符列表
    operateList = ( '%', '*', '÷', '+', '-' );

    # 计算列表
    __previewLabel = '';

    # 结果
    __resultLabel = '';

    # contruct
    def __init__( self ):
        pass

    # 预览
    def preview( self, winForm, context ):
        # 如果最后一个字符是操作列表的字符，则不允许再进行追加
        if( context in self.operateList ):
            if( len( self.__previewLabel  ) == 0 ): return;
            if( self.__previewLabel[ -1 ] in self.operateList ): return;

        self.__previewLabel += str( context );
        winForm.previewLabel.setText( self.__previewLabel );
        winForm.resultLabel.setText( '' );
    
    # 计算结果
    def calsResult( self, winForm ):
        # 最后一个是计算符不进行计算
        if( self.__previewLabel[ -1 ] in self.operateList ): return;

        # 预览不能为空
        if not self.__previewLabel: return;

        try:
            # 除法字符格式化
            expression = self.__previewLabel.replace( '÷', '/' );
            self.__resultLabel = str( round( sympify( expression ).evalf(), 8 ) );

            # 去后面多余的0
            if( '.' in self.__resultLabel ):
                self.__resultLabel = self.__resultLabel.rstrip( "0" ).rstrip( "." );
            
            winForm.resultLabel.setText( str(  self.__resultLabel ) );
        except ZeroDivisionError as ex:
            QMessageBox.critical( winForm, '计算错误', '除数不能为0' );
        # except:
        #     QMessageBox.critical( winForm, '计算错误', '计算公式错误' );
        

    # 重置
    def reset( self, winForm ):
        self.__previewLabel = '';
        self.__resultLabel = '';
        winForm.previewLabel.setText( '' );
        winForm.resultLabel.setText( '0' );

    # 删除
    def delete( self, winForm ):
        if( len( self.__previewLabel ) != 0 ):
            self.__previewLabel = self.__previewLabel[ :-1 ];
            winForm.previewLabel.setText( self.__previewLabel );