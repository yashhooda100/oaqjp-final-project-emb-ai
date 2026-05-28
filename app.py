from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    provider = None

    if request.method == 'POST':
        npi = request.form['npi']

        url = f"https://npiregistry.cms.hhs.gov/api/?number={npi}&version=2.1"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if data['result_count'] > 0:
                provider = data['results'][0]

    return render_template('index.html', provider=provider)

if __name__ == '__main__':
    app.run(debug=True)