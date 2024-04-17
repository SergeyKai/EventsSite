let subBtn = document.getElementById('sub_btn');
let unSubBtn = document.getElementById('un_sub_btn');

if (subBtn) {
    subBtn.addEventListener('click', subFunc);
} else if (unSubBtn) {
    unSubBtn.addEventListener('click', unSubFunc);

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

    document.body.appendChild(alertMsg)
    await sleep(3000)
    alertMsg.remove()
}

async function subFunc(event) {
    let btn = event.srcElement
    let response = await sendRequest('sub', btn.dataset.pk);
    if (response.ok) {
        btn.textContent = 'Отписаться';
        btn.id = 'un_sub_btn'
        btn.addEventListener('click', unSubFunc);
        showAlert()
    } else {
        showAlert(false)
    }
}

async function unSubFunc(event) {
    let btn = event.srcElement
    let response = await sendRequest('un_sub', btn.dataset.pk);
    if (response.ok) {
        btn.textContent = 'Подписаться';
        btn.id = 'sub_btn'
        btn.addEventListener('click', subFunc)
        showAlert()
    } else {
        showAlert(false)
    }
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