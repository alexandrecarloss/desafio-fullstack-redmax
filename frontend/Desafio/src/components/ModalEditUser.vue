<template>
  <div class="modal fade" tabindex="-1" ref="modalRef" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <form @submit.prevent="salvar">
          <div class="modal-header">
            <h5 class="modal-title">Editar Usuário</h5>
            <button type="button" class="btn-close" @click="fechar" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="mb-3">
              <label>Nome</label>
              <input type="text" class="form-control" v-model="usuario.nome" required minlength="2" />
            </div>
            <div class="mb-3">
              <label>Email</label>
              <input type="email" class="form-control" v-model="usuario.email" required />
            </div>
            <div class="mb-3">
              <label>Idade</label>
              <input type="number" class="form-control" v-model="usuario.idade" required min="1" max="120" />
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="fechar">Cancelar</button>
            <button type="submit" class="btn btn-primary">Salvar</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch, onMounted } from 'vue';
import * as bootstrap from 'bootstrap';
import api from '../services/api';

export default {
  props: {
    usuarioEdit: Object
  },
  emits: ['updated'],
  setup(props, { emit }) {
    const modalRef = ref(null);
    const bsModal = ref(null);
    const usuario = ref({ nome: '', email: '', idade: null });

    onMounted(() => {
      bsModal.value = new bootstrap.Modal(modalRef.value);
    });

    watch(() => props.usuarioEdit, (novoUsuario) => {
      if (novoUsuario && bsModal.value) {
        usuario.value = { ...novoUsuario };
        bsModal.value.show();
      }
    });

    function fechar() {
      bsModal.value?.hide();
    }

    async function salvar() {
      try {
        const res = await api.put(`/usuarios/${usuario.value.id}/`, usuario.value);
        emit('updated', res.data.data); 
        fechar();
        alert('Usuário atualizado com sucesso!');
      } catch (err) {
        alert('Erro ao atualizar usuário');
        console.log(err);
      }
    }

    return { modalRef, usuario, fechar, salvar };
  }
}
</script>
