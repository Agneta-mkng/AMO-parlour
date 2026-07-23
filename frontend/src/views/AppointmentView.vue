<script setup lang="ts">
import { ref, watch } from "vue";
import api from "@/services/api";

const client_email = ref("");
const appointment_date = ref("");
const appointment_time = ref("");
const service_name = ref("");

const availableSlots = ref<string[]>([]); 
const message = ref("");
const isLoadingSlots = ref(false);

// The watch() helps us to monitor dates selected.Whenever the user selects or changes the date, fetch the available time slots for that specific day automatically.

watch(appointment_date, async (newDate) => {
  if (!newDate) {
    availableSlots.value = [];
    return;
  }

  isLoadingSlots.value = true;
  try {
    const response = await api.post("appointment-slot/", {
      appointment_date: newDate
    });
    availableSlots.value = response.data.available_slots || []; 
  } catch (error) {
    message.value = "Could not load available slots for this date.";
    console.error(error);
  } finally {
    isLoadingSlots.value = false;
  }
});

//Book the final appointment with all selected details
async function bookAppointment() {
  if (!client_email.value || !appointment_date.value || !appointment_time.value) {
    message.value = "Please fill in all fields.";
    return;
  }

  try {
    const response = await api.post("appointment/", {
      client_email: client_email.value,
      appointment_date: appointment_date.value,
      appointment_time: appointment_time.value,
      service_name: service_name.value,
    });
    message.value = response.data.message || "Appointment booked successfully!";
  } catch (error) {
    message.value = error?.response?.data?.message || "Something went wrong. Please try again.";
  }
}
</script>

<template>
  <div class="booking-container">
    <h2>Book an Appointment</h2>
    
    <form @submit.prevent="bookAppointment">
      <div class="displayAppointment">
        
        <div class="form-group">
          <label>Email Address</label>
          <input
            v-model="client_email"
            type="email"
            placeholder="Enter your email"
            required
          />
        </div>

        <div class="form-group">
          <label>Preferred Date</label>
          <input
            v-model="appointment_date"
            type="date"
            required
          />
        </div>


        <div class="form-group" v-if="appointment_date">
          <label>Available Time Slots</label>
          <p v-if="isLoadingSlots" class="loading-text">Loading times...</p>
          
          <select 
            v-else-if="availableSlots.length > 0" 
            v-model="appointment_time"
            required
          >
            <option value="" disabled selected>-- Select a convenient time --</option>
            <option v-for="slot in availableSlots" :key="slot" :value="slot">
              {{ slot }}
            </option>
          </select>

          <p v-else class="no-slots">No slots available for this date. Try another day!</p>
        </div>

        <button type="submit" class="submit-btn" :disabled="!appointment_time">
          Book Appointment
        </button>
      </div>
    </form>

    <p v-if="message" class="feedback-message">{{ message }}</p>
  </div>
</template>

<style scoped>
.booking-container {
  max-width: 500px;
  margin: 40px auto;
  padding: 35px;
  background: white;
  border-radius: 20px;
  backdrop-filter:blur(10px);
  border:1px solid rgba(200,162,200,.35);
  box-shadow: 0 15px 35px rgba(75, 46, 79, 18);
}

h2 {
  margin-bottom: 20px;
  color: #4B2E4F;
  font-size: 2rem;
  margin-bottom:25px;
  font-family:"Playfair Display",serrif;
  text-align: center;
}

.form-group {
  margin-bottom: 18px;
  display: flex;
  flex-direction: column;
}

label {
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 8px;
  color: #4B2E4F;
}

input, select {
  padding: 12px 15px;
  border: 1px solid #D8C3D5;
  border-radius: 12px;
  background:#FFF8FC;
  color:#4A4A4A;
  font-size: 1rem;
  transition: .3s;
}

input:focus, select:focus {
  border-color: #B76E79;
  outline:none;
  box-shadow:0 0 10px rgba(183,110,121,.25);

}

.loading-text, .no-slots {
  font-size: 0.9rem;
  color: #8B5E83;
  font-style: italic;
  margin-top:8px;
}

.submit-btn {
  width: 100%;
  padding: 14px;
  background-color: #B76E79;
  color: #FFFFFF;
  border: none;
  background:linear-gradient(135deg,#B76E79,#D48A9A);
  border-radius: 30px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: .3s;
}

.submit-btn:hover:not(:disabled) {
  background:linear-gradient(135deg,#9F5A65,#B76E79);
  transform:translateY(-2px);
  box-shadow:0 10px 20px rgba(183,110,121,.35);
}

.submit-btn:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.feedback-message {
  margin-top: 20px;
  text-align: center;
  font-weight: 600;
  color: #B76E79;
}
</style>