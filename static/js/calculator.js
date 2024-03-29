document.addEventListener('DOMContentLoaded', function() {
    let display = document.querySelector('#display');
    let buttons = document.querySelectorAll('button');

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            let buttonText = this.innerText;
            let operators = ["+", "-", "*", "/", "%"]

            if (buttonText == '=') {
                let expression = display.value;
                let csrfToken = getCookie('csrftoken');  // Obtain CSRF token
                let form = document.getElementById('calculator-form');

                fetch('/calc/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    },
                    body: JSON.stringify({'expression': expression})
                })
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        display.value = 'Error';
                    } else {
                        display.value = data.result;
                    }
                });
            } else if (buttonText == 'C') {
                display.value = '';
            } else if (buttonText == 'Del') {
                display.value = display.value.slice(0,-1);
            } else if (operators.includes(display.value[display.value.length - 1]) && operators.includes(buttonText)) {
                display.value = display.value.slice(0,-1) + buttonText
            // } else if (display.value === "0" ) {
            //     display.value = buttonText
            } else {
                display.value += buttonText
            }

        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
