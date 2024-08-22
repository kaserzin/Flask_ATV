# Sistema de Gerenciamento de Atletas, Times e Competições

## Descrição

Este projeto é uma aplicação web desenvolvida com Flask para gerenciar informações sobre atletas, times e competições de vôlei. O sistema permite a adição, edição e remoção de registros de atletas, times e competições. Utiliza um banco de dados SQLite para armazenar e manipular dados, fornecendo uma interface simples e eficiente para gestão de informações esportivas.

## Estrutura do Projeto

O projeto é dividido em várias partes, cada uma com uma funcionalidade específica:

- **`app.py`**: Arquivo principal que define as rotas da aplicação e a lógica de negócios para a gestão de atletas, times e competições.
- **`db.py`**: Contém as classes `Atleta`, `Time`, `Competicao` e `Arbitro` responsáveis pela manipulação do banco de dados SQLite. Cada classe define métodos para criar, listar, atualizar e remover registros.
- **`templates/`**: Diretório contendo os arquivos HTML que definem a interface do usuário. Inclui:
  - **`volei.html`**: Página que lista todos os atletas.
  - **`form_volei.html`**: Formulário para adicionar ou editar atletas.
  - **`times.html`**: Página que lista todos os times.
  - **`form_times.html`**: Formulário para adicionar ou editar times.
  - **`competicoes.html`**: Página que lista todas as competições.
  - **`form_competicoes.html`**: Formulário para adicionar ou editar competições.

## Recursos Utilizados

### Banco de Dados

O sistema utiliza um banco de dados SQLite, que é gerenciado pelas classes no arquivo `db.py`. O banco de dados armazena informações sobre atletas, times e competições em tabelas separadas, permitindo operações eficientes de CRUD (criação, leitura, atualização e exclusão).

### Templates HTML

Os templates HTML fornecem uma interface intuitiva para interação com o sistema. Eles são utilizados para exibir listas de atletas, times e competições, além de formulários para inserir e atualizar informações.

Exemplo de tabela na página `volei.html` para listar atletas:

```html
<table border="1">
  <thead>
    <tr>
      <th>ID</th>
      <th>Nome</th>
      <th>Posição</th>
      <th>Altura</th>
      <th>Ações</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>João Silva</td>
      <td>Atacante</td>
      <td>1.90m</td>
      <td>
        <a href="/editar/1">Editar</a>
        <a href="/remover/1">Remover</a>
      </td>
    </tr>
  </tbody>
</table>
```
### Arquivos CSS
O estilo do site é gerenciado através de arquivos CSS, que podem estar localizados na pasta /static/css/ se necessário. Estes arquivos controlam o layout e o design visual da aplicação, garantindo uma apresentação consistente e atraente.

### Implementação de Design Responsivo
O design da aplicação é responsivo, o que garante que a interface seja utilizável em dispositivos móveis, tablets e desktops. Isso é alcançado através de media queries no CSS, adaptando o layout conforme o tamanho da tela do dispositivo.

### Melhoria Contínua
O projeto é constantemente atualizado para melhorar a funcionalidade e a usabilidade. Sugestões e feedback dos usuários são bem-vindos para implementar melhorias e adicionar novas funcionalidades.

### Conclusão
Este sistema oferece uma plataforma eficiente para gerenciar informações de atletas, times e competições de vôlei. Com uma interface intuitiva e suporte para operações CRUD básicas, o projeto proporciona uma solução prática e fácil de usar para a gestão de dados esportivos.
