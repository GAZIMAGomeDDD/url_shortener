<script>
export default {
  name: 'Redirect',
  props: ['link',],
  methods:
      {
        postMethod() {
          this.axios.get(
              `http://127.0.0.1:8000/api/${this.link}`
          ).then((response) => {
            window.location.replace(response.data.url)
          }).catch(error => this.$router.push('/'))
        }
      },
  beforeMount() {
    this.postMethod()
  }
}
</script>
