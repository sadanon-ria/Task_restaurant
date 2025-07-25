<template>
<div class="max-w-6xl mx-auto px-4">
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
        <div v-for="i,idx in places" :key="i">
            <div class="w-full sm:max-w-sm bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700">
                <div v-if="photos[idx]">
                    <img
                        :src="photos[idx].prefix + 'original' + photos[idx].suffix"
                        alt="restaurant photo"
                        class="rounded-lg w-full object-cover"
                    />
                </div>
                <div v-else class="w-full h-48 flex items-center justify-center bg-gray-200 text-gray-500 rounded-lg">
                    ไม่มีรูปภาพ
                </div>
                <div class="p-5">
                    <a href="#">
                        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
                            {{ i.name }} 
                        </h5>
                    </a>
                    <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
                        address:
                        {{ i.formatted_address }}
                    </p>
                    <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
                        tell :
                        {{ i.tel }}
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>

</template>

<script>
export default {
  name: "RestaurantCard",
  props: {
    places: {
      type: Array,
      required: true
    },
    photos: {
        type: Array,
        required: true
    }
  }
}
</script>
