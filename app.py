from flask import Flask
from flask import  render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Welcome to MSRIT registration"
@app.route('/students')
def hello_world2():
    return render_template('student.html')
@app.route('/faculty')
def hello_world3():
    return render_template('faculty.html')
@app.route('/admin')
def hello_world4():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run()
