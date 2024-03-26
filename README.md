# SERVEUR

### Commandes

Pour lancer le serveur :

```
flask run
```

Pour lancer le client : 

```
Ouvrir le fichier quiz.html dans le navigateur
```

### Commandes curl

Liste des quiz:

```
curl -i http://localhost:5000/quiz/api/v1.0/quiz
```

Ajouter un quiz:

```
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"NouveauQuiz"}' http://localhost:5000/quiz/api/v1.0/quiz
```

Supprimer un quiz:

```
curl -i -H "Content-Type: application/json" -X DELETE  http://localhost:5000/quiz/api/v1.0/quiz/3
```

Liste des questions d'un quiz:

```
curl -i http://localhost:5000/quiz/api/v1.0/quiz/1/questions
```

Détails sur une question :

```
curl -i http://localhost:5000/quiz/api/v1.0/quiz/1/questions/1
```

Ajouter une question :

```
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"NouvelleQuestion", "type": "simplequestion", "reponse": "ReponseQuestion"}' http://localhost:5000/quiz/api/v1.0/quiz/3/questions
```

Supprimer une question :

```
curl -i -H "Content-Type: application/json" -X DELETE  http://localhost:5000/quiz/api/v1.0/quiz/3/questions/1
```