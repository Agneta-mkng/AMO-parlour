
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
  max-width: 450px;
  margin: 0 auto;
  padding: 30px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

h2 {
  margin-bottom: 20px;
  color: #2c3e50;
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
  margin-bottom: 6px;
  color: #555;
}

input, select {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.2s;
}

input:focus, select:focus {
  border-color: #b5838d;
}

.loading-text, .no-slots {
  font-size: 0.9rem;
  color: #888;
  font-style: italic;
}

.submit-btn {
  width: 100%;
  padding: 12px;
  background-color: #B76E79;
  color: #FFFFFF;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s;
}

.submit-btn:hover:not(:disabled) {
  background-color: 9F5A65;
}

.submit-btn:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.feedback-message {
  margin-top: 15px;
  text-align: center;
  font-weight: 500;
  color: #b5838d;
}
</style>