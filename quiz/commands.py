from .app import app,db
from .models import *

@app.cli.command()
def syncdb():
    db.create_all()

    questionnaire1 = Questionnaire(id=1, title="Questionnaire1")
    questionnaire2 = Questionnaire(id=2, title="Questionnaire2")
    
    question1 = SimpleQuestion(title="Question1", questionnaire_id=1, reponse="Reponse1")
    question2 = SimpleQuestion(title="Question2", questionnaire_id=1, reponse="Reponse2")
    question3 = MutipleQuestion(title="Question3", questionnaire_id=2, proposition1="Reponse3", proposition2="Reponse2", reponse=1)

    db.session.add(questionnaire1)
    db.session.add(questionnaire2)
    db.session.add(question1)
    db.session.add(question2)
    db.session.add(question3)

    db.session.commit()