from flask import Flask,jsonify,render_template,request,url_for
app=Flask(__name__)
@app.route('/')
def apps():
    return render_template('app.html')

if __name__ == '__main__':
    apps()
    app.run()
