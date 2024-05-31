<template>
  <scaffold-alert
    title-text="Angular Size Measurement"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
    <p> 
      The angular scale is measured in degrees (&#176;&thinsp;), arcminutes (&thinsp;'&thinsp;), or arcseconds (&thinsp;"&thinsp;) as you zoom in.  
    </p>
     <p> 
      There are 60 <b>arcminutes</b> in 1 degree, and 60 <b>arcseconds</b> in 1 arcminute.
    </p>
    <p> The data in your table will be measured in arcseconds.</p>
      
    </div>
  </scaffold-alert>
</template>