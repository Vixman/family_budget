<template>
    <div>
      <div>
        <b-col>
          <b-table
            ref="budget"
            id="budget-table"
            hover
            :items="income"
            :fields="fields"
            :per-page="perPage"
            :current-page="currentPage"
            sticky-header="500px"
            class="main-scroller"
          >
          </b-table>
        </b-col>
        <span class="pt-1">
          <b-pagination
            v-model="currentPage"
            :total-rows="6"
            :per-page="perPage"
            aria-controls="budget-table"
            first-number
            last-number
            pills
          ></b-pagination>
        </span>
        <div class="d-flex w-100 justify-content-between mb-1">
          <span class="pt-2">
            <span>View:</span>
            <a :class="(size===perPage) ? 'px-1 page-size active' : 'px-1 page-size'"
              v-for="size in pageSizes"
              :key="size" @click="perPage = size">{{size}}</a>
          </span>
          <span class="pt-1">
          </span>
        </div>
      </div>
    </div>
  </template>

<script>
import axios from 'axios'
import {BPagination, BTable} from 'bootstrap-vue'

export default {
  data() {
    return {
      income: {
        "Income": 2222,

      },
      expenses: null,
      currentPage: 1,
      perPage: 10,
      pageSizes: [5, 10, 15],
      fields: [
        { key: 'Income', sortable: true },
        { key: 'Expenses', sortable: true },
        { key: 'Category', sortable: true },
        { key: 'User', sortable: true },
      ],
    }
  },
  mounted () {
    axios
    .get('https://127.0.0.1/8080/expenses/')
    .then(response => (this.expenses = response))
    console.log(this.expenses);
    axios
    .get('https://127.0.0.1/8080/Users/')
    .then(response => (this.Users = response))
  }
}
</script>