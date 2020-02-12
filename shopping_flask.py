from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

app = Flask(__name__)


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('posting.html')


@app.route('/order', methods=['GET'])
def listing():
    # 모든 document 찾기
    result = list(db.customer_data.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'customer_data': result})


## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def saving():
    # saving 이라는 함수명은 아무거나 해도 상관없음. 안써먹는다
    name = request.form['name']
    sort = request.form['sort']
    cnt = request.form['cnt']
    addr = request.form['addr']
    PN = request.form['PN']
    # 데이터를 받아와서

    # mongoDB에 넣는 부분
    data = {'name': name,
            'sort': sort,
            'cnt': cnt,
            'addr': addr,
            'PN': PN
            }

    db.customer_data.insert_one(data)

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
