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

    // Verifica se os elementos existem
    if (lupaBusca && barraBusca) {
        // Abre ou fecha a barra de busca
        lupaBusca.addEventListener('click', () => {
            barraBusca.classList.toggle('open'); // Alterna a classe 'open'
        });
    } else {
        alert('Elemento não encontrado');
    }
});
