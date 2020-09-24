from flask import Flask, render_template, request

app = Flask(__name__)

def roman(number):
    number = int(number)
    integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    x = 0
    while  number > 0:
        for i in range(number // integer[x]):
            roman_num += romans[x]
            number -= integer[x]
        x += 1
    return roman_num

@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html', developer_name= 'E2105-Ozkan', not_valid = False )


@app.route("/", methods = ["GET", "POST"])
def head():
    sayi = request.form['number']
    
    if not sayi.isdecimal():
        return render_template('index.html', developer_name ='E2105-Ozkan', not_valid = True)
    sayi = int(sayi)
    if not 0 < sayi< 4000 :
        return render_template('index.html', developer_name ='E2105-Ozkan', not_valid = True)
    
    return render_template("result.html", number_decimal = sayi, number_roman = roman(sayi) , developer_name="E2105-Ozkan")

if __name__ == "__main__":
    #app.run(debug = True)
    app.run(host='0.0.0.0', port=80)

