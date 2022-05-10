from flask import Flask

app = Flask (__name__)


@app.route('/test', methods=['GET'])

def somefunction():

    return ''

app.run(host='0.0.0.0', port=3245, debug=True)
