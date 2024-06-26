<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Reflect on Your Data"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >

    <template #before-next>
      Click <span class="inline-guideline-button" style="background-color: var(--warning-dark);">REFLECT</span> button.
    </template>

    <div
      class="mb-4"
    >
      <p>
        As scientists do, let’s examine what conclusions you might draw from your data.
      </p>
      <p>
        Click the <span class="inline-guideline-button" style="background-color: var(--warning-dark);">REFLECT</span> button to complete the reflection sequence before moving on.
      </p>
    </div>
  </scaffold-alert>
</template>