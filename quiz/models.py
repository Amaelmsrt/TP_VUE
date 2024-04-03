from .app import db
from flask import url_for

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

    def __repr__(self):
        return '<Questionnaire (%d) %s>' % (self.id, self.name)
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'questions': url_for('get_quiz_id', quiz_id=self.id)
        }
    
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship('Questionnaire', backref=db.backref('questions', lazy='dynamic'))
    question_type = db.Column(db.String(120))

    __mapper_args__ = {
        'polymorphic_identity':'question',
        'with_polymorphic': '*',
        'polymorphic_on': 'question_type'
    }
    
class SimpleQuestion(Question):
    __mapper_args__ = {
        'polymorphic_identity':'simplequestion',
        'with_polymorphic': '*',
        'polymorphic_load': 'inline'
    }
     
    reponse = db.Column(db.String(120))
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'reponse': self.reponse,
            'type': self.question_type
        }

class MutipleQuestion(Question):
    __mapper_args__ = {
        'polymorphic_identity':'multiplequestion',
        'with_polymorphic': '*',
        'polymorphic_load': 'inline'
    }
     
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    proposition1 = db.Column(db.String(120))
    proposition2 = db.Column(db.String(120))
    reponse = db.Column(db.String(120))

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'reponse': self.reponse,
            'type': self.question_type,
            'proposition1': self.proposition1,
            'proposition2': self.proposition2
        }

def get_questionnaires():
    return [q.to_json() for q in Questionnaire.query.all()]

def get_questions(questionnaire_id):
    return [url_for("get_quiz_question", 
        quiz_id=questionnaire_id, question_id=q.id) 
        for q in Question.query.filter_by(questionnaire_id=questionnaire_id).all()]

def get_question(id):
    return Question.query.filter_by(id=id).first().to_json()