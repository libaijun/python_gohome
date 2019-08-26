"""
    日志配置
"""
import logging
from datetime import datetime
import os


class MyLogging:

    def __init__(self):
        time_str = datetime.now().strftime('%Y-%m-%d')

        cwd = os.getcwd().split("/")
        project_name = cwd[len(cwd) - 1]

        lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../logs/', project_name))

        exists = os.path.exists(lib_path)
        if not exists:
            print('不存在，创建目录 %s ' % lib_path)
            os.mkdir(lib_path)

        # 日志格式  os.sep: 路径分隔符 \ /
        filename = lib_path + os.sep + time_str + ".log"

        # 默认root
        self.logger = logging.getLogger('lbj')

        # 等级
        self.logger.setLevel(logging.INFO)

        # 输出取控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # 打印日志到文件
        file_handler = logging.FileHandler(filename=filename)
        file_handler.setLevel(logging.INFO)

        # 设置格式对象
        formatter = logging.Formatter(
            "%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s - %(message)s")

        # 设置handler的格式对象
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # 加到logger中
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)


# 暴露一个日志对象
my_logger = MyLogging().logger
