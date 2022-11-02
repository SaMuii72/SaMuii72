<template>
  <div class="app">
  <nav>
    <ul>
    <li><router-link to="/" class="active">Home</router-link></li>
    </ul>
  </nav>
  <router-view/>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap');
* {
  font-family:  'Rubik', sans-serif;
  margin: 0;
}

ul {
  text-align: left;
  text-decoration: none;
  font-size: 17px;
}

li{
  display: inline-block;
}

a{
  display: block;
  color: white;
  text-align: center;
  padding: 10px 10px;
  text-decoration: none;
  font-size: 17px;
}

nav{
  background: black;
  padding: 14px 0px;
  overflow: hidden;
}
</style>



