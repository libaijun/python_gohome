"""
    用flask写后台接口
"""
from MysqlHelper import MysqlUtil   # 导入MysqlHelper模块的类MysqlUtil
from flask import Flask

app = Flask(__name__)


@app.route("/hello", methods=['GET'])
def hello():
    return "Hello Flask!!!"


@app.route("/person/<int:person_id>", methods=['GET', 'POST'])
def person_info(person_id):
    json_obj = {
        "id": "%d" % person_id,
        "name": "张无忌",
        "age": 30,
        "address": "冰火岛"
    }
    return json_obj


@app.route("/position/<int:pos_id>", methods=['GET'])
def position_info(pos_id):
    sql = "select * from t_position where id = %s"
    select_result = MysqlUtil.op_select(sql, pos_id)
    print(select_result)
    return select_result


if __name__ == "__main__":
    app.run(port=9000, debug=1, host='0.0.0.0')
