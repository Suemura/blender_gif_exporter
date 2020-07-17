# blender_gif_exporter
<img width="1920" alt="out.gif (720.8 kB)" src="https://img.esa.io/uploads/production/attachments/9489/2020/07/16/78640/3351bca1-aedd-455b-a1ad-d2c40b716fe7.gif">

<img width="20" alt="out.gif (785.6 kB)" src="https://img.esa.io/uploads/production/attachments/9489/2020/07/16/78640/aa99aad6-f6cf-4e43-a991-5aeb8c2d68f2.gif">**This add-on is incomplete.**<img width="20" alt="out.gif (785.6 kB)" src="https://img.esa.io/uploads/production/attachments/9489/2020/07/16/78640/aa99aad6-f6cf-4e43-a991-5aeb8c2d68f2.gif">  
This add-on creates a gif file from multiple images rendered with Blender.

## Why?
I wanted the rendered image to be a GIF file immediately.  

## Where?
`IMAGE_EDITOR > UI > Gif Exporter `

## Installation
install pillow  

`$ cd C:\Program Files\Blender Foundation\Blender 2.83\2.83\python\bin `  
`$ .\python.exe -m pip install pillow `  

## How to use?
Just press the button once you have rendered.  
Refer to the output destination set in Blender and export as a Gif file.  

images import from "render.filepath" on blender setting.  
gif image output to "gif_output_directory" on this addon setting.  
<img width="840" alt="image.png (214.1 kB)" src="https://img.esa.io/uploads/production/attachments/9489/2020/07/16/78640/e4f16a5d-0fe7-4fd4-a206-47b8690140a6.png">
## use alpha
RGB or RGBA ?
## invert
Reverse playback
## loop counts
- 0 : Forever
- 1～9999 : Counts
## duration
Time per frame
