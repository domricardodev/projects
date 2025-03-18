// document se refere ao html
// querySelector seleciona um elemento do html (ex: a class declarada no button - '.button-add-task')
const button = document.querySelector('.button-add-task');
const input = document.querySelector('.input-task');
const completeList = document.querySelector('.list-tasks')

// declaração de array para salvar tarefas inputadas pelo usuário.
let myItemList = []

// Função para captar o input da tarefa e salvar no array [myItemList]
function addNewTask() {
  myItemList.push({
    task: input.value,
    done: false
  });
  input.value = ''
  showTasks();
}


function showTasks() {
  let newLi = ''

  myItemList.forEach((item, index) => {
    newLi = newLi + `
    
        <li class="tasks ${item.done && "done"}">
          <img src="./img/checked.png" alt="check-na-tarefa" onclick="doneTask(${index})">
          <p>${item.task}</p>
          <img src="./img/trash.png" alt="tarefa-para-o-lixo" onclick="deleteItem(${index})">
        </li>
    
    `
  })

  // innerHTML permite add o que quiser no HTML
  completeList.innerHTML = newLi;

  // salva dados no local storage do navegador
  localStorage.setItem('list', JSON.stringify(myItemList))

}


function doneTask(index) {
  myItemList[index].done = !myItemList[index].done

  showTasks()
}


function deleteItem(index) {
  myItemList.splice(index, 1);
  showTasks()
}

function reloadTasks() {
  const localStorageTasks = localStorage.getItem('list')

  if (localStorageTasks) {
    myItemList = JSON.parse(localStorageTasks)
  }

  showTasks()
}

reloadTasks()

// addEventListener fica de olho nas interacões com o botão, como declarado abaixo, no click do botão.
// E chama a função declarada acima para adicionar nova tarefa.
button.addEventListener('click', addNewTask);