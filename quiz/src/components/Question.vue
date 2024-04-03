<template>
   <div class="card">
      <div class="card-header">
         <h2>{{ question.title }}</h2>
         <button @click="deleteQuestion" class="btn btn-danger">Supprimer</button>
         <button v-if="!edit" @click="edit = true" class="btn btn-primary">Editer</button>
         <button v-else @click="edit = false" class="btn btn-primary">Fermer</button>
      </div>
      <div class="card-body">
         <div v-if="edit">
            <input v-model="question.title" placeholder="Titre">
            <input v-model="question.reponse" placeholder="Reponse">
            <input v-if="question.type === 'multiplequestion'" v-model="question.proposition1" placeholder="Proposition 1">
            <input v-if="question.type === 'multiplequestion'" v-model="question.proposition2" placeholder="Proposition 2">
            <button @click="updateQuestion" class="btn btn-success">Valider</button>
         </div>
         <div v-else>
            <p>Reponse: {{ question.reponse }}</p>
            <p v-if="question.type === 'multiplequestion'">Proposition 1: {{ question.proposition1 }}</p>
            <p v-if="question.type === 'multiplequestion'">Proposition 2: {{ question.proposition2 }}</p>
         </div>
      </div>
   </div>
</template>
<script>

import axios from 'axios';

export default{
   data(){
      return {
         edit: false
      }
   },
   props: {
      question: Object,
      questionnaireId: Number
   },
   methods: {
      async deleteQuestion(){
         try{
            await axios.delete(`http://localhost:5000/quiz/api/v1.0/quiz/${this.questionnaireId}/questions/${this.question.id}`);
            this.$emit('question-deleted', this.question.id);
         }catch(error){
            console.error(error);
         }
      },
      async updateQuestion(){
         try{
            await axios.put(`http://localhost:5000/quiz/api/v1.0/quiz/${this.questionnaireId}/questions/${this.question.id}`, this.question);
            this.edit = false;
         }catch(error){
            console.error(error);
         }
      },
   }
}
</script>