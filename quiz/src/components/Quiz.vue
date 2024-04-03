<template>
    <div class="card">
        <div class="card-header bg-secondary">
            <h2>{{ quiz.title }}</h2>
            <button @click="del" class="btn btn-danger">Supprimer</button>
            <button v-if="!showQuestions" @click="loadQuestionsAndShow" class="btn btn-primary">Déplier</button>
            <button v-else @click="showQuestions = false" class="btn btn-primary">Replier</button>
            <button v-if="!edit" @click="edit = true" class="btn btn-primary">Editer</button>
            <button v-else @click="edit = false" class="btn btn-primary">Fermer</button>
            <button v-if="!add" @click="add = true" class="btn btn-primary">Ajouter question</button>
        </div>

        <div class="card-body" v-if="edit">
            <input v-model="quiz.title" placeholder="Titre">
            <button @click="updateQuiz" class="btn btn-success">Valider</button>
        </div>

        <div class="card-body" v-if="add">
           <AddQuestion :quiz="quiz" @question-add="addQuestion"></AddQuestion>
        </div>

        <div class="card-body" v-if="showQuestions">
            <div v-for="question in questions" :key="question.id">
                <Question :question="question" :questionnaireId="quiz.id" @question-deleted="delQuestion"/>
            </div>
        </div>
    </div>
</template>

<script>
import Question from './Question.vue';
import AddQuestion from './AddQuestion.vue';
import axios from 'axios';

export default{
    data(){
        return {
            questions: [],
            showQuestions: false,
            edit: false,
            add: false,
        }
    },
    props: {
        quiz: Object
    },
    components: {
        Question,
        AddQuestion
    },
    methods: {
        async loadQuestions(){
            const response = await axios.get(`http://localhost:5000/quiz/api/v1.0/quiz/${this.quiz.id}/questions`);
            this.questions = await Promise.all(response.data.questions.map(async question => {
                const response = await axios.get(`http://localhost:5000/${question}`);
                return {
                    ...response.data
                }
            }));
        },
        async loadQuestionsAndShow(){
            await this.loadQuestions();
            this.showQuestions = true;
        },
        
        async del(){
            await axios.delete(`http://localhost:5000/quiz/api/v1.0/quiz/${this.quiz.id}`);
            this.$emit('quiz-deleted', this.quiz.id);
        },
        async updateQuiz(){
            await axios.put(`http://localhost:5000/quiz/api/v1.0/quiz/${this.quiz.id}`, this.quiz);
            this.edit = false;
        },
        // supprime de la liste des questions chargées
        delQuestion(id){
            for(let i = 0; i < this.questions.length; i++){
                if(this.questions[i].id === id){
                    this.questions.splice(i, 1);
                    break;
                }
            }
        },
        // ajoute une question à la liste des questions chargées
        addQuestion(question){
            this.questions.push(question);
            this.add = false;
        }
    }
}
</script>