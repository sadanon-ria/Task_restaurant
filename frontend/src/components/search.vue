<template>
  <div class="flex items-center justify-center w-full mb-6">
    <div class="flex w-full max-w-2xl rounded-xl shadow-md bg-white px-4 py-2 ring-1 ring-gray-200">
      <input
        v-model="keyword"
        @keyup.enter="search"
        type="text"
        placeholder="ค้นหาสถานที่..."
        class="flex-1 bg-transparent focus:outline-none text-gray-800 placeholder-gray-400"
      />
      <button
        @click="search"
        class="ml-4 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition duration-200"
      >
        ค้นหา
      </button>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
export default {
  name: "searchBar",
  emits: ['onSearch'],
  setup(props, { emit }){
    const keyword = ref('')
    const search = () => {
      if (keyword.value.trim() !== '') {
        emit('onSearch', keyword.value.trim())
      }
    }

    return {
      keyword,
      search
    }
  }
}

</script>
