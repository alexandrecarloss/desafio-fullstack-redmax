<template>
  <div class="container mt-4">
    <h2>Lista de Usuários</h2>
    <table class="table table-bordered mt-3">
      <thead>
        <tr>
          <th>Nome</th>
          <th>Email</th>
          <th>Idade</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="usuario in usuarios" :key="usuario.id">
          <td>{{ usuario.nome }}</td>
          <td>{{ usuario.email }}</td>
          <td>{{ usuario.idade }}</td>
          <td>
            <button class="btn btn-warning btn-sm me-2" @click="abrirModal(usuario)">Editar</button>
            <button class="btn btn-danger btn-sm" @click="excluir(usuario.id)">Excluir</button>
          </td>
        </tr>
      </tbody>
    </table>

    <ModalEditUser :usuarioEdit="usuarioSelecionado" @onUpdated="atualizarUsuario" />
  </div>
</template>

<script>
import api from '../services/api';
import ModalEditUser from './ModalEditUser.vue';
import { ref } from 'vue';

export default {
  components: { ModalEditUser },
  setup() {
    const usuarios = ref([]);
    const usuarioSelecionado = ref(null);

    async function carregarUsuarios() {
      const res = await api.get('/usuarios/');
      usuarios.value = res.data.data;
    }

    function abrirModal(usuario) {
      usuarioSelecionado.value = usuario;
    }

    function atualizarUsuario(usuarioAtualizado) {
      const index = usuarios.value.findIndex(u => u.id === usuarioAtualizado.id);
      if (index !== -1) {
        usuarios.value[index] = usuarioAtualizado;
      }
    }

    async function excluir(id) {
      await api.delete(`/usuarios/${id}/`);
      carregarUsuarios();
    }

    carregarUsuarios();

    return { usuarios, abrirModal, atualizarUsuario, excluir, usuarioSelecionado };
  }
}
</script>
