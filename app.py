from typing import Text, get_args
from flask import Flask, render_template, url_for, request, jsonify, redirect
from googletrans import Translator
import json

# opens the languages.json file and loads it to the 'data variable
with open('static/languages.json', 'r') as file:
    languages = file.read()
data = json.loads(languages)

# function that appends only the language values to the 'all_languages' array
def get_langs():
    all_languages = []
    for i in data['languages']:
        all_languages.append(i['language'])
    return all_languages

# function that returns the code to the language parameter
def get_code (language):
    for i in data['languages']:
        if language == i['language']:
            return i['code']

# initialize google translate translator
translator = Translator()

# initialize app
app = Flask(__name__)

# Homepage of app
@app.route("/")
def index():
    return render_template('index.html', langs=get_langs())

# ---------- ROUTES --------------------------

# /translate 
# Upon clicking 'submit' in the index.html form, this functuon is called which will translate the input and return the output
@app.route('/', methods=['POST', "GET"])
def translate(trans = translator):
    if request.method == 'POST':
        input = request.form['input']
        language = request.form['language']
        flag = 0

        # if user leaves the language field blank, return the translation in Enlgish
        if language == '':
            trans = translator.translate(input, dest='en')
            return render_template('index.html',trans=trans.text, input=input, langs=get_langs())

        # from the language selected, find it in the data array, if it's found then translate the text to that language
        for i in data['languages']:
            if language in i['language']:
                flag = 1
                trans = translator.translate(input, dest=get_code(language))
                return render_template('index.html',trans=trans.text, input=input, langs=get_langs())
        # if this is reached, then the language was not found and will translate the text to English   
        if flag == 0:
            trans = translator.translate(input, dest='en')
            return render_template('index.html',trans=trans.text, input=input, langs=get_langs())

    
# Using the app's URL, you can get a translated input in JSON to use for an external application
@app.route('/translate/<language>/<input>')
def translate_json(language, input):
    trans = translator
    flag = 0

    # from the language selected, find it in the data array, if it's found then translate the text to that language
    for i in data['languages']:
        if language in i['language']:
            flag = 1
            trans = translator.translate(input, dest=get_code(language))
            return jsonify({"output": trans.text, "input": input, "language": language, })
    # if this is reached, then the language was not found and will translate the text to English   
    if flag == 0:
        trans = translator.translate(input, dest='en')
        return jsonify({"output": trans.text, "input": input, "language": language, })       
                
if __name__ == "__main__":
    app.run(debug=True)