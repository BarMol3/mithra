<template>
  <div id="public-page" class="fixed-top d-flex align-items-center justify-content-center mb-0">
    <b-card id="public-form" img-src="/static/logo-black.png" img-top img-height="150">
      <slot/>
    </b-card>
  </div>
</template>

<style>
#public-page {
  height: 100%;
  background-color: rgb(243, 245, 248);
  background-size: cover;
  background-repeat: no-repeat;
}
#public-form {
  background: white;
}
</style>