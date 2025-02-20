# Projeto Agenda Django

Este é um projeto de uma aplicação web de agenda de contatos desenvolvida com Django.

## Funcionalidades

- Cadastro de usuários
- Login e logout de usuários
- CRUD de contatos (criação, leitura, atualização e exclusão)
- Pesquisa de contatos
- Paginação de contatos
- Upload de imagens para os contatos

## Estrutura do Projeto

- `base_static/`: Arquivos estáticos globais (CSS, JS, imagens)
- `base_templates/`: Templates HTML globais
- `contact/`: Aplicação principal com modelos, views, forms e templates específicos
- `core/`: Configurações e URLs do projeto
- `media/`: Diretório para upload de arquivos
- `static/`: Diretório para arquivos estáticos coletados
- `utils/`: Scripts utilitários

## Site Hospedado
Acesse a aplicação em `https://agendaotaviossousa.pythonanywhere.com/`.

## Scripts Utilitários

- `utils/create_contacts.py`: Cria contatos aleatórios para teste