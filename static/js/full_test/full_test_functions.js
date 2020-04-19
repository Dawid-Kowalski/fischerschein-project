let selectedQuestionsGlobal = [];

chooseQuestionBetween = (min,max) => {
    return Math.floor(Math.random()*(max-min+1))+min;
}

choose12uniqueQuestionBetween = (min,max) => {
    const questions = [];
    let newQuestion;
    do {
        newQuestion = chooseQuestionBetween(min,max);
        if(!questions.includes(newQuestion)){
            questions.push(newQuestion)
        }
    } while(questions.length != 12);

    return questions
}

chosseTestQuestionsIds = () => {
    const testQuestionsId = [];
    testQuestionsId.push(choose12uniqueQuestionBetween(0,119));
    testQuestionsId.push(choose12uniqueQuestionBetween(120,239));
    testQuestionsId.push(choose12uniqueQuestionBetween(240,359));
    testQuestionsId.push(choose12uniqueQuestionBetween(360,479));
    testQuestionsId.push(choose12uniqueQuestionBetween(480,599));

    return testQuestionsId;
}

makeSelectedQuestionsData = () => {
    const selectedQuestionIds = chosseTestQuestionsIds().flat(Infinity);
    const allQuestions = makeQuestionsData();

    const selectedQuestions = [];
    let newQuestion;

    for(i=0;i<selectedQuestionIds.length;i++){
        newQuestion= {};
        newQuestion.questionDe = allQuestions[selectedQuestionIds[i]].questionDe;
        newQuestion.questionPl = allQuestions[selectedQuestionIds[i]].questionPl;
        newQuestion.answersDe = allQuestions[selectedQuestionIds[i]].answersDe;
        newQuestion.answersPl = allQuestions[selectedQuestionIds[i]].answersPl;
        newQuestion.correctAnswerDe = allQuestions[selectedQuestionIds[i]].correctAnswerDe;
        newQuestion.mainTopicDe = allQuestions[selectedQuestionIds[i]].mainTopicDe;
        selectedQuestions.push(newQuestion);
    }

    selectedQuestionsGlobal = selectedQuestions;

    return selectedQuestions;
}

prepareDataQuestionToTemplate = () => {
    const questionData = makeSelectedQuestionsData();

    const dataToTemplate = {}
    dataToTemplate.questions =[];
    for(let i=0;i<questionData.length;i++){
        let question = {}
        let shuffledAnswerIndexs = shuffleQuestionsAnswer();

        question.questionId = i+1;
        question.mainTopicDe = questionData[i].mainTopicDe;
        question.questionDe = questionData[i].questionDe;
        question.questionPl = questionData[i].questionPl;
        question.answerAde = questionData[i].answersDe[shuffledAnswerIndexs[0]];
        question.answerBde = questionData[i].answersDe[shuffledAnswerIndexs[1]];
        question.answerCde = questionData[i].answersDe[shuffledAnswerIndexs[2]];
        question.answerApl = questionData[i].answersPl[shuffledAnswerIndexs[0]];
        question.answerBpl = questionData[i].answersPl[shuffledAnswerIndexs[1]];
        question.answerCpl = questionData[i].answersPl[shuffledAnswerIndexs[2]];
        question.correctAnswerDe = questionData[i].correctAnswerDe;

        dataToTemplate.questions.push(question);
    }
    return dataToTemplate
}

hideAllQuestions = () => {
    const allQuestionsDivs = document.querySelectorAll('div[data-topic]');
    for(let i=0;i<allQuestionsDivs.length;i++){
        allQuestionsDivs[i].style.display = 'none';
    }
}

showQuestionFromTopic = (topic) => {
    hideAllQuestions();
    const questionToShow = document.querySelectorAll(`div[data-topic="${topic}"]`);
    for(let i=0;i<questionToShow.length;i++){
        questionToShow[i].style.display = 'block';
    }
}

renderQuestions = () => {
    const questionTemplate = document.querySelector('#template-question').innerHTML;
    const data = prepareDataQuestionToTemplate();
    const rendered = Mustache.render(questionTemplate,data);
    document.querySelector('#test').innerHTML = rendered;
}

makeTooltips = () => {
    const tooltips = document.querySelectorAll("span[data-toggle='tooltip']");
    
    for(let i=0;i<tooltips.length;i++){
        $(function(){
            $(tooltips[i]).tooltip();
        })
    }
}

prepareTest = () => {
    renderQuestions();
    makeTooltips();
    hideAllQuestions();
    showQuestionFromTopic('Fischkunde und -hege');
}

const newTestButton = document.querySelector('#new-test-btn');
const showQuestions_1_Button = document.querySelector('#show-topic-1-questions-btn')
const showQuestions_2_Button = document.querySelector('#show-topic-2-questions-btn')
const showQuestions_3_Button = document.querySelector('#show-topic-3-questions-btn')
const showQuestions_4_Button = document.querySelector('#show-topic-4-questions-btn')
const showQuestions_5_Button = document.querySelector('#show-topic-5-questions-btn')

newTestButton.addEventListener('click',prepareTest);

showQuestions_1_Button.addEventListener('click',function(){
        showQuestionFromTopic('Fischkunde und -hege')
    }
);

showQuestions_2_Button.addEventListener('click',function(){
        showQuestionFromTopic('Pflege der Fischgewässer')
    }
);

showQuestions_3_Button.addEventListener('click',function(){
        showQuestionFromTopic('Fanggeräte und deren Gebrauch')
    }
);

showQuestions_4_Button.addEventListener('click',function(){
        showQuestionFromTopic('Behandlung der gefangenen Fische')
    }
);

showQuestions_5_Button.addEventListener('click',function(){
        showQuestionFromTopic('Einschlägige Rechtsvorschriften')
    }
);

prepareTest()