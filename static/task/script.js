let count = 1;

function add_input(){
    let form = document.getElementById('form');
    let  parent = document.querySelector('.test')
    let newDiv = parent.cloneNode(true)
    newDiv.getElementsByTagName('label')[0].innerText = `Input data ${count}:`
    document.getElementById('form').appendChild(newDiv)
    count++;


}

