import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import naive from 'naive-ui'
import axios from "axios";

const app = createApp(App)

// axios.defaults.baseURL = "http://localhost:5000"
// axios.defaults.url = "http://127.0.0.1:5000"

app.use(createPinia())
app.use(router)
app.use(naive)

if (import.meta.env.MODE === "development") {
    app.config.globalProperties.$axios = axios.create({
        // url: import.meta.env.VITE_API,
        // baseURL: "http://127.0.0.1:5000",
        timeout: 3000
    })
} else {
    app.config.globalProperties.$axios = axios.create({
        baseURL: import.meta.env.VITE_API,
        timeout: 3000
    })
}

// app.config.globalProperties.$axios = axios

app.mount('#app')
