from flask import Flask, abort, request, jsonify
 
app = Flask(__name__)
 
@app.route('/demo_post', methods=['POST'])
def demo_post():
    if not request.json or 'name' not in request.json or 'age' not in request.json:
        abort(400)    
    get_name = request.json.get("name")
    get_age = request.json.get("age")
    get_age += 10
    return jsonify(name=get_name, age=get_age)
 
if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run()