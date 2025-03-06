
const button = document.createElement('button')
button.innerText = 'can you click me'

button.id = 'mainButton'
button.addEventListener('click', () => {
    alert('oh, you clicked me!');
})

//grabs the weather data from the json file
function getJsonData() {
    fetch('data.json')
    .then(Response =>{ 
    
        if (!Response.ok) {
            throw new Error('Network response was not ok');
        }
        return Response.json();
    })
    .then(data => document.getElementById("result").textContent = data.region)
    .catch(error => {
        console.error('Error reading json file: ', error)
    });
}