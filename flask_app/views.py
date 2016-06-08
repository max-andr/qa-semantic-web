import json

from flask import render_template, flash, url_for, request, session, \
    redirect, abort
from urllib.parse import quote
from flask_app import app
from src.qa import ask
from src.db import DB


@app.route('/')
@app.route('/index')
def home():
    print(app.template_folder)
    print(app.jinja_loader.list_templates())
    return render_template("index.html")

@app.route('/get_answer', methods=['GET'])
def get_answer():
    question = request.args['question']
    language = request.args['language']
    return json.dumps(ask(question, language=language))

@app.route('/set_feedback', methods=['POST'])
def set_feedback():
    question = request.form['question']
    language = request.form['language']
    is_correct = request.form['isCorrect']
    data_dict = request.form
    DB().put_qa(question, language, is_correct)
    return json.dumps({'success': True})