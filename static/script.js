document.getElementById('click-button').addEventListener('click', async () => {
    const button = document.getElementById('click-button');
    const clicksElement = document.getElementById('clicks');

    // Отключаем кнопку, чтобы предотвратить множественные запросы
    button.disabled = true;
    button.textContent = 'Обработка...';

    try {
        const response = await fetch('/update_clicks', { method: 'POST' });

        // Проверяем, что ответ успешный
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        // Парсим ответ в JSON
        const data = await response.json();
        clicksElement.textContent = data.clicks;
    } catch (error) {
        console.error('Ошибка при выполнении запроса:', error);
        clicksElement.textContent = 'Ошибка обновления кликов'; // Отображаем сообщение об ошибке пользователю
    } finally {
        // Восстанавливаем кнопку после завершения запроса
        button.disabled = false;
        button.textContent = 'Клик!';
    }
});
