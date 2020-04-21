$(document).ready(function() {
    $('.selectpicker').selectpicker();

    changeLanguage = () => {
        const languageDe = document.querySelector('#language-de');
        const languagePl = document.querySelector('#language-pl');

        if(languageDe.selected == true){
            localStorage.setItem('language','de');
        }
        if(languagePl.selected==true){
            localStorage.setItem('language','pl');
        }
        setLanguageFlag();
        makeTranslate();
    }

    const language = document.querySelector('#language-select');
    const languageDeOption = document.querySelector('#language-de');
    const languagePlOption = document.querySelector('#language-pl');

    language.addEventListener('change',changeLanguage);

    if(localStorage.getItem('language')==null || localStorage.getItem('language')=='de'){
        languagePlOption.selected = false;
        languageDeOption.selected = true;
        localStorage.setItem('language','de');
    } else {
        languageDeOption.selected = false;
        languagePlOption.selected = true;
        localStorage.setItem('language','pl');
    }
    setLanguageFlag();
    makeTranslate();

});