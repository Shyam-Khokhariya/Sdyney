<template>
  <div class="container">
    <!-- Movie Poster -->
    <div class="movie-poster-container">
      <img :src="movie.Poster" alt="Movie Poster" class="movie-poster" />
      <div class="movie-poster-info">
        <div class="moveie-poster-info-watch">
          <div>image</div>
          <div class="movie-poster-info-text">
            <span>Now Streaming</span>
            <span class="watch-now"> Watch Now</span>
          </div>
        </div>

        <!-- Icons only shown on mobile screens -->
        <div class="mobile-icons">
          <div class="user-score-icon-mobile">ico</div>
          <div class="user-score-icon-mobile">ico</div>
          <div class="user-score-icon-mobile">ico</div>
          <div class="user-score-icon-mobile">ico</div>
        </div>
      </div>
    </div>

    <!-- Movie Details -->
    <div class="movie-details">
      <div class="movie-title">
        {{ movie.Title }} <span>({{ movie.Year }})</span>
      </div>
      <div class="movie-runtime">
        <span>12</span> {{ movie.Released }} • {{ movie.Genre }} •
        {{ movie.Runtime }}
      </div>
      <div class="user-score">
        <div class="user-score-circle">
          <span class="circle-border"></span>
          <span class="rating-circle">{{ movie.imdbRating }}</span>

          <div class="user-score-text">User Score</div>
        </div>
        <div class="user-score-icon">ico</div>
        <div class="user-score-icon">ico</div>
        <div class="user-score-icon">ico</div>
        <div class="user-score-icon">ico</div>
        <div class="user-score-play">▶ Play Trailer</div>
      </div>

      <div class="movie-overview">
        <label>Obviously</label>
        <h3>Overview</h3>
        <p>{{ movie.Plot }}</p>
      </div>

      <!-- Director and Writer -->
      <div class="meta-info">
        <div v-for="(item, index) in metaInfo" :key="index">
          <strong>{{ item.value }}</strong>
          <p>{{ item.label }}</p>
        </div>
      </div>

      <!-- IMDb Link -->
      <a
        :href="`https://www.imdb.com/title/${movie.imdbID}/`"
        target="_blank"
        class="button"
        >View on IMDb</a
      >
    </div>
  </div>
</template>

<script>
export default {
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      metaInfo: [
        { label: "Director", value: this.movie.Director },
        { label: "Writer", value: this.movie.Writer },
        { label: "Actors", value: this.movie.Actors },
        { label: "Characqter", value: "Stan Lee" },
        { label: "Characqter", value: "Stan Lee" },
        { label: "Characqter", value: "Stan Lee" },
        { label: "Characqter", value: "Stan Lee" },
        { label: "Characqter", value: "Stan Lee" },
        { label: "Characqter", value: "Stan Lee" },
        { label: "Characqter", value: "Stan Lee" },
        { label: "Characqter", value: "Stan Lee" },
      ],
    };
  },
};
</script>

<style scoped>
.container {
  display: flex;
  padding: 40px;
  margin: 0 auto;
}

.movie-poster {
  max-width: 100%;
  height: 600px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
}
.movie-poster-info {
  background-color: #333b52;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffffa8;
  font-weight: bold;
  font-size: 17px;
  padding: 0 20px;
}

.movie-poster-info-text {
  display: flex;
  flex-direction: column;
  text-align: start;
  margin: 0 0 0 20px;
}

.movie-poster-info-text span {
  margin-right: 20px;
}

.watch-now {
  color: #ffffff;
}

.movie-details {
  text-align: start;
  padding: 0 60px;
}

.movie-title {
  font-size: 2.5rem;
  font-weight: bold;
}
.movie-title span {
  color: #abb1ba;
  font-weight: normal;
}

.user-score {
  margin: 10px 0;
  display: flex;
  align-items: center;
  gap: 10px;
}

.user-score-circle {
  display: flex;
}
.moveie-poster-info-watch {
  display: flex;
  justify-content: center;
  align-items: center;
}

.user-score-text {
  width: 70px;
  font-size: 1.2rem;
  font-weight: bold;
}
.user-score-icon {
  padding: 15px;
  border-radius: 50%;
  background-color: #404240;
  margin: 0 10px;
}
.user-score-icon-mobile {
  display: none;
}

.user-score-play {
  padding: 5px 10px;
  cursor: pointer;
  font-size: 1.2rem;
  font-weight: 500;
}
.circle-border {
  border-radius: 50%;
  border-top: 5px solid #08e54b;
  border-right: 5px solid #08e54b;
  border-bottom: 5px solid #08e54b;
  border-left: 5px solid #bff1ce;
  box-shadow: 0 0 0 4px #3f3f3f;
  transform: rotate(45deg);
  position: relative;
  color: white;
  background-color: #3f3f3f;
  width: 50px;
  height: 50px;
  display: flex;
  margin: 0 10px;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.2rem;
}

.rating-circle {
  position: absolute;
  color: white;
  width: 50px;
  height: 50px;
  display: flex;
  margin: 5px 15px;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.2rem;
  z-index: 1;
}

.movie-runtime {
  font-size: 1.1rem;
  margin: 5px 0 25px 0;
}

.movie-runtime span {
  border-radius: 5px;
  padding: 2px 7px 2px 4px;
  border: 1px solid #abb1ba;
  color: #abb1ba;
}

.movie-overview {
  margin: 20px 0;
  text-align: left;
}

.movie-overview h3 {
  font-size: 1.5rem;
  margin: 10px 0;
}
.movie-overview label {
  font-size: 1.2rem;
  font-style: italic;
  color: #abb1ba;
}

.meta-info {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin: 20px 0;
}

.meta-info div {
  text-align: left;
}

.meta-info div p {
  margin: 5px 0;
}

a.button {
  background-color: #3b82f6;
  color: white;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
  margin-top: 20px;
  display: inline-block;
  font-weight: bold;
}

a.button:hover {
  background-color: #2563eb;
}

@media (max-width: 768px) {
  .container {
    flex-direction: column;
    padding: 0 20px;
    margin:0 0 160px 0;
  }
  .movie-details {
    padding: 0 0;
  }
  .user-score-icon {
    display: none;
  }
  .user-score-icon-mobile {
    padding: 15px;
    border-radius: 50%;
    background-color: #404240;
    margin: 0 10px;
    display: block;
  }
  .user-score {
    display: flex;
    justify-content: space-between;
  }
  .movie-title {
    font-size: 1.3rem;
    font-weight: bold;
    margin: 10px 0;
  }

  .movie-runtime {
    font-size: 1.1rem;
    margin: 20px 0;
    padding: 0 40px;
    text-align: center;
  }
  .meta-info {
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
  .movie-poster-info {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    z-index: 1000;
    padding: 10px 0;
    height: 120px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-shadow: 0px -2px 10px rgba(0, 0, 0, 0.3);
  }

  .movie-poster-info-text {
    display: flex;
    flex-direction: column; 
    justify-content: center;
  }

  .mobile-icons {
    display: flex;
    gap: 10px;
    margin-top: 10px;
  }
.movie-poster {
  width: 100%;
  height: 500px;
}
}
@media (max-width: 1025px) {
.movie-details {
  text-align: start;
  padding: 0 30px;
}
.movie-poster-container {
 width: 100%; 
}
}
</style>
