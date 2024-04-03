<template>
    <h2>{{ quiz.title }}</h2>
    <button @click="loadQuestions">
        {{ showQuestions ? 'Cacher les questions' : 'Voir les questions' }}
    </button>
    <button class="btn btn-primary" @click="addingQuestion = !addingQuestion">
        {{ addingQuestion ? 'Annuler' : 'Ajouter une question' }}
    </button>
    <div v-if="addingQuestion">
        <input v-model="newQuestionTitle" placeholder="Titre de la question">
        <div>
        <input type="radio" id="simple" value="simplequestion" v-model="newQuestionType">
        <label for="simple">Question simple</label>
        <input type="radio" id="multiple" value="multiplequestion" v-model="newQuestionType">
        <label for="multiple">Question multiple</label>
        </div>
        <div v-if="newQuestionType === 'simplequestion'">
        <input v-model="newQuestionReponse" placeholder="Réponse à la question">
        </div>
        <div v-else-if="newQuestionType === 'multiplequestion'">
        <input v-model="newQuestionProposition1" placeholder="Proposition 1">
        <input v-model="newQuestionProposition2" placeholder="Proposition 2">
        <input v-model="newQuestionReponse" placeholder="Réponse à la question">
        </div>
        <button @click="addQuestion">Ajouter la question</button>
    </div>
    <ol v-if="showQuestions">
        <li v-for="question in questions" :key="question.id">
            <Question :question="question" :questionnaireId="quiz.id" @question-deleted="loadQuestions"/>
        </li>
    </ol>
</template>

<script>
import Question from './Question.vue'
import axios from 'axios'

export default {
    data() {
        return {
            questions: [],
            showQuestions: false,
            addingQuestion: false,
            newQuestionTitle: '',
            newQuestionType: '',
            newQuestionReponse: '',
            newQuestionProposition1: '',
            newQuestionProposition2: ''
        }
    },
    props: {
        quiz: Object
    },
    components: {
        Question
    },
    methods: {
        async loadQuestions() {
            if (!this.showQuestions) {
                const response = await axios.get(`http://localhost:5000/quiz/api/v1.0/quiz/${this.quiz.id}/questions`);
                this.questions = await Promise.all(response.data.questions.map(async question => {
                    const response = await axios.get(`http://localhost:5000/${question}`);
                    return {
                        ...response.data
                    }
                }));
            }
            this.showQuestions = !this.showQuestions;
        },
        async addQuestion() {
            this.showQuestions = false;
            const questionData = {
                title: this.newQuestionTitle,
                type: this.newQuestionType,
                reponse: this.newQuestionReponse,
                proposition1: this.newQuestionProposition1,
                proposition2: this.newQuestionProposition2
            };
            const response = await axios.post(`http://localhost:5000/quiz/api/v1.0/quiz/${this.quiz.id}/questions`, questionData);
            this.questions.push(response.data);
            this.addingQuestion = false;
            this.newQuestionTitle = '';
            this.newQuestionType = '';
            this.newQuestionReponse = '';
            this.newQuestionProposition1 = '';
            this.newQuestionProposition2 = '';
        }
    }
}
</script>