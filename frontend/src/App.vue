<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <searchBar @onSearch="fetchData" />
  <div class="max-w-6xl mx-auto px-4">
    <h1 class="text-2xl font-bold mb-4">
      ผลลัพธ์สำหรับ: "{{ dataresults.keyword }}"
    </h1>
    <RestaurantCard :places="dataresults.results" :photos="allPhoto"/>
  </div>

  
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import RestaurantCard from './components/card.vue'
import searchBar from './components/search.vue'
import { ref, onMounted } from 'vue'

export default {
  name: 'App',
  components: {
    // HelloWorld
    RestaurantCard,
    searchBar
  },
  setup(){
    const defaultkeyword = ref('บางซื่อ')
    const dataresults = ref({
      id: '',
      keyword: '',
      results: [{
        "fsq_place_id": "",
        "name": "",
        "formatted_address": "",
        "tel": ""
      }]
    })
    const onePhoto = ref('')
    const allPhoto = ref([])

    const fetchData = async (keyword) => {
      defaultkeyword.value = keyword
      const res = await fetch(`http://127.0.0.1:8000/dataKey/${keyword}`)
      dataresults.value = await res.json()

      allPhoto.value = []
      for (const place of dataresults.value.results) {
        await fetchDataPhoto(place.fsq_place_id)
      }
      console.log(allPhoto.value)
    }

    const fetchDataPhoto = async (fsq_place_id) => {
      const res = await fetch(`http://127.0.0.1:8000/dataPhoto/${fsq_place_id}`)
      const photoData = await res.json()
      onePhoto.value = photoData
      allPhoto.value.push(photoData)
    }

    onMounted(() => {
      fetchData(defaultkeyword.value)
    })
    console.log(dataresults)
    return {
      dataresults,
      allPhoto,
      fetchData
    }
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
