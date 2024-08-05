const boton = document.querySelector('button')
const input = document.querySelector('input')
const ul = document.querySelector('ul')

function onClick(event){
    event.preventDefault();
    const li = document.createElement('li')
    const p = document.createElement('p')
    const checked = document.createElement('img')
    const deletebtn = document.createElement('button')
    checked.setAttribute('src','./images/unchecked.png')
    checked.setAttribute('class','checkedIcon')
    p.textContent = input.value
    deletebtn.textContent ='x'
    deletebtn.setAttribute('class','li-button')
    li.appendChild(checked)
    li.appendChild(p)
    li.appendChild(deletebtn)
    ul.appendChild(li)

    // Add event listener to the delete button
    deletebtn.addEventListener('click', function() {
        ul.removeChild(li);
    });
}

boton.addEventListener("click",onClick)