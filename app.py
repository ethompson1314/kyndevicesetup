from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Android')
def android():
        return render_template('android.html')
    
@app.route('/iOS-DEP')
def iosDep():
        return render_template('iosDep.html')
    
@app.route('/iOS')
def ios():
        return render_template('ios.html')
    
@app.route('/Mac')
def mac():
        return render_template('mac.html')
    
@app.route('/Windows')
def windows():
        return render_template('windows.html')
    

if __name__ == "__main__":
    app.run(debug=True)

