import sys;
from pathlib import Path;

# 获取资源地址
def resourcePath( relative_path: str ) -> Path:
    if getattr( sys, "frozen", False ):
        return Path( sys._MEIPASS ) / relative_path;

    return Path( __file__ ).resolve().parent.parent / relative_path;