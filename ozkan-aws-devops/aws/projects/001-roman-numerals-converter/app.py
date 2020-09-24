from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def head():
    if request.method == "POST":
        num = request.form["number"]
        if number.isdecimal():
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
        return render_template("result.html", number = num, developer_name="E2105-Ozkan", not_valid = False)
    else:
        return render_template("index.html", developer_name="E2105-Ozkan", not_valid = True)
    #return render_template("index.html", developer_name="E2105-Ozkan")

if __name__ == "__main__":
    #app.run(debug = True)
    app.run(host='0.0.0.0', port=80)

