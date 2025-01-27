document.addEventListener("DOMContentLoaded", function () {
    const cartaoDeCredito = document.getElementById('cartao-de-credito');
    const pix = document.getElementById('PIX');
    const formCartaoDeCredito = document.getElementById('payment-form');
    const formPix = document.getElementById('pix-form');

    // Função para ocultar todos os formulários
    function hideAllForms() {
        if (formCartaoDeCredito)
            formCartaoDeCredito.classList.remove('open');
        if (formPix) 
            formPix.classList.remove('open');
    }

    // Verifique se os elementos existem antes de adicionar os eventos
    if (cartaoDeCredito && formCartaoDeCredito) {
        cartaoDeCredito.addEventListener('click', () => {
            hideAllForms(); // Oculta todos os formulários
            formCartaoDeCredito.classList.add('open'); // Exibe o formulário de cartão de crédito
        });
    }

    if (pix && formPix) {
        pix.addEventListener('click', () => {
            hideAllForms(); // Oculta todos os formulários
            formPix.classList.add('open'); // Exibe o formulário de PIX
        });
    }
});
