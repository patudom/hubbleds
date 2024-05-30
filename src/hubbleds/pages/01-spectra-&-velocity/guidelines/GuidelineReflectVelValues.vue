<template>
  <scaffold-alert
    title-text="How fast are these galaxies"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Choose a response
    </template>
    <div
      class="mb-4"
    >
      <p>
        Take a moment to consider what these velocity values mean. A typical car on the highway moves at 60 mph, which is about 0.03 km/s. 
      </p>
      <p>
        How many times faster are these galaxies moving compared with a car?
      </p>
      <mc-radiogroup 
          :radio-options="[
            'The galaxies move about the same speed as a car.',
            'The galaxies move about 100,000 times faster than a car.',
            'The galaxies move about 100,000 times slower than a car'
            ]"
            :feedbacks="[
            'Try again. Compare the values in the velocity column of your table with the velocity of a car (about 0.03 km/s).',
            'Correct! These galaxies are moving at much, much greater speeds than a car on the road.',
            'Try again. Compare the values in the velocity column of your table with the velocity of a car (about 0.03 km/s).'
            ]" 
          :correct-answers="[1]"
          :wrong-answers="[0, 2]"
          @select="(opt) => { if (opt.correct) { console.log('correct'); $emit('ready'); } }"
          score-tag="reflect_vel_value">
            >
          </mc-radiogroup>
    </div>
  </scaffold-alert>
</template>

