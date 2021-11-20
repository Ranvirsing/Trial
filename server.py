from flask import Flask,jsonify,render_template,request,url_for
app=Flask(__name__)
@app.route('/')
def apps():
    return render_template('app.html')
@app.route('get_est_price', methods=['GET','POST'])
def get_est_price():
    year=int(request.form['year'])
    km=int(request.form['km'])
    tran=request.form['tran']
    mileage=int(request.form['mileage'])
    fuel=request.form['fuel'] 
    response = jsonify({
        'est_price':util.get_est_price(year,km,tran,mileage,fuel)
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response,render_template('app.html')
if __name__ == '__main__':
    apps()
    app.run()
