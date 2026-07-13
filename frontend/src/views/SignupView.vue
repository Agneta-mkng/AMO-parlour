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