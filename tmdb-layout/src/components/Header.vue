<template>
  <header class="header">
    <nav class="nav">
      <div class="logo">TMDB</div>
      <div class="nav-divider"></div>
      <a href="#" class="nav-link">Movies</a>
      <a href="#" class="nav-link">TV Shows</a>
      <a href="#" class="nav-link">People</a>
      <a href="#" class="nav-link">More</a>
    </nav>
    <div class="header-actions">
      <button class="plus-btn">+</button>
      <button class="language-btn">EN</button>
      <button class="login-btn">Login</button>
      <button class="join-btn">Join TMDB</button>
      <button class="join-btn">Search</button>
    </div>
  </header>

  <!-- Responsive header (mobile) -->
  <header class="header-responsive">
    <div class="menu-icon" @click="toggleMenu">☰</div>

    <div v-if="isMenuVisible" class="nav-dropdown">
      <a href="#" class="nav-link">Movies</a>
      <a href="#" class="nav-link">TV Shows</a>
      <a href="#" class="nav-link">People</a>
      <a href="#" class="nav-link">More</a>
    </div>

    <nav class="nav">
      <div class="logo">TMDB</div>
    </nav>

    <div class="header-actions">
      <button class="join-btn">User</button>
      <button class="join-btn">Search</button>
    </div>
  </header>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      isMenuVisible: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuVisible = !this.isMenuVisible;
    },
  },
};
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 30px;
  background-color: #0d253f;
  color: white;
  font-size: 14px;
}

.header-responsive {
  display: none;
  justify-content: space-between;
  align-items: center;
  padding: 15px 30px;
  background-color: #0d253f;
  color: white;
  font-size: 14px;
}

.logo {
  font-size: 24px;
  font-weight: bold;
  color: #01d277;
}

.nav-divider {
  width: 70px;
  display: flex;
  margin: 6px 0 0;
  height: 25px;
  background-color: #799da8;
  border-radius: 20px;
}

.nav {
  display: flex;
  gap: 20px;
}

.nav-link {
  text-decoration: none;
  color: white;
  font-weight: 600;
  font-size: 17px;
  display: flex;
  align-items: center;
}

.nav-link:hover {
  color: #01d277;
}

.header-actions {
  display: flex;
  gap: 15px;
}

.plus-btn,
.login-btn,
.join-btn {
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
}

.language-btn {
  border: 1px solid #abb1ba;
  border-radius: 5px;
  padding: 2px 5px;
  font-size: 14px;
  font-weight: 600;
}

.join-btn {
  padding: 5px 10px;
  border-radius: 5px;
}

.join-btn:hover {
  background-color: #03e892;
}

@media (max-width: 768px) {
  .header {
    display: none;
  }

  .header-responsive {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    justify-content: space-between;
    align-items: center;
    padding: 15px 30px;
    background-color: #0d253f;
    color: white;
    font-size: 14px;
  }

  .join-btn {
    padding: 5px 0;
    border-radius: 5px;
  }

  .menu-icon {
    font-size: 24px;
    cursor: pointer;
  }

  .nav-dropdown {
    display: flex;
    flex-direction: column;
    gap: 10px;
    position: absolute;
    z-index: 99;
    top: 60px;
    left: 0;
    right: 0;
    background-color: #0d253f;
    padding: 10px 20px;
  }

  .nav-dropdown a {
    text-decoration: none;
    color: white;
    font-weight: 600;
    font-size: 17px;
  }

  .nav-dropdown a:hover {
    color: #01d277;
  }
  .nav {
    justify-content: center;
  }
  .menu-icon {
    display: flex;
  }
  .header-actions {
    display: flex;
    gap: 15px;
    justify-content: flex-end;
  }
}
</style>
