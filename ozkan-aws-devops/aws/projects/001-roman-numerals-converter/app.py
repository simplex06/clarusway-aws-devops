from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def head():
    if request.method == "POST":
        num = request.form["number"]
        return render_template("index.html", number = num, developer_name="E2105-Ozkan")
    else:
        return render_template("result.html", developer_name="E2105-Ozkan")
    #return render_template("index.html", developer_name="E2105-Ozkan")

@app.route("/result")
def result():
    return render_template("result.html", developer_name="E2105-Ozkan")


# This code converts an integer to a roman number between 1 and 3999.
def roman(number):
    while True: 
        if number == 'exit':
            print("Goodbye")
            break

        elif number.isdecimal():
            number = int(number)

            if not 0 < number < 4000:
                print("Enter a number 0 < num < 4000: ")

            elif 0 < number < 4000:
                integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
                romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
                roman_num = ''
                x = 0
                while  number > 0:
                    for i in range(number // integer[x]):
                        roman_num += romans[x]
                        number -= integer[x]
                    x += 1

                print(roman_num)

if __name__ == "__main__":
    app.run(debug = True)
    #app.run(host='0.0.0.0', port=80)

