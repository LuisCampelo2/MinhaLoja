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

document.querySelector('.search-button').addEventListener('click', () => {
    const searchText = document.querySelector('.search-bar').value;
    alert(`Você buscou por: ${searchText}`);
});
// Animaçao de entrada no index
window.addEventListener("load", function () {
    const bemVindoDiv = document.querySelector(".bem-vindo");
    bemVindoDiv.classList.add("ativo"); // Adiciona a classe 'ativo' ao carregar a página
});
// Mostrar imagens do carrossel automaticamente
document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('.banner img');
    const prevButton = document.querySelector('.carousel-btn.prev');
    const nextButton = document.querySelector('.carousel-btn.next');
    let currentIndex = 0;
    const intervalTime = 3000; // Tempo entre as mudanças automáticas (em milissegundos)

    // Função para mostrar a imagem atual
    function showImage(index) {
        images.forEach((img, i) => {
            img.style.display = i === index ? 'block' : 'none';
        });
    }

    // Mostrar a primeira imagem inicialmente
    showImage(currentIndex);

    // Função para avançar para a próxima imagem
    function nextImage() {
        currentIndex = (currentIndex + 1) % images.length;
        showImage(currentIndex);
    }

    // Evento para botão "Próximo"
    nextButton.addEventListener('click', function () {
        nextImage();
        resetAutoSlide(); // Reinicia o temporizador ao clicar manualmente
    });

    // Evento para botão "Anterior"
    prevButton.addEventListener('click', function () {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        showImage(currentIndex);
        resetAutoSlide(); // Reinicia o temporizador ao clicar manualmente
    });

    // Configuração do temporizador para mudança automática
    let autoSlide = setInterval(nextImage, intervalTime);

    // Função para reiniciar o temporizador ao clicar manualmente
    function resetAutoSlide() {
        clearInterval(autoSlide);
        autoSlide = setInterval(nextImage, intervalTime);
    }
});


