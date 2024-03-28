from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('example.html')

@app.route('/submit-data', methods=['POST'])
def submit_data():
    # 获取 JSON 数据
    data = request.json['data1']
    # 处理数据（这里只是简单地返回了数据）
    return jsonify(message=f"Received data: {data}")

if __name__ == '__main__':
    app.run(debug=True)
