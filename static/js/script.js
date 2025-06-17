document.getElementById('calcForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const a = document.getElementById('a').value;
    const b = document.getElementById('b').value;
    const operation = document.getElementById('operation').value;

    fetch('/Calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ a, b, operation })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('result').textContent = '';
            document.getElementById('error').textContent = data.error;
        } else {
            document.getElementById('error').textContent = '';
            document.getElementById('result').textContent = `Result: ${data.result}`;
        }
    })
    .catch(error => console.error('Error:', error));
});
