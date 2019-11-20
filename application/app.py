import json

from utils import sum_numbers, create_app

app = create_app()


@app.route('/total', methods=['GET'])
def get_total():
    sum = sum_numbers(app.config['NUMBERS'])
    return json.dumps({'total': sum})


#app.run() # to run locally