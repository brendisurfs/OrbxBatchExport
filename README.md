# Houdini ORBX Batch Exporter

## By Brendan Prednis

### Why?
I, among other Houdini users, have run into the issue of trying to export massive Houdini animations to ORBX, only to reach the limits of what a single ORBX file can handle for now. Being an incredibly useful file format for the Octane ecosystem, I wanted to make it as effortless as possible to send these massive scenes to the RNDR network to render.

### What can I do with the code? 
If you work in another DCC, such as Cinema4D or Blender, I would be thrilled if you used this code to build the same feature for those applications. 
While I have used both programs mentioned, I spend 99% of my 3D time in Houdini. 
I believe it would be better for someone with an understanding of the certain caveats and behaviors of their main program to port this.
All I ask is that you give credit to me and link this Github, and of course share your creation with me if you build off of it! 

### What if I find a bug/issue?
Please file an issue on Github with your Houdini version, OS, Octane version, and a desccription of what you are trying to make happen vs. what is actually happening. 
It is innevitable that issues may arise with so many different systems and setups, and I will try to find the issue as best as I can. 
I welcome the Houdini programming community to help as well if they run into an issue. 


### Important to know
All rights belong to their respective owners. I am not professionally affiliated with, nor do I work for Otoy, the Octane core team, or any other related party. 
I am a web developer with a love for web-oriented processes and 3D rendering.




# INSTRUCTIONS

This node is for batch exporting ORBX files from the Octane ROP in Houdini.

You are going to need:

- Octane (hopefully you have it)

- A mouse that works

- A plan?

### Step 1. 
Set your Octane ROP. Set your output folder for the ORBX batch exporter to export to.

### Step 2.
 Set your appropriate scene start and end frames. By default these are $FSTART and $FEND. Feel free to modify these as necessary.

### Step 3. 
Set your batching interval. Example: 12 on the int slider means it will batch 12 frames together in an orbx. If the scene cannot be divided in increments of 12 evenly, it will auto calculate the necessary final section to export.

### Step 4. 
Hitting export will export to your orbx folder destination. It will print in the python console the location and number of batches exported.

a video breakdown can be found here: https://vimeo.com/551334253