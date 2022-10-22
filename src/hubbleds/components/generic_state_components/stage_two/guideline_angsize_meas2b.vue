<template>
  <scaffold-alert
    header-text="Angular Size Measurement"
    @back="
      state.marker = 'ang_siz2';
    "
    @next="state.marker = 'ang_siz3';"
  >
    <div
      class="mb-4"
    >
    <p> 
      The angular scale is measured in either in degrees (&#176;&thinsp;), arcminutes (&thinsp;'&thinsp;), or arcseconds (&thinsp;"&thinsp;) as you zoom in.  
    </p>
     <p> 
      One <strong>arcminute</strong> is 1/60 of a degree, and one <strong>arcsecond</strong> is 1/60 of an arcminute 
    </p>
    <p> The data in your table will be measured in arcseconds.</p>
      
    </div>
  </scaffold-alert>
</template>