from flask import Flask, render_template, request

app = Flask(__name__)

def milli(number):
    hour = number // (1000*60*60)
    minute = (number - hour * (1000*60*60)) // (1000*60)
    sec = (number - hour * (1000*60*60) - minute * (1000*60)) // (1000)
    return f"{hour} hour/s {minute} minute/s {sec} second/s"

@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html', developer_name= 'E2105-Ozkan', not_valid = False )


@app.route("/", methods = ["GET", "POST"])
def head():
    sayi = request.form['number']
    
    if not sayi.isnumeric() :
        return render_template('index.html', developer_name ='E2105-Ozkan', not_valid = True)
        
    sayi = int(sayi)
    if not sayi > 0:
        return render_template('index.html', developer_name ='E2105-Ozkan', not_valid = True)
    
    return render_template("result.html", milliseconds = sayi, result = milli(sayi) , developer_name="E2105-Ozkan")

if __name__ == "__main__":
    app.run(debug = True)
    #app.run(host='0.0.0.0', port=80)

