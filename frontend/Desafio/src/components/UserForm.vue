<template>
  <div class="container mt-4">
    <h2>Cadastrar Usuário</h2>
    <form @submit.prevent="salvar">
      <div class="mb-3">
        <label>Nome</label>
        <input type="text" class="form-control" v-model="nome" required minlength="2">
      </div>
      <div class="mb-3">
        <label>Email</label>
        <input type="email" class="form-control" v-model="email" required>
      </div>
      <div class="mb-3">
        <label>Idade</label>
        <input type="number" class="form-control" v-model="idade" required min="1" max="120">
      </div>
      <button type="submit" class="btn btn-primary">Salvar</button>
    </form>
  </div>
</template>

<script>
import api from '../services/api';

export default {
  data() {
    return {
      nome: '',
      email: '',
      idade: null
    };
  },
  methods: {
    async salvar() {
      await api.post('/usuarios/', {
        nome: this.nome,
        email: this.email,
        idade: this.idade
      });
      alert('Usuário criado com sucesso!');
      this.nome = '';
      this.email = '';
      this.idade = null;
    }
  }
};
</script>
