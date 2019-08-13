from flask import Flask
application = Flask(__name__)
@application.route('/')
def helloworld():
    return "Hello World in python,run as a POD in Openshift\r\n",200,{'Content-Type': 'text/plain'}

if __name__== '__main__':
    application.run(debug = True)

