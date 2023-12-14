document.addEventListener('DOMContentLoaded', function () {
    var links = document.querySelectorAll('.side-menu .nav-link');
    var sections = document.querySelectorAll('main section');

    function hideAllSections() {
        sections.forEach(function (section) {
            section.style.display = 'none';
        });
    }

    links.forEach(function (link) {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            hideAllSections();

            links.forEach(function (item) {
                item.classList.remove('active');
            });
            this.classList.add('active');

            var targetSection = document.querySelector(this.getAttribute('data-target'));
            if (targetSection) {
                targetSection.style.display = 'block';
            }
        });
    });

    // Inicialmente, esconde todas as seções e mostra apenas a primeira
    hideAllSections();
    sections[0].style.display = 'block';
    links[0].classList.add('active');
});

document.getElementById('form-abastecimento').addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const notificationElement = document.getElementById('notification');

    fetch('/abastecer', {
        method: 'POST',
        body: formData
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro na rede ao enviar os dados');
            }
            return response.json();
        })
        .then(data => {
            if (data.message === 'Número de requisição já está em uso') {
                notificationElement.textContent = 'Número de requisição já está em uso.';
                notificationElement.style.display = 'block';
                notificationElement.style.backgroundColor = 'red';
                notificationElement.style.color = 'white';
            } else {
                notificationElement.textContent = 'Dados cadastrados com sucesso!';
                notificationElement.style.display = 'block';
                notificationElement.style.backgroundColor = 'green';
                notificationElement.style.color = 'white';

                // Limpar o formulário
                this.reset();
            }

            // Ocultar notificação após um tempo
            setTimeout(() => {
                notificationElement.style.display = 'none';
            }, 5000);
        })
        .catch(error => {
            // Exibir mensagem de erro
            notificationElement.textContent = error.message || 'Erro ao enviar o formulário.';
            notificationElement.style.display = 'block';
            notificationElement.style.backgroundColor = 'red';
            notificationElement.style.color = 'white';

            // Ocultar notificação após um tempo
            setTimeout(() => {
                notificationElement.style.display = 'none';
            }, 5000);
        });
});

function searchRequisitions() {
    const searchField = document.getElementById('searchField').value;

    fetch('/get-requisitions')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.getElementById('requisitionsTable').getElementsByTagName('tbody')[0];
        tableBody.innerHTML = ''; // Limpar tabela atual

        data.forEach(requisition => {
            if (requisition.numero_requisicao.includes(searchField)) {
                const row = tableBody.insertRow();
                Object.values(requisition).forEach(text => {
                    const cell = row.insertCell();
                    cell.textContent = text;
                });
            }
        });
    })
    .catch(error => console.error('Erro:', error));
}

// Carregar todas as requisições quando a página for carregada
document.addEventListener('DOMContentLoaded', function () {
    searchRequisitions();
});
