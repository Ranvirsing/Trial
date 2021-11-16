from flask import Flask,jsonify,render_template,request
import util 
app=Flask(__name__)
@app.route('/')
def apps():
    return render_template('app.html')


    


if __name__ == '__main__':
    util.load_artfacts()
    app.run(debug=True)
