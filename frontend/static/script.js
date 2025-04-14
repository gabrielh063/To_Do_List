const taskList = document.getElementById('task-list');
const form = document.getElementById('task-form');
const titleInput = document.getElementById('title');
const descInput = document.getElementById('desc');

const API_URL = '/tasks';

async function loadTasks() {
  taskList.innerHTML = '';
  const res = await fetch(API_URL);
  const tasks = await res.json();

  tasks.forEach(task => {
    const card = document.createElement('div');
    card.className = 'card';

    card.innerHTML = `
      <div class="checkbox">
        <input type="checkbox" id="is_done_${task.ID_TASK}" ${task.TASK_IS_DONE ? 'checked' : ''} onchange="toggleTaskStatus(${task.ID_TASK})">
      </div>
      <h3>${task.TASK_TITLE}</h3>
      <p>${task.TASK_DESC}</p>
      <p>Status: ${task.TASK_IS_DONE ? 'Concluída' : 'Pendente'}</p>
      <div class="card-buttons">
        <button onclick="deleteTask(${task.ID_TASK})">Excluir</button>
        <button onclick="openEditModal(${task.ID_TASK})">Editar</button>
      </div>
    `;

    taskList.appendChild(card);
  });
}

async function toggleTaskStatus(id) {
  const checkbox = document.getElementById(`is_done_${id}`);
  const isDone = checkbox.checked;

  const updatedTask = {
    TASK_IS_DONE: isDone
  };

  await fetch(`${API_URL}/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(updatedTask)
  });

  loadTasks();
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  if (!titleInput.value.trim()) {
    alert('O título é obrigatório!');
    return;
  }

  const task = {
    TASK_TITLE: titleInput.value,
    TASK_DESC: descInput.value || '',
    TASK_IS_DONE: false
  };

  await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(task)
  });

  titleInput.value = '';
  descInput.value = '';
  loadTasks();
});

async function deleteTask(id) {
  await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
  loadTasks();
}

function openEditModal(taskId) {
  fetch(`/tasks/${taskId}`)
    .then(response => response.json())
    .then(data => {
      document.getElementById('editTitle').value = data.TASK_TITLE;
      document.getElementById('editDesc').value = data.TASK_DESC;
      document.getElementById('editStatus').checked = data.TASK_IS_DONE;

      document.getElementById('editTaskForm').onsubmit = function(event) {
        event.preventDefault();
        updateTask(taskId);
      };

      document.getElementById('editTaskModal').style.display = 'flex';
    })
    .catch(error => console.log('Erro ao carregar dados da tarefa:', error));
}

function closeModal() {
  document.getElementById('editTaskModal').style.display = 'none';
}

document.getElementById('editTaskModal').addEventListener('click', function(event) {
  if (event.target === document.getElementById('editTaskModal')) {
    closeModal();
  }
});

function updateTask(taskId) {
  const title = document.getElementById('editTitle').value;
  const description = document.getElementById('editDesc').value;
  const status = document.getElementById('editStatus').checked;

  const updatedData = {};
  if (title !== '') updatedData.TASK_TITLE = title;
  if (description !== '') updatedData.TASK_DESC = description;
  updatedData.TASK_IS_DONE = status;

  fetch(`/tasks/${taskId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(updatedData)
  })
    .then(response => response.json())
    .then(data => {
      if (data.message) {
        alert(data.message);
        closeModal();
        loadTasks();
      } else {
        alert('Erro ao atualizar tarefa');
      }
    })
    .catch(error => console.log('Erro ao atualizar a tarefa:', error));
}

loadTasks();
