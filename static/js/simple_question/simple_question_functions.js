uncheckedRadios = () => {
    document.querySelector('#answer-A').checked = false;
    document.querySelector('#answer-B').checked = false;
    document.querySelector('#answer-C').checked = false;
}

shuffleQuestionsAnswer = () => {
    const array = [0,1,2];
    array.sort(()=>Math.random()-0.5);
    return array;
}

makeTooltip = (elementToAddTooltip,tooltipText) => {
    $(function(){
        $(`#${elementToAddTooltip}`).tooltip('dispose').tooltip({title:tooltipText}).tooltip();
    })
}

prepareQuestion = (question) => {
    document.querySelector('#question-id').textContent = question.questionId;
    document.querySelector('#main-topic-de').textContent = question.mainTopicGer + ' ';
    makeTooltip('main-topic-pl',question.mainTopicPl);
    document.querySelector('#under-topic-de').textContent = question.underTopicGer + ' ';
    makeTooltip('under-topic-pl',question.underTopicPl);
    document.querySelector('#question-de').textContent = question.questionGer;
    makeTooltip('question-pl',question.questionPl);

    const shuffledAnswerIndexs = shuffleQuestionsAnswer(); // returns array 0,1,2 in random order
    document.querySelector('#answer-A-label').textContent = question.answersGer[shuffledAnswerIndexs[0]];
    document.querySelector('#answer-B-label').textContent = question.answersGer[shuffledAnswerIndexs[1]];
    document.querySelector('#answer-C-label').textContent = question.answersGer[shuffledAnswerIndexs[2]];

    document.querySelector('#answer-A').value = question.answersGer[shuffledAnswerIndexs[0]];
    makeTooltip('answer-A-pl',question.answersPl[shuffledAnswerIndexs[0]]);
    document.querySelector('#answer-B').value = question.answersGer[shuffledAnswerIndexs[1]];
    makeTooltip('answer-B-pl',question.answersPl[shuffledAnswerIndexs[1]]);
    document.querySelector('#answer-C').value = question.answersGer[shuffledAnswerIndexs[2]];
    makeTooltip('answer-C-pl',question.answersPl[shuffledAnswerIndexs[2]]);
    
    uncheckedRadios();
}

drawQuestion = () => {
    const randomNumber = Math.floor(Math.random() * 600) + 1;
    const questions = makeQuestionsData();
    const simpleQuestion = questions[randomNumber];
    prepareQuestion(simpleQuestion);
}

getUserAnswer = () => {
    let userAnswer;
    try {
        userAnswer = document.querySelector('input[name="answers"]:checked').value;
    }
    catch (err){
        userAnswer = 'no answer';
    }
    return userAnswer;
}

checkQuestion = () => {
    const userAnswer = getUserAnswer();
    const questionId = parseInt(document.querySelector('#question-id').textContent);
    const allQuestions = makeQuestionsData();
    const correctAnswer = allQuestions[questionId-1].correctAnswerGer; // index in array from 0, questions from 1
    const modalBody = document.querySelector('#check-result-modal-body');
    userAnswer == correctAnswer ? modalBody.textContent= 'correct' : modalBody.textContent = 'false';
    $('#check-question-modal').modal()
}

const drawNewQuestionButton = document.querySelector('#draw-new-question-btn');
drawNewQuestionButton.addEventListener('click',drawQuestion);

const checkQuestionButton = document.querySelector('#check-question-btn');
checkQuestionButton.addEventListener('click',checkQuestion);

const modalNewQuestionBtn = document.querySelector('#modal-new-question-btn');
modalNewQuestionBtn.addEventListener('click',drawQuestion);

drawQuestion();