<template>
  <section id="fileListWrapper">
    <div class="none">
      <p>No files for now, upload some!</p>
    </div>
  </section>
</template>

<script>
// import isMobile from 'ismobilejs';

export default {
};
</script>

<style lang="scss">
@import "../../../../static/scss/partials/_vars.scss";
@import "../../../../static/scss/partials/_mixins.scss";

#queueWrapper {
  .none {
    color: $color2ndText;
    padding: 16px 24px;

    a {
      color: $colorHighlight;
    }
  }
}
</style>
