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
 message.value=error.response?.data?.message || "Login failed!";
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
v-model="client_password" type="text" placeholder="Your password"
/>

<button type="submit">Login</button>
</form>

<p>{{message}}</p>

</div>
</template>