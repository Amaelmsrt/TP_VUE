<template>
    <input v-model="newQuestion.title" placeholder="Titre">
    <select class="form-select"v-model="newQuestion.type">
        <option value="simplequestion">Simple</option>
        <option value="multiplequestion">Multiple</option>
    </select>
    <input v-model="newQuestion.reponse" placeholder="Reponse">
    <input v-if="newQuestion.type === 'multiplequestion'" v-model="newQuestion.proposition1" placeholder="Proposition 1">
    <input v-if="newQuestion.type === 'multiplequestion'" v-model="newQuestion.proposition2" placeholder="Proposition 2">
    <button @click="addQuestion" class="btn btn-success">Valider</button>
    <button @click="add = false" class="btn btn-primary">Annuler</button>
</template>

<script>
import axios from 'axios'

export default{
    data(){
        return {
            newQuestion: {
                title: '',
                type: '',
                reponse: '',
                proposition1: '',
                proposition2: ''
            },
        }
    },
    props: {
        quiz: Object,
    },
    methods: {
        async addQuestion(){
            const response = await axios.post(`http://localhost:5000/quiz/api/v1.0/quiz/${this.quiz.id}/questions`, this.newQuestion);
            this.$emit('question-add', response.data);
            this.newQuestion = {
                title: '',
                type: '',
                reponse: '',
                proposition1: '',
                proposition2: ''
            };
        }, 
    }
}
</script>