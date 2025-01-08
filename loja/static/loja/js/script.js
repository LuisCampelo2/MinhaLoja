document.addEventListener("DOMContentLoaded", function () {
    const menuHamburguer = document.getElementById("menu-hamburguer");
    const menuLateral = document.getElementById("menu-lateral");
    const closeBtn = document.getElementById("close-btn");

    // Abre o menu ao clicar no ícone
    menuHamburguer.addEventListener("click", function () {
        menuLateral.style.left = "0"; // Move o menu para dentro da tela
    });

    // Fecha o menu ao clicar no botão de fechar
    closeBtn.addEventListener("click", function () {
        menuLateral.style.left = "-250px"; // Move o menu para fora da tela
    });
});
