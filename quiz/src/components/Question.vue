<template>
    <div class="question">
      <h2>{{ question.title }}</h2>
      <div v-if="question.questionType === 'simplequestion'">
        <p>{{ question.reponse }}</p>
      </div>
      <div v-else-if="question.questionType === 'multiplequestion'">
        <p>{{ question.proposition1 }}</p>
        <p>{{ question.proposition2 }}</p>
        <p>{{ question.reponse }}</p>
      </div>
      <button class="btn btn-danger" @click="deleteQuestion">Supprimer</button>
      <button class="btn btn-primary" @click="editQuestion">Modifier</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      question: Object
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