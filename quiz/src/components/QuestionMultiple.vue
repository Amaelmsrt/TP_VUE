<template>
    <div class="question">
        <h2>{{ question.title }}</h2>
        <p>{{ question.proposition1 }}</p>
        <p>{{ question.proposition2 }}</p>
        <p>{{ question.reponse }}</p>
        <button class="btn btn-danger" @click="deleteQuestion">Supprimer</button>
        <button class="btn btn-primary" @click="editQuestion">Modifier</button>
    </div>
</template>

<script>
    export default {
        props: {
            question: Object,
            required: true
        },
        methods: {
            deleteQuestion() {
                // Logique pour supprimer la question
            },
            editQuestion() {
                // Logique pour modifier la question
            }
        }
    }
</script>
        
        <button class="btn btn-danger" @click="deleteQuestion">Supprimer</button>
    </div>
</template>

<script>
    export default {
        props: {
            question: Object,
            required: true
        }
    }
</script>