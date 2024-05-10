let subBtn = document.getElementById('sub_btn');

let btnActive = true;

if (subBtn) {
    subBtn.addEventListener('click', subFunc);
} 

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function showAlert(success = true) {
    let alertMsg = document.createElement('div');
    alertMsg.className = 'alert '
    if (success) {
        alertMsg.innerText = 'Успешно!';
        alertMsg.className += 'alert-success';
    } else {
        alertMsg.innerText = 'Ошибка!';
        alertMsg.className += 'alert-error';
    }

    document.body.appendChild(alertMsg);
    await sleep(3000);
    alertMsg.remove();
}

async function subFunc(event) {

    let user = getCookie('sessionid');
    console.log(user);

    if (!btnActive) return;
    btnActive = false

    let btn = event.srcElement

    if (btn.dataset.sub == 'sub') {
        let response = await sendRequest('sub', btn.dataset.pk);

        if (response.redirected) {
            window.location.href = response.url
            return
        }

        if (response.ok) {
            btn.textContent = 'Отписаться';
            btn.dataset.sub = 'un_sub';
            showAlert();
        } else {
            showAlert(false);
        }

    } else if (btn.dataset.sub == 'un_sub') {
        let response = await sendRequest('un_sub', btn.dataset.pk);

        if (response.redirected) {
            window.location.href = response.url
            return
        }

        if (response.ok) {
            btn.textContent = 'Подписаться';
            btn.dataset.sub = 'sub';
            showAlert();
        } else {
            showAlert(false);
        }

    }

    await sleep(2000);
    btnActive = true;

}

async function sendRequest(url, pk) {
    const csrfToken = getCookie('csrftoken');
    const response = await fetch('http://127.0.0.1:8000/' + url + '/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({'event': pk})
    })
    
    return response
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}