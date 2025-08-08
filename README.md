# Desafio Fullstack RedMax - Sistema de Usuários

## 📋 Descrição do Desafio

Desenvolva uma aplicação fullstack simples para gerenciar usuários, contendo backend com API REST e frontend para consumir essa API, tudo dockerizado.

## 🎯 Objetivos

Criar um sistema básico de CRUD de usuários com as seguintes funcionalidades:

- Listar usuários
- Cadastrar novo usuário
- Excluir usúario
- Interface web para interagir com a API

## 🛠️ Requisitos Técnicos

### Backend (Escolha uma das opções)

- **Node.js** com Express/NestJS
- **Python** com Flask/FastAPI/Django
- **Java** com Spring Boot

### Frontend (Escolha uma das opções)

- **React**
- **Vue.js**
- **Angular.js**
- **Next.js**
- **HTML/CSS/JavaScript**

### Banco de Dados

- SQLite (para simplicidade)
- Ou PostgreSQL

## 📊 Estrutura de Dados

### Usuário

```json
{
  "id": 1,
  "nome": "João Silva",
  "email": "joao@email.com",
  "idade": 30,
  "created_at": "2024-01-15T10:30:00Z"
}
```

## 🔌 Rotas da API

### 1. **GET /api/usuarios**

- **Descrição**: Lista todos os usuários
- **Resposta**: Array de usuários
- **Status**: 200

```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "nome": "João Silva",
      "email": "joao@email.com",
      "idade": 30,
      "created_at": "2024-01-15T10:30:00Z"
    }
  ]
}
```

### 2. **POST /api/usuarios**

- **Descrição**: Cadastra um novo usuário
- **Body**:

```json
{
  "nome": "Maria Santos",
  "email": "maria@email.com",
  "idade": 25
}
```

- **Resposta**: Usuário criado
- **Status**: 201

````json
{
  "success": true,
  "message": "Usuário criado com sucesso",
  "data": {
    "id": 2,
    "nome": "Maria Santos",
    "email": "maria@email.com",
    "idade": 25,
    "created_at": "2024-01-15T11:00:00Z"
  }
}

### 3. **DELETE /api/usuarios**

- **Descrição**: Deleta um  usuário
- **Body**:
```json
{
  "nome": "Maria Santos",
  "email": "maria@email.com",
  "idade": 25
}
````

- **Resposta**: Usuário criado
- **Status**: 201

```json
{
  "success": true,
  "message": "Usuário criado com sucesso",
  "data": {
    "id": 2,
    "nome": "Maria Santos",
    "email": "maria@email.com",
    "idade": 25,
    "created_at": "2024-01-15T11:00:00Z"
  }
}
```

## 🖥️ Interface Frontend

### Páginas Necessárias:

1. **Lista de Usuários**

   - Tabela mostrando todos os usuários
   - Botão para adicionar novo usuário

2. **Formulário de Cadastro**
   - Campos: Nome, Email, Idade
   - Validação básica
   - Botão de salvar

### Validações:

- Nome: obrigatório, mínimo 2 caracteres
- Email: obrigatório, formato válido
- Idade: obrigatório, número entre 1 e 120

## 🐳 Docker

### Requisitos:

1. **Dockerfile** para o backend
2. **Dockerfile** para o frontend
3. **docker-compose.yml** para orquestrar os serviços

### Estrutura esperada:

```
projeto/
├── backend/
│   ├── Dockerfile
│   ├── src/
│   └── package.json (ou requirements.txt)
├── frontend/
│   ├── Dockerfile
│   ├── src/
│   └── package.json
├── docker-compose.yml
└── README.md
```

### Portas:

- Backend: 3001(Pode deixar porta padrão de framework)
- Frontend: 3000(Pode deixar porta padrão de framework)
- Banco (se PostgreSQL): 5432

## 📝 Entregáveis

1. **Código fonte** completo (backend + frontend)
2. **Dockerfiles** funcionais
3. **docker-compose.yml** configurado
4. **README.md** com:
   - Instruções de como executar
   - Tecnologias utilizadas
   - Endpoints da API
   - Screenshots da aplicação (opcional)

## 🚀 Como Executar

O projeto deve funcionar com apenas um comando:

```bash
docker-compose up --build
```

Após executar:

- Frontend acessível em: http://localhost:3000(dependendo do framework)
- Backend acessível em: http://localhost:3001 (dependendo do framework)

## ✅ Critérios de Avaliação

### Obrigatórios (70 pontos)

- [ ] Backend com 2 rotas funcionais (20 pts)
- [ ] Frontend consumindo a API (20 pts)
- [ ] Docker funcionando corretamente (20 pts)
- [ ] Validações básicas (10 pts)

### Diferenciais (30 pontos)

- [ ] Tratamento de erros (10 pts)
- [ ] Interface responsiva (5 pts)
- [ ] Código bem documentado (5 pts)
- [ ] Testes unitários (5 pts)
- [ ] Design clean e intuitivo (5 pts)

## ⏱️ Prazo

**3 dias** a partir do recebimento do desafio.

## 📤 Entrega

Enviar o link do repositório Git (GitHub, GitLab, etc.) para Responsável do processo

**Assunto**: `[Desafio Fullstack] - Seu Nome`

---

## 💡 Dicas

- Comece pelo backend e teste as rotas
- Use ferramentas como Postman para testar a API
- Mantenha o código simples e funcional
- Documente as decisões técnicas no README
- Teste o Docker antes de enviar

**Boa sorte! 🚀**

---
