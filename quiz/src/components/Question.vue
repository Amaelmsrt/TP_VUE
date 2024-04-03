<template>
  <div class="question">
    <p>{{ question.question.title }}</p>
    <div v-if="question.question.questionType === 'simplequestion'">
      <p>{{ question.question.reponse }}</p>
    </div>
    <div v-else-if="question.question.questionType === 'multiplequestion'">
      <p>{{ question.question.proposition1 }}</p>
      <p>{{ question.question.proposition2 }}</p>
      <p>{{ question.question.reponse }}</p>
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