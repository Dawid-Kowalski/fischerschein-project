$(document).ready(function() {
    $('.selectpicker').selectpicker();

    setLanguageFlag = () => {
        const languageDe = document.querySelector('#language-de');
        const languagePl = document.querySelector('#language-pl');
        const innerCountryFlag = document.querySelector('.filter-option-inner-inner');

        if(languageDe.selected == true){
            let span = document.createElement('span');
            innerCountryFlag.firstChild.remove();
            span.classList.add('flag-icon', 'flag-icon-de');
            innerCountryFlag.appendChild(span);
        }
        if(languagePl.selected==true){
            let span = document.createElement('span');
            innerCountryFlag.firstChild.remove();
            span.classList.add('flag-icon', 'flag-icon-pl');
            innerCountryFlag.appendChild(span);
        }
    }

    makeTranslate = () => {
        const languageDe = document.querySelector('#language-de');
        const languagePl = document.querySelector('#language-pl');
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