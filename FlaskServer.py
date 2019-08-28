"""
    用flask写后台接口
"""
from flask import Flask

app = Flask(__name__)


@app.route("/hello", methods=['GET'])
def hello():
    return "Hello Flask!!!"


@app.route("/person/<int:person_id>", methods=['GET', 'POST'])
def person_info(person_id):
    json_str = {
        "id": "%d" % person_id,
        "name": "张无忌",
        "age": 30,
        "address": "冰火岛"
    }
    return json_str


if __name__ == "__main__":
    app.run(port=9000, debug=1)