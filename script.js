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

function getUserInput() {

    const cityName = document.getElementById("cityName").value;

    document.getElementById("result").textContent = cityName;
}