let openSearchListLocationBtn = document.getElementById('location-btn');
let openSearchListTopicnBtn = document.getElementById('topic-btn');

let locationList = document.getElementById('location-list');
let topicList = document.getElementById('topic-list');


let searchConditionList = document.getElementById('search-condition');
let searchCheckboxList = document.querySelectorAll('.checkbox');

openSearchListLocationBtn.addEventListener('click', function () {
    if (locationList.dataset.open == '0') {
        if (topicList.dataset.open == '1') {
            topicList.dataset.open = '0';
            topicList.style.display = 'none';
        }
        locationList.dataset.open = '1';
        locationList.style.display = 'flex';
    } else {
        locationList.dataset.open = '0';
        locationList.style.display = 'none';
    }
});

openSearchListTopicnBtn.addEventListener('click', function () {
    if (topicList.dataset.open == '0') {
        if (locationList.dataset.open == '1') {
            locationList.dataset.open = '0';
            locationList.style.display = 'none';
        }
        topicList.dataset.open = '1';
        topicList.style.display = 'flex';
    } else {
        topicList.dataset.open = '0';
        topicList.style.display = 'none';
    }
});

searchCheckboxList.forEach(function (chechBoxInstance) {
    chechBoxInstance.addEventListener('click',
        function () {
            console.log('111');
            console.log(chechBoxInstance);
            if (chechBoxInstance.dataset.checked == '0') {
                let checkedItem = document.createElement("div")
                checkedItem.innerText = chechBoxInstance.textContent;
                checkedItem.className = 'checked-item';
                checkedItem.id = 'topic_checkbox_chacked_item_' + chechBoxInstance.id.split('_')[-1];
                searchConditionList.appendChild(checkedItem);
                chechBoxInstance.dataset.checked = '1';
            } else {
                let checkedItem = document.getElementById('topic_checkbox_chacked_item_' + chechBoxInstance.id.split('_')[-1]);
                checkedItem.remove();
                chechBoxInstance.dataset.checked = '0';
            }

        }
    )
});