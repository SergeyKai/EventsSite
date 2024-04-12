let menuCallapseBtn = document.getElementById('menu-callapse');
let mainMenu = document.getElementById('main-menu');

menuCallapseBtn.addEventListener('click', function () {
    if (mainMenu.dataset.open == 0) {
        mainMenu.style.display = 'flex'
        mainMenu.dataset.open = 1
    } else if (mainMenu.dataset.open == 1) {
        mainMenu.style.display = 'none'
        mainMenu.dataset.open = 0
    }

})