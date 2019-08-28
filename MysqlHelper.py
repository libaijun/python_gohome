"""
    相当于java中的dao层
"""
import pymysql
import ReadConf
from DBUtils.PooledDB import PooledDB


class MysqlUtil:
    conn_pool = None

    db_cfg = ReadConf.db

    # port 用int()转换
    config = {'host': db_cfg['host'], 'port': int(db_cfg['port']), 'database': db_cfg['database'],
              'user': db_cfg['user'], 'password': db_cfg['password'], 'charset': db_cfg['charset']}

    def __init__(self):
        pass

    @staticmethod
    def get_pool():
        if MysqlUtil.conn_pool is None:
            conn_pool = PooledDB(creator=pymysql, mincached=1, maxcached=20, **MysqlUtil.config)
        return conn_pool

    @staticmethod
    def get_mysql_connection():
        return MysqlUtil.get_pool().connection()

    # 查询
    @staticmethod
    def op_select(select_sql, condition):
        conn = MysqlUtil.get_mysql_connection()
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(select_sql, condition)

        all_data = cur.fetchone()

        MysqlUtil.close_resource(conn, cur)
        return all_data

    # 释放资源
    @staticmethod
    def close_resource(conn, cur):
        conn.close()
        cur.close()


if __name__ == '__main__':
    sql = "select * from t_position where id = %s;"
    mh = MysqlUtil()
    select_res = mh.op_select(sql, 1)
