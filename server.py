from flask import Flask,jsonify,render_template,request
app=Flask(__name__,static_folder='../static')
@app.route('/')
def apps():
    return render_template('app.html')

if __name__ == '__main__':
    apps()
    app.run()
