from flask import jsonify, abort, make_response, request
from .app import app
from flask import url_for
from .models import *

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.route('/quiz/api/v1.0/quiz', methods=['GET'])
def get_quiz():
    return jsonify(questionnaires=get_questionnaires())

@app.route('/quiz/api/v1.0/quiz/<int:quiz_id>/questions', methods=["GET"])
def get_quiz_id(quiz_id):
    return jsonify(questions=get_questions(quiz_id))

@app.route('/quiz/api/v1.0/quiz/<int:quiz_id>/questions/<int:question_id>', methods=["GET"])
def get_quiz_question(quiz_id, question_id):
    return jsonify(question=get_question(question_id))

@app.route('/quiz/api/v1.0/quiz', methods=["POST"])
def add_quiz():
    if not request.json or not 'title' in request.json:
        abort(400)

    title = request.json['title']
    questionnaire = Questionnaire(title=title)
    db.session.add(questionnaire)
    db.session.commit()
    return jsonify(questionnaire.to_json()), 201

@app.route('/quiz/api/v1.0/quiz/<int:quiz_id>', methods=["PUT"])
def update_quiz(quiz_id):
    questionnaire = Questionnaire.query.filter_by(id=quiz_id).first()
    if not questionnaire:
        abort(400)

    if not request.json:
        abort(400)

    if 'title' in request.json:
        questionnaire.title = request.json['title']
    else: 
        abort(400)

    db.session.commit()
    return jsonify(questionnaire.to_json())

@app.route('/quiz/api/v1.0/quiz/<int:quiz_id>', methods=["DELETE"])
def delete_quiz(quiz_id):
    questionnaire = Questionnaire.query.filter_by(id=quiz_id).first()
    if not questionnaire:
        abort(400)
    db.session.delete(questionnaire)
    db.session.commit()
    return jsonify({'resultat': "true"})

@app.route('/quiz/api/v1.0/quiz/<int:quiz_id>/questions', methods=["POST"])
def add_question(quiz_id):
    if not request.json or not 'title' in request.json or not 'type' in request.json or not 'reponse' in request.json:
        abort(400)
    
    title = request.json['title']
    questionType = request.json['type']
    reponse = request.json['reponse']

    if questionType == "simplequestion":

        question = SimpleQuestion(title=title, question_type=questionType, questionnaire_id=quiz_id,
                                  reponse=reponse)
        
    elif questionType == "multiplequestion":
        if not 'proposition1' in request.json or not 'proposition2' in request.json:
            abort(400)

        question = MutipleQuestion(title=title, question_type=questionType, questionnaire_id=quiz_id, 
                                   proposition1=request.json['proposition1'],
                                   proposition2=request.json['proposition2'],
                                   reponse=reponse)
    else:
        abort(400)

    db.session.add(question)
    db.session.commit()
    return jsonify(question.to_json()), 201

@app.route('/quiz/api/v1.0/quiz/<int:quiz_id>/questions/<int:question_id>', methods=["PUT"])
def update_question(quiz_id, question_id):
    question = Question.query.filter_by(id=question_id).first()
    if not question:
        abort(400)

    if 'title' not in request.json or 'type' not in request.json or 'reponse' not in request.json:
        abort(400)

    question_type = request.json['type']
    if question_type == "multiplequestion":
        if not 'proposition1' in request.json or not 'proposition2' in request.json:
            abort(400)

        question.proposition1 = request.json['proposition1']
        question.proposition2 = request.json['proposition2']

    question.reponse = request.json['reponse']
    question.title = request.json['title']
    db.session.commit()
    return jsonify(question.to_json())

@app.route('/quiz/api/v1.0/quiz/<int:quiz_id>/questions/<int:question_id>', methods=["DELETE"])
def delete_question(quiz_id, question_id):
    question = Question.query.filter_by(id=question_id).first()
    if not question:
        abort(400)
    db.session.delete(question)
    db.session.commit()
    return jsonify({'resultat': "true"})