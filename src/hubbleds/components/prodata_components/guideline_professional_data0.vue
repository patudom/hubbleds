<template>
  <scaffold-alert
    header-text="Professional Data"
    @back="
      state.marker = 'con_int2c';
    "
    @next="
      state.marker = 'pro_dat1';
      state.prodata_response = false;
    "
  >
    <div
      class="mb-4"
    >
    Let's now turn to professional astronomers' data and see how that compares to your class's data (in teal).

    </div>
  </scaffold-alert>
</template>






