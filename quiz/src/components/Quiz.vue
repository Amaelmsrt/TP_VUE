<script>
import QuestionMultiple from './components/QuestionMultiple.vue'

export default {
    props: {
        quiz: Object
    },
}
</script>

<template>
    <h2>{{ quiz.nom }}</h2>
    <ol>
        <li v-for="question in quiz.questions">
            <QuestionMultiple :question="question"/>
        </li>
    </ol>
</template>