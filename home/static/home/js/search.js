//barra de pesquisa
document.addEventListener('DOMContentLoaded', () => {
    const lupaBusca = document.getElementById('icon-search');
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
