shuffleQuestionsAnswer = () => {
    const array = [0,1,2];
    array.sort(()=>Math.random()-0.5);
    return array;
}