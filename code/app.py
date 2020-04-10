from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    height = int(request.args.get('height'))
    weight = int(request.args.get('weight'))
    bmi = round(weight/(height/100)**2,2)

    if(height<=0) or (weight<=0):
        return jsonify({'message':'height or weight must not be below or equal to 0'})

    if(bmi>=18.5) and (bmi<=24.9):
        return jsonify({'bmi':bmi,'label':'healthy'})
    elif(bmi>=25):
        return jsonify({'bmi':bmi,'label':'overweight'})
    else:
        return jsonify({'bmi':bmi,'label':'unclassified'})

if __name__ == '__main__':
    app.run(debug=True)