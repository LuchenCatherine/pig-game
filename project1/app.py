from flask import Flask, render_template
import numpy as np
import json

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():  # put application's code here

    action = np.load('one_die_action.npy')
    json_array = json.dumps(action.tolist())
    return render_template('index.html', data=json_array)


if __name__ == '__main__':
    app.run()
