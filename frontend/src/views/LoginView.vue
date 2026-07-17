<script setup lang="ts">
import { ref } from "vue";
import api from "@/services/api";

const client_email=ref("");
const client_password=ref("");
const message=ref("");

 async function userLogin(){
 try{
 const response=await api.post("login/",{
 client_email: client_email.value,
 client_password: client_password.value,
 });
 message.value=response.data.message;
 }

 catch(error){
 message.value=error.response?.data?.message || "Login failed!#b76e79;";
 }};
</script>

<template>
<div class="login">
<h2>Login</h2>
<form @submit.prevent="userLogin">

<input
v-model="client_email" type="email" placeholder="Email"
/>

<input
v-model="client_password" type="password" placeholder="Your password"
/>

<button type="submit">Login</button>
</form>

<p>{{message}}</p>

</div>
</template>

<style>
.login {
  text-align: center;
  font-size: 20px;
  display: flex;
  flex-direction: column;
  gap: 30px;
  width: 350px;
}

button{
background-color:#B76E79;
color:#FFFFFF;
padding: 20px 20px;
font-size:1.5rem;
}

button:hover{
background-color:9F5A65;
}

form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  color:4B2E4F;
}

input {
  padding: 12px;
  font-size: 1rem;
  color:4A4A4A;
  border:1px solid #D8C3D5;
  border-color:#B76E79;
  box-shadow:0 0 8px rgba(183,110,121,.25);
}
</style>