<template>
  <nav class="side side-nav" id="sidebar">
    <section>
      <h1>Mounts</h1>

      <ul class="menu">
        <li>
          <a class="home">Local</a>
        </li>
      </ul>
    </section>

  </nav>
</template>

<script>
// TODO add back ismobilejs
</script>

<style lang="scss">
@import "../../../../static/scss/partials/_vars.scss";
@import "../../../../static/scss/partials/_mixins.scss";

#sidebar {
  flex: 0 0 256px;
  background-color: $colorSidebarBgr;
  padding: 22px 0 0;
  max-height: calc(100vh - #{$headerHeight + $footerHeight});
  overflow: auto;
  overflow-x: hidden;
  -ms-overflow-style: -ms-autohiding-scrollbar;

  html.touchevents & {
    // Enable scroll with momentum on touch devices
    overflow-y: scroll;
    -webkit-overflow-scrolling: touch;
  }

  a.droppable {
    transform: scale(1.2);
    transition: .3s;
    transform-origin: center left;

    color: $colorMainText;
    background-color: rgba(0, 0, 0, .3);
  }

  section {
    margin-bottom: 32px;

    h1 {
      text-transform: uppercase;
      letter-spacing: 1px;
      padding: 0 16px;
      margin-bottom: 12px;

      i {
        float: right;
      }
    }

    a {
      display: block;
      height: 36px;
      line-height: 36px;
      padding: 0 12px 0 16px;
      border-left: 4px solid transparent;

      &.active, &:hover {
        border-left-color: $colorHighlight;
        color: $colorLinkHovered;
        background: rgba(255, 255, 255, .05);
      }

      &:hover {
        border-left-color: darken($colorHighlight, 20%);
      }

      &::before {
        width: 24px;
        display: inline-block;
        font-family: FontAwesome;
      }

      &.home::before {
        content: "\f015";
      }
    }
  }

  .new-ver {
    margin: 16px;
    padding: 16px;
    border: 1px solid $color2ndText;
    color: $colorMainText;
    opacity: .3;
    font-size: .9rem;
    display: block;
    transition: .3s;

    &:hover {
      opacity: .7;
    }
  }


  @media only screen and (max-width : 667px) {
    position: fixed;
    height: calc(100vh - #{$headerHeight + $footerHeight});
    padding-bottom: $footerHeight; // make sure the footer can never overlap the content
    width: 100%;
    z-index: 99;
    top: $headerHeight;
    left: -100%;
    transition: left .3s ease-in;

    &.showing {
      left: 0;
    }
  }
}
</style>

