<template>
  <div id="app">
    <h1>{{ title }}</h1>
    <Quiz v-for="quiz in quizzes" :key="quiz.id" :quiz="quiz" />
  </div>
</template>

<script>
import axios from 'axios';
import Quiz from './components/Quiz.vue';

export default {
  name: 'App',
  components: {
    Quiz
  },
  data() {
    return {
      title: 'Mes quiz',
      quizzes: []
    }
  },
  async created() {
    const response = await axios.get('http://localhost:5000/quiz/api/v1.0/quiz');
    this.quizzes = await Promise.all(response.data.questionnaires.map(async quiz => {
      return {
        ...quiz
      };
    }));
  }
}
</script>