const button = document.createElement('button')
button.innerText = 'can you click me'
button.addEventListener('click', () => {
    alert('oh, you clicked me!')
})

document.body.appendChild(button)