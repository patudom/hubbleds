<template>
  <v-card color="info"
          :class="highlighted ? 'pa-1' : ''">
    <v-data-table
        :headers="headers"
        :items="items"
        :items-per-page="5"
        class="elevation-1"
        hide-default-header
        hide-default-footer
        single-select
        show-select
        @item-selected="on_row_selected"
    >
      <template
          v-slot:top
      >
        <v-toolbar
            color="primary"
            dense
            dark
            rounded
        >
          <v-toolbar-title
              class="text-h6 text-uppercase font-weight-regular"
          >
             {{ title }}
          </v-toolbar-title>
        </v-toolbar>
      </template>

      <template
          v-slot:header="{ props: { headers } }"
      >
        <thead>
        <tr>
          <th v-for="header in headers">
            <span v-html="header.text"></span>
          </th>
        </tr>
        </thead>
      </template>

      <template v-slot:item.rest_wave="{ item }">
        {{ item.rest_wave }}
      </template>

      <template v-slot:item.measured_wave="{ item }">
        <v-icon v-if="item.measured_wave < 1.0">mdi-alert</v-icon>
        <span v-else>{{ item.measured_wave }}</span>
      </template>

      <template v-slot:item.velocity="{ item }">
        <v-icon v-if="item.velocity < 1.0">mdi-alert</v-icon>
        <span v-else>{{ item.velocity }}</span>
      </template>

    </v-data-table>
  </v-card>
</template>

<style scoped>

</style>

<script>
export default {
    data: () => ({
        selected: [],
    }),
}
</script>