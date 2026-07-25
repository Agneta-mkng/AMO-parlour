<template>
  <section class="hero">
  <h1>AMO parlour</h1>
   <p class="description">
    Experience luxurious beauty treatments tailored to bring out your natural elegance.
   </p>
   <button class="explore-btn" @click="scrollToServices">
     Explore our services
   </button>
  </section>
  <section v-if="showServices" id="services" class="servicesProvided">
    <h2>Our services</h2>
    <div class="services">
      <div
        class="service-card"
        v-for="service in services"
        :key="service.id"
      >
        <h3>{{ service.service_name }}</h3>
        <p>{{ service.service_des }}</p>
        <h4>From Ksh {{ service.service_price }}</h4>
        <button class="service-btn" @click="goToBooking(service.service_name)">
         Book this service
        </button>
      </div>
    </div>
    
  </section>
</template>

<script setup lang="ts">
import { ref,onMounted,nextTick } from "vue";
import { useRouter } from "vue-router";
import api from "@/services/api";

interface Service{
 id:number;
 service_name: string;
 service_des: string;
 service_price: number | string;
}

const services = ref<Service[]>([]);
const showServices=ref(true)
const router= useRouter();

const loadServices = async () => {
    try {
      const response = await api.get("services/");
      services.value = response.data;
    } catch (error) {
      console.error("Failed to load services:", error);
  }
};
onMounted(() =>{
loadServices();
});
async function scrollToServices(){
 showServices.value=true;
 await nextTick();
 const section=document.getElementById("services");
 section?.scrollIntoView({ behavior:"smooth"});
}
function goToBooking(serviceName: string){
router.push({
path:"appointment/",
query: {service:serviceName }
});
}
</script>

<style scoped>
.hero{
text-align :center;
padding:60px 20px;
}
.hero h1{
font-size: 2.5rem;
  color: #4b2e4f;
  margin-bottom: 15px;
}

.description {
  font-size: 1.1rem;
  color: #666;
  max-width: 600px;
  margin: 0 auto 25px;
}

.explore-btn {
  padding: 12px 28px;
  background-color: #4b2e4f;
  color: white;
  border: none;
  border-radius: 25px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s;
}

.explore-btn:hover {
  background-color: #362139;
}
.servicesProvided {
  padding: 30px;
  text-align: center;
}

.services {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
  margin-top: 30px;
}

.service-card {
  background: rgba(255, 255, 255, 0.85);
  border-radius: 18px;
  padding: 25px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.service-card h3 {
  color: #4b2e4f;
  margin-bottom: 10px;
}

.service-card p {
  color: #555;
  margin-bottom: 15px;
}

.service-card h4 {
  color: #b76e79;
}
.service-card:hover{
color:#b76e79;
}
.service-btn{
margin-top:18px;
width:100%;
padding:12px;
border:none;
border-radius:30px;
cursor:pointer;
background:linear-gradient(135deg,#B76E79,#D48A9A);
color:white;
font-weight:600;
transition:3s;
}
.service-btn:hover{
transform:translateY(-2px);
box-shadow:0 8px 20px rgba(183,110,121,.3);
}
</style>