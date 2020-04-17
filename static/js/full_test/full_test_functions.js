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

prepareTest = () => {
    const selectedQuestion = makeSelectedQuestionsData();
    console.log(selectedQuestion);
}

prepareTest()