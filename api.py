import os

from flask import Flask
import recognitor as Recognitor
from pyaudioclassification import feature_extraction, train, predict, print_leaderboard
import numpy as np
from keras.models import load_model
from azure.storage.blob import BlobClient

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():

    if np.DataSource().exists("./model.h5"):
        model = load_model('./model.h5')

        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        container_name = os.getenv('AZURE_STORAGE_CONTAINER_NAME')

        download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))


        sas_url = "https://account.blob.core.windows.net/container/blob-name?sv=2015-04-05&st=2015-04-29T22%3A18%3A26Z&se=2015-04-30T02%3A23%3A26Z&sr=b&sp=rw&sip=168.1.5.60-168.1.5.70&spr=https&sig=Z%2FRHIX5Xcg0Mq2rqI3OlWTjEg2tYkboXr1P9ZUXDtkk%3D"
        blob_client = BlobClient.from_blob_url(sas_url)

        with open(download_file_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())


        pred = predict(model, download_file_path)
        return str(pred)
    return 'None'


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)