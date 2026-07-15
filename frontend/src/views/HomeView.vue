<template>
  <section class="servicesProvided">

    <div class="services">
      <div
        class="service-card"
        v-for="service in services"
        :key="service.id"
      >
        <h3>{{ service.service_name }}</h3>
        <p>{{ service.service_des }}</p>
        <h4>Ksh {{ service.service_price }}</h4>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref,onMounted } from "vue";
import axios from "axios";

const services = ref([]);

const loadServices = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/services/");
      services.value = response.data;
    } catch (error) {
      console.error("Failed to load services:", error);
  }
};
onMounted(() =>{
loadServices();
});
</script>

<style scoped>
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
</style>