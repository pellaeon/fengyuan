<template>
  <section id="mainContent">
    <div class="translucent" :style="{ backgroundImage: albumCover ? 'url(' + albumCover + ')' : 'none' }"></div>
    <filelist></filelist>
  </section>
</template>

<script>
// import { event } from '../../../utils'; //TODO

import filelist from './filelist.vue';

export default {
  components: { filelist },

  data() {
    return {
      albumCover: null,
    };
  },
};
</script>

<style lang="scss">
@import "../../../../static/scss/partials/_vars.scss";
@import "../../../../static/scss/partials/_mixins.scss";

#mainContent {
  flex: 1;
  position: relative;
  overflow: hidden;

  > section {
    position: absolute;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    backface-visibility: hidden;

    .main-scroll-wrap {
      padding: 24px 24px 48px;
      overflow: auto;
      flex: 1;
      -ms-overflow-style: -ms-autohiding-scrollbar;

      html.touchevents & {
        // Enable scroll with momentum on touch devices
        overflow-y: scroll;
        -webkit-overflow-scrolling: touch;
      }
    }
  }

  h1.heading {
    font-weight: $fontWeight_UltraThin;
    font-size: 2.76rem;
    padding: 1rem 1.8rem;
    border-bottom: 1px solid $color2ndBgr;
    min-height: 96px;
    position: relative;
    align-items: center;
    align-content: stretch;
    display: flex;
    line-height: normal;

    span:first-child {
      flex: 1;
    }

    .meta {
      display: block;
      font-size: $fontSize;
      color: $color2ndText;
      margin: 12px 0 0 2px;

      a {
        color: #fff;

        &:hover {
          color: $colorHighlight;
        }
      }
    }

    .buttons {
      text-align: right;
      z-index: 2;

      @include button-group();
    }
  }

  .translucent {
    position: absolute;
    top: -20px;
    left: -20px;
    right: -20px;
    bottom: -20px;
    filter: blur(20px);
    opacity: .07;
    z-index: 0;
    overflow: hidden;
    background-size: cover;
    background-position: center;
    transform: translateZ(0);
    backface-visibility: hidden;
    perspective: 1000;
    pointer-events: none;
  }

  @media only screen and (max-width: 768px) {
    h1.heading {
      font-size: 1.38rem;
      min-height: 0;
      line-height: 1.85rem;
      text-align: center;
      flex-direction: column;

      .toggler {
        font-size: 1rem;
        margin-left: 4px;
        color: $colorHighlight;
      }

      .meta {
        display: none;
      }

      .buttons {
        justify-content: center;
        margin-top: 8px;
      }

      span:first-child {
        flex: 0 0 28px;
      }
    }

    > section {
      .main-scroll-wrap {
        padding: 12px;
      }
    }
  }

  @media only screen and (max-width: 375px) {
    > section {
      // Leave some space for the "Back to top" button
      .main-scroll-wrap {
        padding-bottom: 64px;
      }
    }
  }
}
</style>
