<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Introducing the Guidelines"
    @next="state.marker_forward = 1"
    :allow-back="false"
  >
    <template #back-content>
      <div>
        Open menu to return to earlier stages.<br>
        (Open/close menu with <v-icon>mdi-menu</v-icon> above)
      </div>
    </template>
    <div
      class="mb-4"
    >
      <p>
        <strong>These are guideline boxes. They will help you as you move through the story.</strong>
      </p>
      <p>
        The information in the guideline boxes will suggest what you should focus on, or what you should do next.
      </p>
      <p>
        The images, tables, or graph where the guideline suggests action will also be highlighted with an <strong>orange outline</strong>.
      </p>
    </div>
    
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
