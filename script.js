document.getElementById('ganForm').addEventListener('submit', function(e) {
    e.preventDefault();
    var form = e.target;
    var formData = new FormData(form);

    fetch(form.action, {
        method: form.method,
        body: formData
    })
    .then(response => response.text())
    .then(result => {
        document.getElementById('resultOutput').textContent = result;
        document.getElementById('resultContainer').style.display = 'block';
    });
});