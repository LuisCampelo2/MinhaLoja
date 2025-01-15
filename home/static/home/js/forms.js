document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('edit-user-form');

    // Armazena os valores iniciais dos campos
    const initialFormData = new FormData(form);

    form.addEventListener('submit', function (e) {
        e.preventDefault(); // Impede o envio padrão do formulário

        const currentFormData = new FormData(form);
        const modifiedFields = new FormData();

        // Compara os valores atuais com os iniciais
        for (let [key, value] of currentFormData.entries()) {
            if (value !== initialFormData.get(key)) {
                modifiedFields.append(key, value);
            }
        }

        // Inclui o token CSRF
        modifiedFields.append('csrfmiddlewaretoken', currentFormData.get('csrfmiddlewaretoken'));

        // Envia apenas os campos alterados
        fetch(form.action, {
            method: 'POST',
            body: modifiedFields,
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Alterações salvas com sucesso!');
                    window.location.reload();
                } else {
                    alert('Erro ao salvar alterações.');
                }
            })
            .catch(error => console.error('Erro:', error));
    });
});
