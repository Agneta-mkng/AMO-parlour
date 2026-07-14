<script setup lang="ts">
import api from "@/services/api"
import {ref} from "vue"

const client_contact=ref("");
const client_email=ref("");
const client_name=ref("");
const client_password=ref("");
const message=ref("");

async function signUp(){
try{
const response=await api.post("signup/",{
client_email:client_email.value,
client_name:client_name.value,
client_contact:client_contact.value,
client_password:client_password.value,
});
message.value=response.data.message
}
catch(error){
message.value=error.response?.data?.message
}
}
</script>
<template>
<div class="signup">
<form @submit.prevent="signUp">
<input
v-model="client_email" type="email" placeholder="Email"
/>

<input
v-model="client_name" type="text" placeholder="Name"
/>

<input
v-model.number="client_contact" type="number" placeholder="Phone number"
/>

<input
v-model="client_password" type="password" placeholder="Password"
/>
<button type="submit">Sign up</button>
</form>
<p>{{message}}</p>
</div>
</template>

<style>
.signup {
  text-align: center;
  font-size: 20px;
  display: flex;
  flex-direction: column;
  gap: 30px;
  width: 350px;
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

button{
background-color:#B76E79;
color:#FFFFFF;
padding: 20px 20px;
font-size:1.5rem;
}

button:hover{
background-color:9F5A65;
}
</style>