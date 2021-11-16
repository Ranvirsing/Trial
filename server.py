from flask import Flask,jsonify,render_template,request

app=Flask(__name__)
@app.route('/')
def apps():
    return render_template('app.html'), render_template('app.css')


    


if __name__ == '__main__':
    apps()
    app.run()
