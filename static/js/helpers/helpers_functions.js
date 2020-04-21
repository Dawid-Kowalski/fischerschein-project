shuffleQuestionsAnswer = () => {
    const array = [0,1,2];
    array.sort(()=>Math.random()-0.5);
    return array;
}


setLanguageFlag = () => {
    const languageDe = document.querySelector('#language-de');
    const languagePl = document.querySelector('#language-pl');
    const innerCountryFlag = document.querySelector('.filter-option-inner-inner');

    if(languageDe.selected == true){
        let span = document.createElement('span');
        if(innerCountryFlag.firstChild != null){
            innerCountryFlag.firstChild.remove();
        }
        span.classList.add('flag-icon', 'flag-icon-de');
        innerCountryFlag.appendChild(span);
    }
    if(languagePl.selected==true){
        let span = document.createElement('span');
        if(innerCountryFlag.firstChild != null){
            innerCountryFlag.firstChild.remove();
        }
        span.classList.add('flag-icon', 'flag-icon-pl');
        innerCountryFlag.appendChild(span);
    }
}

makeTranslate = () => {
    const languageDe = document.querySelector('#language-de');
    const textsDe = document.querySelectorAll('span[data-translate-text-de="true"]');
    const textsPl = document.querySelectorAll('span[data-translate-text-pl="true"]');

    if(languageDe.selected == true) {
        for(let i=0;i<textsDe.length;i++){
            textsDe[i].style.display = 'inline';
        }
        for(let i=0;i<textsPl.length;i++){
            textsPl[i].style.display = 'none';
        }
    } else {
        for(let i=0;i<textsDe.length;i++){
            textsDe[i].style.display = 'none';
        }
        for(let i=0;i<textsPl.length;i++){
            textsPl[i].style.display = 'inline';
        }
    }
}