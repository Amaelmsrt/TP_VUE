<template>
  <div class="question">
    <div class="titre-btn">
      <p>{{ question.question.title }}</p>
      <button class="btn btn-success" @click="editQuestion">Modifier</button>
      <button class="btn btn-danger" @click="deleteQuestion">Supprimer</button>
    </div>
    <div v-if="question.question.questionType === 'simplequestion'">
      <p>Réponse : {{ question.question.reponse }}</p>
    </div>
    <div v-else-if="question.question.questionType === 'multiplequestion'">
      <p>Proposition 1 : {{ question.question.proposition1 }}</p>
      <p>Proposition 2 :{{ question.question.proposition2 }}</p>
      <p>Réponse : {{ question.question.reponse }}</p>
    </div>
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

<style>
  .titre-btn {
    display: flex;
  }

  button {
    margin-left: 10px;
    font-size: 1rem;
  }
</style>