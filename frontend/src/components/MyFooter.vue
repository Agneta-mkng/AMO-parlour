<template>
  <footer class="footer">
    <div class="container">
      <p>&copy; {{ currentYear }} AMO parlour.</p>
    </div>
  </footer>
</template>

<script setup lang="ts">
const currentYear = new Date().getFullYear()
</script>

<style scoped>
.footer {
  background: rgba(255,255,255,0.9);
  color: #B76E79;
  padding: 20px;
  margin-top: 40px;
}

.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}
</style>