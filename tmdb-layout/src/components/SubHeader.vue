<template>
  <header class="header">
    <nav class="nav">
      <select id="overview-select" class="nav-select" disabled>
        <option value="overview-1">Overview</option>
        <option value="overview-2">Overview 2</option>
        <option value="overview-3">Overview 3</option>
      </select>

      <select id="media-select" class="nav-select" disabled>
        <option value="media-1">Media</option>
        <option value="media-2">Media 2</option>
        <option value="media-3">Media 3</option>
      </select>

      <select id="fandom-select" class="nav-select" disabled>
        <option value="fandom-1">Fandom</option>
        <option value="fandom-2">Fandom 2</option>
        <option value="fandom-3">Fandom 3</option>
      </select>

      <select id="share-select" class="nav-select" disabled>
        <option value="share-1">Share</option>
        <option value="share-2">Share 2</option>
        <option value="share-3">Share 3</option>
      </select>
    </nav>
  </header>
</template>

<style scoped>
.header {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 15px 30px;
  height: 40px;
  background-color: white;
  font-size: 14px;
}

.nav {
  display: flex;
  gap: 20px;
  align-items: center;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.nav-select {
  font-size: 18px;
  padding: 21px 10px;
  font-weight: 500;
  border: 1px solid #fff; 
  background-color: #fff;
  color: #000;
  position: relative; 
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.nav-select:hover {
  border-bottom: 4px solid #55e8d2;
}

.nav-select:focus {
  outline: none;
  border-color: #000; 
}

.nav-select option {
  font-size: 16px;
  padding: 10px;
}

.nav::-webkit-scrollbar {
  height: 8px;
}

.nav::-webkit-scrollbar-thumb {
  background-color: #888;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.nav::-webkit-scrollbar-thumb:hover {
  background-color: #555;
}

.nav::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

@media (max-width: 768px) {
  .header {
    padding: 10px;
  }

  .nav {
    gap: 15px;
  }

  .nav-select {
    font-size: 16px;
    padding: 18px 8px;
  }
}

@media (max-width: 480px) {
  .nav {
    gap: 10px;
  }

  .nav-select {
    font-size: 10px;
    padding: 18px 0;
  }
}
</style>
