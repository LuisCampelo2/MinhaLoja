// Selecionando elementos
const menuHamburguer = document.getElementById('menu-hamburguer');
const menuLateral = document.getElementById('menu-lateral');
const closeBtn = document.getElementById('close-btn');

// Exibe o menu lateral
menuHamburguer.addEventListener('click', () => {
    menuLateral.classList.add('open');
});

// Fecha o menu lateral
closeBtn.addEventListener('click', () => {
    menuLateral.classList.remove('open');
});


//carrossel
const items = document.querySelectorAll('.carousel-item');
const prevBtn = document.querySelector('.carousel-btn.prev');
const nextBtn = document.querySelector('.carousel-btn.next');
let currentIndex = 0;

function updateCarousel(index) {
    items.forEach((item, i) => {
        item.classList.toggle('active', i === index);
    });
}

prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + items.length) % items.length;
    updateCarousel(currentIndex);
});

nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % items.length;
    updateCarousel(currentIndex);
});

// Inicializa o primeiro item como ativo
updateCarousel(currentIndex);

//barra de pesquisa
document.addEventListener('DOMContentLoaded', () => {
    const lupaBusca = document.getElementById('search-icon');
    const barraBusca = document.getElementById('search-container');

    if (lupaBusca && barraBusca) {
        lupaBusca.addEventListener('click', () => {
            if (barraBusca.style.display === 'none' || barraBusca.style.display === '') {
                barraBusca.style.display = 'block'; // Mostra a barra de busca
            } else {
                barraBusca.style.display = 'none'; // Esconde a barra de busca
            }
        });
    } else {
        alert('elemento nao encontrado')
    }
});
