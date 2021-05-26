<template>
  <div>
    <header class="navbar">
      <strong>link shortener</strong>
      <button class="btn danger" id="btn-1" hidden="true" @click="showShortLink">Создать короткую ссылку</button>
      <button class="btn danger" id="btn-2" @click="showCustomShortLink">Создать кастомную ссылку</button>
    </header>
    <div class="container with-nav" id="app">
      <form class="card" @submit.prevent="createShortLink" id="2">
        <div class="form-control">
          <input placeholder="Введите URL-адресс"
                 type="text" id="UrlForShortLink"
                 v-model="inputHandler.UrlForShortLink"
                 v-on:keypress.enter="createShortLink"
          />
        </div>
        <button
            :disabled="this.inputHandler.UrlForShortLink.length === 0"
            class="btn primary">Создать
        </button>
        <h1 v-if="shortLink.error">
          <hr>
          {{ shortLink.error }}
        </h1>
        <h1 v-if="shortLink.short_link">
          <hr>
          <a v-bind:href="shortLink.url" v-text="'http://127.0.0.1:8080/' + shortLink.short_link"/>
        </h1>
      </form>
      <form class="card" id="1" @submit.prevent="createCustomShortLink" hidden="true">
        <div class="form-control">
          <input placeholder="Введите URL-адресс"
                 type="text" id="UrlForCustomShortLink"
                 v-model="inputHandler.UrlForCustomShortLink"
                 v-on:keypress.enter="createCustomShortLink"
          />
        </div>
        <div class="form-control">
          <input placeholder="Введите кастомную ссылку"
                 type="text" id="customShortLink"
                 v-model="inputHandler.customShortLink"
                 v-on:keypress.enter="createCustomShortLink"

          />
        </div>
        <button
            :disabled="
                       this.inputHandler.customShortLink.length === 0 ||
                       this.inputHandler.UrlForCustomShortLink.length === 0
                      "
            class="btn primary">Создать
        </button>
        <h1 v-if="customShortLink.error">
          <hr>
          {{ customShortLink.error }}
        </h1>
        <h1 v-if="customShortLink.custom_short_link">
          <hr>
          <a v-bind:href="customShortLink.url" v-text="'http://127.0.0.1:8080/' + customShortLink.custom_short_link"/>
        </h1>
      </form>
    </div>
  </div>
</template>
<script>


export default {
  name: 'Home',
  data: () => ({
    shortLink: {},
    customShortLink: {},
    inputHandler: {
      UrlForShortLink: '',
      UrlForCustomShortLink: '',
      customShortLink: ''
    }
  }),
  methods: {
    showShortLink() {
      document.getElementById('1').hidden = true
      document.getElementById('2').hidden = false
      document.getElementById('btn-1').hidden = true
      document.getElementById('btn-2').hidden = false
      this.shortLink = {}
    },
    showCustomShortLink() {
      document.getElementById('2').hidden = true
      document.getElementById('1').hidden = false
      document.getElementById('btn-1').hidden = false
      document.getElementById('btn-2').hidden = true
      this.customShortLink = {}
    },
    inputChangeHandler(event) {
      this.inputHandler[event.target.id] = event.target.value
    },
    createShortLink() {
      this.axios.post(
          'http://127.0.0.1:8000/api/create-short-link/',
          {'url': this.inputHandler.UrlForShortLink}
      ).then((response) => {
        this.shortLink = response.data
        this.inputHandler.UrlForShortLink = ''
      })
    },
    createCustomShortLink() {
      this.axios.post(
          'http://127.0.0.1:8000/api/create-custom-short-link/',
          {
            'url': this.inputHandler.UrlForCustomShortLink,
            'custom_short_link': this.inputHandler.customShortLink
          }
      ).then((response) => {
        this.customShortLink = response.data
        this.inputHandler.UrlForCustomShortLink = ''
        this.inputHandler.customShortLink = ''
      })
    }
  }
}
</script>
