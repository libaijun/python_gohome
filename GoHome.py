import psutil
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

import MyLogging


# r'' 防止路径带空格
config = {'process_name': 'TeamViewer.exe', 'process_path': r'"C:/Program Files (x86)/TeamViewer/TeamViewer.exe"'}

# 创建logger
logger = MyLogging.my_logger


# 查询指定的程序的pid
def get_process_pid(process_name):
    pids = psutil.pids()
    for pid in pids:
        try:
            if psutil.Process(pid).name() == process_name:
                return pid
        except psutil.NoSuchProcess:
            logger.error("%s 没有该进程: %s" % (detail_now(), pid))

    else:
        return None


def start_process():
    flag = get_process_pid(config['process_name'])
    if flag is not None:
        logger.info("%s 程序【%s】已启动, pid = %d " % (detail_now(), config['process_name'], flag))
    else:
        logger.info("%s 程序【%s】未启动, 启动之" % (detail_now(), config['process_name']))
        os.startfile(config['process_path'])


def detail_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    logger.info('启动python脚本......')
    scheduler = BlockingScheduler()
    # 工作日
    scheduler.add_job(start_process, 'cron', day_of_week='0-4', hour='16-23,0-9', minute='*/1', second='0')
    # 周末
    scheduler.add_job(start_process, 'cron', day_of_week='5-6', minute='*/1', second='0')
    scheduler.start()
