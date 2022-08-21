---VERTEX SHADER---
#ifdef GL_ES
    precision highp float;
#endif

/* output to the fragment shader */
varying vec4 frag_color;
varying vec2 text_coord0;

/* vertex attributes */
attribute vec2 vPosition;
attribute vec2 vTextCoords0;

/* uniform variables */
uniform mat4 modelview_mat;
uniform mat4 projection_mat;
uniform vec4 color;
uniform float opacity;

void main (void){
    frag_color = color * vec4(1.0, 1.0, 1.0, opacity);
    tex_coord0 = vTexCoords0;
    gl_Position = projection_mat * modelview_mat * vec4(vPosition.xy, 0.0, 1.0);

}

---FRAGMENT SHADER---
#ifdef GL_ES
    precision highp float;
#endif

/* input from the vertex shader */
varying vec4 frag_color;
varying vec2 tex_coord0;

/* uniform texture samplers */
uniform sampler2D texture0;

/* this is the only part of the default shader we need to change to grayscale our picture: we need to take the average of rgb channels and then assign rgb to be the avaregae */
void main (void){
    vec4 pixel_color = frag_color * texture2D(texture0, tex_coord0);
    float average = (pixel_color[0] + pixel_color[1] + pixel_color[2])/3.;
    gl_fragColor = vec4(average, average, average, pixel_color[3]);
}

