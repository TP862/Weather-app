const button = document.createElement('button')
button.innerText = 'can you click me'

button.id = 'mainButton'
button.addEventListener('click', () => {
    alert('oh, you clicked me!');
})

document.body.appendChild(button)

function showAlert() {
    alert("clicky clacky");
}

function showText() {
    document.getElementById("displayedText").textContent = "Hello World"
}

//takes what user puts in text box and outputs that text into a paragraph
function getUserInput() {
    const cityName = document.getElementById("cityName").value;
    document.getElementById("result").textContent = cityName;
}

//function to set contents of the paragraph
function setResult(input) {
    document.getElementById("result").textContent = input;
}

//grabs the weather data from the json file
function getJsonData() {
    fetch('data.json')
    .then(Response =>{ 
    
        if (!Response.ok) {
            throw new Error('Network response was not ok');
        }
        return Response.json();
    })
    .then(data => document.getElementById("result").textContent = data.temp)
    .catch(error => {
        console.error('Error reading json file: ', error)
    });
}