<template>
  <scaffold-alert
    header-text="Professional Data"
    @back="
      state.marker = 'con_int2c';
    "
    @next="
      state.marker = 'pro_dat1';
    "
  >
    <div
      class="mb-4"
    >
    Let's now turn to professional astronomers' data and see how that compares to your class's data.

    </div>
  </scaffold-alert>
</template>






