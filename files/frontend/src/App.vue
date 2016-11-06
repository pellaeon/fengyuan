<template>
  <div id="app">
    <main-wrapper></main-wrapper>
  </div>
</template>

<script>
import mainWrapper from './components/main-wrapper';

export default {
  components: {
    mainWrapper
  },
};
</script>

<style lang="scss">
@import "static/scss/partials/_vars.scss";
@import "static/scss/partials/_mixins.scss";
@import "static/scss/partials/_shared.scss";

#main {
  display: flex;
  min-height: 100vh;
  flex-direction: column;

  background: $colorMainBgr;
  color: $colorMainText;

  font-family: $fontFamily;
  font-size: 1rem;
  line-height: 1.5rem;
  font-weight: $fontWeight_Thin;

  padding-bottom: $footerHeight;
}
</style>
