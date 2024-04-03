<template>
  <div id="app">
    <h1>Quiz</h1>
    <button class="btn-success" @click="add = !add">
      {{add ? "Fermer" : "Ajouter un quiz"}}
    </button>

    <div v-if="add">
      <input v-model="newQuiz" placeholder="Titre">
      <button @click="addQuiz">Valider</button>
    </div>

    <Quiz v-for="q in quiz" :key="quiz.id" :quiz="q" @quiz-deleted="loadQuiz"/>
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
      quiz: [],
      add: false,
      newQuiz: ''
    }
  },
  methods: {
    async addQuiz() {
      try {
        const response = await axios.post('http://localhost:5000/quiz/api/v1.0/quiz', {
          title: this.newQuiz
        });
        this.add = false;

        this.quiz.push({
          id: response.data.id,
          title: response.data.title,
          questions: response.data.questions
        });

        this.newQuiz = '';
      }catch (error){
        console.error(error);
      }
    },
    async loadQuiz(){
      const response = await axios.get('http://localhost:5000/quiz/api/v1.0/quiz');
      this.quiz = await Promise.all(response.data.questionnaires.map(async q => {
        return {
          ...q
        };
      }));
    }
  },
  async created() {
    const response = await axios.get('http://localhost:5000/quiz/api/v1.0/quiz');
    this.quiz = await Promise.all(response.data.questionnaires.map(async q => {
      return {
        ...q
      };
    }));
  }
}
</script>