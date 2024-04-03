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
  </div>
</template>
  
  <script>
  import axios from 'axios';

  export default {
    props: {
      question: Object,
      questionnaireId: Number
    },
    methods: {
      deleteQuestion() {
        try {
          axios.delete(`http://localhost:5000/quiz/api/v1.0/quiz/${this.questionnaireId}/questions/${this.question.question.id}`);
          this.$emit('delete-question', this.question.question.id);
        } catch (error) {
          console.error(error);
        }
      },
      updateQuestion() {
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