<template>
  <nav class="navbar">
    <div class="logo">
      <span class="logo-text">AMO parlour</span>
    </div>

    <div class="nav-links">
      <router-link to="/" class="nav-item">Home</router-link>
      <router-link to="/login" class="nav-item">Login</router-link>
      <router-link to="/signup" class="nav-item">Signup</router-link>
      
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color:rgba(255,255,255,0.9);
  padding: 20px 40px;
  width: 100%;
}

.logo-text {
  font-weight: 700;
  font-size: 1.6rem;
  color: #4B2E4F;
}

.nav-links {
  display: flex;
  gap: 25px;
  color:#4B2E4F;
}

.nav-item {
  text-decoration: none;
  color: #4B2E4F;
  font-weight: 500;
}

.nav-item:hover {
  color: #B76E79;
}

.router-link-active {
  font-weight: 700;
}
</style>