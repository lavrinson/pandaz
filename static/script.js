document.addEventListener('DOMContentLoaded', function() {
    const clickButton = document.getElementById('click-button');
    const clicksCount = document.getElementById('clicks-count');

    clickButton.addEventListener('click', async function() {
        try {
            const response = await fetch('/update_clicks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({})
            });
            const data = await response.json();
            if (response.ok) {
                clicksCount.textContent = `Clicks: ${data.clicks}`;
            } else {
                console.error(data.error);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });
});
