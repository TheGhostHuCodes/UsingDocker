from flask import Flask, Response, request
import requests
import urllib.parse

app = Flask(__name__)
default_name = 'Joe Bloggs'


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    name = default_name
    if request.method == 'POST':
        name = request.form['name']

    header = '<html><head><title>Identidock</title></head><body>'
    body = '''<form method="POST">
           Hello <input type="text" name="name" value="{0}">
           <input type="submit" value="submit">
           </form>
           <p>You look like a:
           <img src="/moster/{1}"/>
           '''.format(name, urllib.parse.quote(name))
    footer = '</body></html>'

    return header + body + footer


@app.route('/moster/<name>')
def get_identicon(name):
    r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
    image = r.content

    return Response(image, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
