<template>
  <div id="app">
    <router-view name="navbar"/>
    <router-view/>
    <router-view name="footer"/>
  </div>
</template>

<style>
  .fade-enter {
    opacity: 0;
  }
  .fade-enter-active {
    transition: opacity .3s ease-in;
  }
  .fade-leave {

  }
  .fade-leave-active {
    opacity: 0;
    transition: opacity .3s ease-in;
  }
</style>
