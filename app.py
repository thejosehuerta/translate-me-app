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

# function that returns the hour value to the language parameter
def get_hours (language):
    for i in data['languages']:
        if language == i['language']:
            return i['hours']

def delim_array(array, delim):
    res = ''
    for i in array:
        res = res + delim + str(i)
    return res


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
@app.route('/', methods=['POST'])
def translate(trans = translator):
    if request.method == 'POST':
        input = request.form['input']
        language = request.form['language']
        flag = 0
        lang_label = "Your text translated to: "


        # if user leaves the language field blank, return the translation in Enlgish
        if language == '-':
            trans = translator.translate(input, dest='en')
            return render_template('index.html',trans=trans.text, input=input, langs=get_langs(), lang_label = lang_label + "English (Default)")

        # from the language selected, find it in the data array, if it's found then translate the text to that language
        for i in data['languages']:
            if language in i['language']:
                flag = 1
                trans = translator.translate(input, dest=get_code(language))
                return render_template('index.html',trans=trans.text, input=input, langs=get_langs(), lang_label = lang_label + language)
        # if this is reached, then the language was not found and will translate the text to English   
        if flag == 0:
            trans = translator.translate(input, dest='en')
            return render_template('index.html',trans=trans.text, input=input, langs=get_langs(), lang_label = lang_label + "English (Default)")

# populate chart microservice based on front end inputs
@app.route('/chart', methods=['POST'])
def get_chart():
    if request.method == 'POST':
        base_url = 'http://chart-me-app.herokuapp.com/service?'
        chart_type = request.form.get('chart_type')
        lang_values = request.form.getlist('lang_values')
        lang_hours = []
        count_lang_values = len(lang_values)

    # for every element in the lang_values array, append their respective hour to the lang_hours array
    # this way both the language and the hour value will be in the same index for their respective array
    for i in range(len(lang_values)):
        lang_hours.append(get_hours(lang_values[i]))

    url =  base_url + 'chart=' + chart_type + delim_array(lang_values, "&labels=") + delim_array(lang_hours, "&values=")
    return render_template('index.html', langs=get_langs(), url=url)
    
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

# ---------- ERRORS --------------------------
#Handling error 400 and displaying relevant web page
@app.errorhandler(400)
def internal_error(error):
    return render_template('index.html', langs=get_langs()),400

#Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template('index.html', langs=get_langs()),404
 
#Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template('index.html', langs=get_langs()),500


# run app
if __name__ == "__main__":
    app.run(debug=True)