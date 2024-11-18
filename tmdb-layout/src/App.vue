<template>
  <div>
    <Header />
    <SubHeader />
    <MovieLayout v-if="movie" :movie="movie" />
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import MovieLayout from "./components/MovieLayout.vue";
import Header from "./components/Header.vue";
import SubHeader from "./components/SubHeader.vue";

export default {
  components: {
    Header,
    SubHeader,
    MovieLayout,
  },
  setup() {
    const movie = ref(null);

    const fetchMovieData = async () => {
      try {
        const response = await fetch(
          "http://www.omdbapi.com/?i=tt3896198&apikey=d2132124"
        );
        const data = await response.json();
        movie.value = data;
      } catch (error) {
        console.error("Failed to fetch movie data:", error);
      }
    };

    onMounted(() => {
      fetchMovieData();
    });

    return {
      movie,
    };
  },
};
</script>

<style>
/* Global styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #1e293b;
  color: #ffffff;
}
</style>
