<template>
  <scaffold-alert
    title-text="Shortcomings in Your Estimate"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
        Enter your responses.
    </template>
    <div
      class="mb-4"
    >
      <p>
        Part of the scientific process is probing at potential weaknesses in your measurement, including the overall methods and execution. Try to identify some shortcomings in the approach this data story takes in the measurement of the age of the universe to this point or any difficulties you had with the process. (What are some reasons you or someone else might question your result?)
      </p>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Shortcoming #1"
        :tag="state_view.free_response_a.tag"
        :initial-response="state_view.free_response_a.response"
        :initialized="state_view.free_response_a.initialized"
        @fr-emit="fr_callback($event)"
      ></free-response>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Shortcoming #2"
        :tag="state_view.free_response_b.tag"
        :initial-response="state_view.free_response_b.response"
        :initialized="state_view.free_response_b.initialized"
        @fr-emit="fr_callback($event)"
      ></free-response>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="Other Shortcomings"
        hint="(if you can think of any more)"
        :tag="state_view.free_response_c.tag"
        :initial-response="state_view.free_response_c.response"
        :initialized="state_view.free_response_c.initialized"
        @fr-emit="fr_callback($event)"
        :allow-empty="true"
      ></free-response>
    </div>
  </scaffold-alert>
</template>
<script>
</script>