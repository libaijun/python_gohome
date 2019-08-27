"""
    mongodb demo
"""
import pymongo
import ReadConf


# 返回指定的集合
def get_collection(db, col):
    mongo_host = ReadConf.mongo['host']
    mongo_port = ReadConf.mongo['port']

    mongo_client = pymongo.MongoClient(host=mongo_host, port=int(mongo_port))
    # 指定数据库
    db = mongo_client[db]
    # 指定集合
    stu_collection = db[col]
    return stu_collection


# 向指定集合插入一条数据
def insert_one(col, json_object):
    result = col.insert_one(json_object)
    return result


# 修改记录
def update(col, con, record_json):
    result = col.update(con, record_json)
    return result


# 查询
def find_one(col, con):
    result = col.find_one(con)
    return result


# 更新
def update(col, con, stu):
    result = col.replace_one(con, stu)
    return result


# 删除一个
def delete(col, con):
    result = col.delete_one(con)
    return result


# 删除多个
def delete_many(col, con):
    result = col.delete_many(con)
    return result


if __name__ == '__main__':
    collection = get_collection('testdb', 'students');
    # 插入
    student = {
        'id': '20170106',
        'name': '徐小凤',
        'age': 62,
        'gender': 'female',
        'address': '香港'
    }

    # 新增
    # result = insert_one(collection, student)
    # print(result)

    # 查询
    condition = {'name': '徐小凤'}
    one = find_one(collection, condition)
    print(one)

    # 更新
    # one['id'] = '20170104'
    # update_result = update(collection, condition, one)
    # print(update_result)

    # 删除
    # delete1 = delete(collection, condition)
    # print(delete1)

    # 批量删除-->删除大于60岁
    con = {'age': {'$gt': 60}}
    many = delete_many(collection, con)
    print(many)
