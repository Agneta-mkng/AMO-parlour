<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue' 
import MyFooter from './components/MyFooter.vue'
import { ref, onMounted } from 'vue'
import api from './services/api'

const message = ref('')

onMounted(async () => {
  try {
    const response = await api.get('test/')
    message.value = response.data.message
  } catch (error) {
    console.error('API Connection Error:', error)
  }
})
</script>

<template>
  <div id="app">
    <NavBar />
    <div v-if="message" class="api-status">
      Backend Connection: {{ message }}
    </div>

    
    <main class="main-content">
      <RouterView />
    </main>
    <MyFooter />
  </div>
  
</template>

<style>

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  color: #2c3e50;
  min-height: 100vh;
  background-color: #fafafa;
  display:flex;
  flex-direction:column;
}

.api-status {
  background-color: #e8f5e9;
  color: #2e7d32;
  text-align: center;
  padding: 8px;
  font-size: 0.85rem;
  font-weight: 500;
}

.main-content {
  flex:1;
  padding: 40px 8%;
}
</style>