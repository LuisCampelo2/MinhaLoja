# MinhaLoja - E-commerce em Django

Este é um projeto de e-commerce desenvolvido em Django. Ele permite que os usuários visualizem produtos, façam compras e gerenciem seus pedidos.

## Pré-requisitos

Antes de começar, você precisará de algumas dependências:

- [Python](https://www.python.org/downloads/) 3.x
- [Git](https://git-scm.com/) (opcional, para clonar o repositório pelo terminal)
- [GitDesktop](https://desktop.github.com/download/)

## Como rodar o projeto localmente

Siga os passos abaixo para rodar o projeto em seu ambiente local,Rode esses comandos(Powershell):

**Clone este Repositorio**

git clone https://github.com/LuisCampelo2/MinhaLoja
cd MinhaLoja

Ou, se preferir, acesse o [repositório no GitHub](https://github.com/LuisCampelo2/MinhaLoja) e clique no botão "Clone", como mostrado na imagem abaixo:


![Descrição da imagem](img-git/cloneGit.png)

Após clicar em "Open with GitHub Desktop", você poderá abrir o projeto diretamente no GitHub Desktop.


**Crie um ambiente virtual python (opcional,porém recomendado)**

python -m venv venv

**Ative seu ambinete virtual**

.venv\Scripts\activate

**Instale as dependências**

pip install -r requirements.txt

**Mude o nome do arquivo .env-example para .env e preencha as informções**

mv .env-example .env

**Aplique migraçoes no banco de dados**

python manage.py migrate

**Rode o servidor**

python manage.py runserver

**Acesse o projeto clicando nesse endereço que irá aparecer no terminal:**
http://127.0.0.1:8000


