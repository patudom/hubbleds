<template>
    <v-card>
        <div class="source"  :style="[mystyle]">
            <slot> </slot>
        </div>
        <v-card-text>
            <div class="sliders" >
                <v-expansion-panels :style="inlineStyle">
                    <v-expansion-panel>
                        <v-expansion-panel-header disable-icon-rotate>Adjust Brightness & Contrast</v-expansion-panel-header>
                        <v-expansion-panel-content>
                            <!-- wrap sliders in a class -->
                            <div class="background_contrast_sliders">
                                <!-- Contrast: a continuous (step="0") slider, logscale from .5, 1.5 -->
                                <v-slider
                                    v-model="contrast"
                                    step="0"
                                    :min="Math.log10(0.50)"  
                                    :max="Math.log10(1.50)"
                                    :label="Math.pow(10,contrast).toFixed(2)"
                                    prepend-icon="mdi-contrast-circle"
                                    @click:prepend="resetContrast"
                                    hide-details=true
                                    style="margin:auto;width:75%;"
                                    >
                                </v-slider>
                                <!-- Brighntess slider: a continuous (step="0") slider, logscale from .5, 1.5 -->
                                <v-slider
                                    v-model="brightness"
                                    step="0"
                                    :min=0
                                    :max=4
                                    :label="parseFloat(brightness).toFixed(2)"
                                    prepend-icon="mdi-brightness-6"
                                    @click:prepend="resetBrightness"
                                    hide-details=true
                                    style="margin:auto; width:75%"
                                    >
                                </v-slider>
                            </div>
                        </v-expansion-panel-content>
                    </v-expansion-panel>
                </v-expansion-panels>
            </div>
        </v-card-text>
    </v-card>

</template>



<style>

/* make sure that whatever is in class div.source has a position  above div.sliders */
div.source {
}

div.sliders {
}

</style>


<script>

module.exports = {

    // name of the component. used in the parent component
    // when importing as: import ContrastBrightnessControl from './path/to/ContrastBrightnessControl.vue'
    name: 'ContrastBrightnessControl', 
    
    // props: ['value'], // props are passed in from the parent. they should not be changed in the child
    props: ['inlineStyle'],

    // data are local to the component. they can be changed
    //  data can be declared one of 3 ways:
    //  1. data() { return { key: value, ... } }
    //  2. data: function() { return { key: value, ... } }
    // 3. data: () => { return { key: value, ... } }
    data: () => {
        return {
            contrast: 0,
            brightness: 1
        }
    },
    
    computed: {
        mystyle() {
            console.log('slider style', this.SliderStyle)
            // console.log('contrast', Math.pow(10, this.contrast) * 100)
            // console.log('brightness', this.brightness)
            // console.log('**************')
            brightness = parseFloat(this.brightness).toFixed(2) * 100 // brightness in percent
            contrast = Math.pow(10, this.contrast).toFixed(2) * 100  // contrast in percent
            let newstyle = { filter: `brightness(${brightness}%) contrast(${contrast}%)` }
            this.$emit('newstyle',newstyle)
            return newstyle
            
        },

        sliders_style() {
            return $createStyle(this.inlineStyle)
        },
    },
    

    methods: {
        resetContrast() {
            this.contrast = 0;
        },
        resetBrightness() {
            this.brightness = 1;
        },
    },
    
}

</script>
