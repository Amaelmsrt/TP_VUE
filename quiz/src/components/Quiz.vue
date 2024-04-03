<template>
    <h2>{{ quiz.title }}</h2>
    <button @click="loadQuestions">
        {{ showQuestions ? 'Cacher les questions' : 'Voir les questions' }}
    </button>
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
            showQuestions: false
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
        }
    }
}
</script>