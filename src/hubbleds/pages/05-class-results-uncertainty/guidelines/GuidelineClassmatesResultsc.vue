<template>
  <scaffold-alert
    title-text="Classmates' Data"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        Now let’s look at age estimates of the universe from other classes who have already completed this data story.
      </p>
      <p>
        Your class's graph is highlighted in {{ state_view.my_class_color }}. Other classes are shown in {{ state_view.other_class_color }}.
      </p>
      <p>
        Use the slider to scan through the age estimates that each participating class measured. 
      </p>
      <p>
        Click <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-select-search</v-icon></v-btn> to zoom in to a smaller velocity or distance range.
      </p>
    </div>
  </scaffold-alert>
</template>

