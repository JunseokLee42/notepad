from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 새 파일 기능
@app.route('/new', methods=['POST'])
def new_file():
    return "New file ready!"

# 파일 열기 기능
@app.route('/open', methods=['GET'])
def open_file():
    filename = request.args.get('filename')
    if filename and os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    return "No file found!"

# 파일 저장 기능 (사용자가 파일명을 지정)
@app.route('/save', methods=['POST'])
def save_file():
    content = request.form['content']
    filename = request.form['filename']
    if filename:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"File '{filename}' saved successfully!"
    return "Error: Filename is required."

if __name__ == '__main__':
    app.run(debug=True)
