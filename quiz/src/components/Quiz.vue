<template>
    <h2>{{ quiz.title }}</h2>
    <ol>
        <li v-for="question in questions" :key="question.id">
            <Question :question="question"/>
        </li>
    </ol>
</template>

<script>
import Question from './Question.vue'
import axios from 'axios'

export default {
    data() {
        return {
            questions: []
        }
    },
    props: {
        quiz: Object
    },
    components: {
        Question
    },
    async created() {
        const response = await axios.get(`http://localhost:5000/quiz/api/v1.0/quiz/${this.quiz.id}/questions`);
        this.questions = await Promise.all(response.data.questions.map(async question => {
            const response = await axios.get(`http://localhost:5000/${question}`);
            return {
                ...response.data
            }
        }));
    }
}
</script>