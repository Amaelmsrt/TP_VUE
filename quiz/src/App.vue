<script>

import Quiz from './components/Quiz.vue'

export default {
    data() {
        return {
            quiz: [
                {
                    id: 1, nom: 'Quiz 1', questions: [
                        { id: 1, question: 'Question 1', reponses: ['Réponse 1', 'Réponse 2', 'Réponse 3'], bonneReponse: 1 },
                        { id: 2, question: 'Question 2', reponses: ['Réponse 1', 'Réponse 2', 'Réponse 3'], bonneReponse: 2 },
                        { id: 3, question: 'Question 3', reponses: ['Réponse 1', 'Réponse 2', 'Réponse 3'], bonneReponse: 3 },
                    ]
                },

            ],
            title: 'Mes quiz'
        }
    }
}
</script>

<template>
<div id="app" class="container">
    <h2>{{ title }}</h2>
    <ol>
        <li v-for="q in quiz">
            <Quiz :quiz="q"></Quiz>
        </li>
    </ol>
  </div>
</template>
