from flask import *
import json

app = Flask(__name__)
app.secret_key = "asdf2LasAdDK3d2fFJ"

def isCorrectNum(num):
    num = str(num)
    if not num.isdigit():
        return False
    if len(num) != 4:
        return False
    if int(num[0:2]) != 24:
        return False
    if int(num[2:4]) > 20 or int(num[2:4]) < 0:
        return False
    return True

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/main', methods = ['POST'])
def main():
    num = int(request.form['number'])
    pA = int(request.form['physicsA'])
    cA = int(request.form['chemistryA'])
    bA = int(request.form['biologyA'])
    bB = int(request.form['biologyB'])

    if isCorrectNum(num):
        file = open('data.json')
        data_array = json.load(file)
        file.close()

        isPersonExists = 0

        for person in data_array:
            if person['num'] == num:
                isPersonExists = 1
                person['pa'] = pA
                person['ca'] = cA
                person['ba'] = bA
                person['bb'] = bB

        if not isPersonExists:
            newPerson = {}
            newPerson['num'] = num
            newPerson['pa'] = pA
            newPerson['ca'] = cA
            newPerson['ba'] = bA
            newPerson['bb'] = bA
            data_array.append(newPerson)

        file = open('data.json', 'w')
        file.write(json.dumps(data_array))
        file.close()

    else:
        flash("학번이 잘못되었습니다.") 

    return render_template('index.html')
        

if __name__ == '__main__':
    app.run(debug=True)
