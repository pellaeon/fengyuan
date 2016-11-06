<template>
  <div id="mainWrapper">
    <sidebar></sidebar>
    <main-content></main-content>
    <!--
  <extra></extra>-->
  </div>
</template>

<script>
import sidebar from './sidebar/index.vue';
import mainContent from './main-content/index.vue';
// import extra from './extra/index.vue';

export default {
  components: { sidebar, mainContent }
};
</script>

<style lang="scss">
@import "../../../static/css/meyer-reset.min.css";

#mainWrapper {
  display: flex;
  flex: 1;
}
</style>
