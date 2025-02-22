document.getElementById('predictionForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    let area = document.getElementById('area').value;
    let bedrooms = document.getElementById('bedrooms').value;
    let bathrooms = document.getElementById('bathrooms').value;

    let response = await fetch('/predict', {
        method: 'POST',
        body: new URLSearchParams({ 'area': area, 'bedrooms': bedrooms, 'bathrooms': bathrooms }),
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    });

    let result = await response.json();
    document.getElementById('result').innerText = result.prediction ? `Estimated Price: ${result.prediction}` : "Error!";
});
