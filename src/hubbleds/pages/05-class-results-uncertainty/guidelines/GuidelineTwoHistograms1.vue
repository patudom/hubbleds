<!-- this state.marker = 'two_his1' -->
<template>
  <scaffold-alert
    title-text="Student Histogram vs. Class Histogram"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        The top graph shows the age values measured by All Students who have completed this Data Story. 
      </p>
      <p>
        Notice how the All Students histogram (top) differs from the All Classes histogram (bottom).
      </p>
    </div>
  </scaffold-alert>
</template>

