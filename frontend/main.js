const boton = document.querySelector('button')
const input = document.querySelector('input')
const ul = document.querySelector('ul')

function onClick(event){
    event.preventDefault();
    if (input.value !== ""){
        const li = document.createElement('li')
        const div = document.createElement('div')
        const p = document.createElement('p')
        const checked = document.createElement('img')
        const deletebtn = document.createElement('button')
        checked.setAttribute('src','./images/unchecked.png')
        checked.setAttribute('class','checkedIcon')
        p.textContent = input.value
        input.value = ""
        deletebtn.textContent ='x'
        deletebtn.setAttribute('class','li-button')
        div.appendChild(checked)
        div.appendChild(p)
        li.appendChild(div)
        li.appendChild(deletebtn)
        ul.appendChild(li)

        // Add event listener to the delete button
        deletebtn.addEventListener('click', function() {
            ul.removeChild(li);
        });
        div.addEventListener('click',function() {
        if (p.getAttribute('class') === ''){
           p.setAttribute('class', 'p-line-through') 
           checked.setAttribute('src','./images/checked.png')}
        else {
            p.setAttribute('class', '')
            checked.setAttribute('src','./images/unchecked.png')}
        }
           
        );
    
    }
}

boton.addEventListener("click",onClick)