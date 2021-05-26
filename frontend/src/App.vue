<template>
  <router-view/>
</template>

<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

* {
  box-sizing: border-box;
}

body {
  font-family: Inter, Roboto, Oxygen, Fira Sans, Helvetica Neue, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 16px;
  color: #2c3e50;
}

hr {
  margin: 1rem 0;
}

.btn {
    color: #42b983;
    position: relative;
    place-content: center;
    place-items: center;
    width: fit-content;
    border-radius: 99px;
    letter-spacing: 0.05em;
    border: 1px solid #42b983;
    text-decoration: none;
    text-transform: uppercase;
    margin-right: 10px;
    padding: 0.5rem 1.5rem;
    white-space: nowrap;
    font-weight: 700;
    outline: none;
    background: #fff;
    transition: all 0.22s;
}

.form-control input,
.form-control select {
    margin: 0;
    outline: none;
    border: 2px solid #ccc;
    display: block;
    width: 100%;
    color: #2c3e50;
    padding: 0.5rem 1.5rem;
    border-radius: 3px;
    font-size: 1rem;
}

.form-control.invalid input {
    border-color: #e53935;
}

.btn:hover {
    cursor: pointer;
    opacity: 0.8;
}

.btn:disabled {
    cursor: not-allowed;
    opacity: 1!important;
    background: #eee!important;
    border-color: #ddd!important;
    color: #999!important;
}

.btn:active {
    box-shadow: inset 1px 1px 1px rgba(0, 0, 0, 0.3);
}

.btn.primary {
    background: #42b983;
    color: #fff;
}

.btn.danger {
    background: #e53935;
    color: #fff;
    border-color: #e53935;
}

.container {
    margin: 0 auto;
    max-width: 1000px;
}

.container.with-nav {
    margin-top: 70px;
}

.form-control {
    position: relative;
    margin-bottom: 0.5rem;
}

.card {
    overflow: hidden;
    padding: 1rem;
    margin-bottom: 1rem;
    border-radius: 10px;
    box-shadow: 2px 3px 10px rgba(0, 0, 0, 0.2);
    background: #fff;
}

.card.marked {
    border: 4px solid #42b983;
}

.navbar {
    display: flex;
    padding: 0 2rem;
    justify-content: space-between;
    align-items: center;
    position: fixed;
    z-index: 20;
    top: 0;
    left: 0;
    right: 0;
    height: 56px;
    background-color: #fff;
    box-sizing: border-box;
    border-bottom: 1px solid #eaecef;
}

</style>