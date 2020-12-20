import os

from flask import Flask
import recognitor as Recognitor
from pyaudioclassification import feature_extraction, train, predict, print_leaderboard
import numpy as np

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():

    if np.DataSource().exists("./model.h5"):
        from keras.models import load_model
        model = load_model('./model.h5')

        pred = predict(model, './cow_test.wav')
        return str(pred)
    return 'None'


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)