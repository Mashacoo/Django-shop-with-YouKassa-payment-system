document.addEventListener("DOMContentLoaded", function() {
    // Получаем все ссылки в меню
    var menuLinks = document.querySelectorAll('.menu-link');
    var menuItems = document.querySelectorAll('.menu-item');
    var orderBlocks = document.querySelectorAll('.Order-block');

    // Обходим все ссылки и назначаем обработчик клика
    menuLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Предотвращаем стандартное действие ссылки

            // Удаляем класс у всех пунктов меню
            menuItems.forEach(function(item) {
                item.classList.remove('menu-item_ACTIVE');
            });

            // Добавляем класс ACTIVE к текущему пункту меню
            link.parentNode.classList.add('menu-item_ACTIVE');

            // Получаем значение атрибута href ссылки, например, "#step1"
            var targetId = link.getAttribute('href');

            // Находим элемент с соответствующим ID
            var targetElement = document.querySelector(targetId);

            if (targetElement) {
                // Прокручиваем страницу к найденному элементу
                targetElement.scrollIntoView({
                    behavior: 'smooth' // Добавляем плавную прокрутку
                });
            }

            // Обходим все блоки формы и скрываем их
            orderBlocks.forEach(function(block) {
                block.classList.remove('Order-block_OPEN');
            });

            // Находим блок формы с соответствующим ID и отображаем его
            var targetBlock = document.querySelector(targetId);
            if (targetBlock) {
                targetBlock.classList.add('Order-block_OPEN');
            }
        });
    });
});