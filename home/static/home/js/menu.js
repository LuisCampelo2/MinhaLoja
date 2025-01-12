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
