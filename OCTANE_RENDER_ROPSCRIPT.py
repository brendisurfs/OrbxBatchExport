"""Made by Brendan Prednis, 2021, at like 12am. 
Description: this code is to batch export ORBX files from the Octane ROP."""

import hou

def exportORBXFrames():  

    """Retrieve the ORBX batch exporter node parms: 
        #frame start, end, interval, and file directory."""
    ORBX_batch_node = hou.pwd()
    #ORBX_batch_node = hou.node("/obj/ORBX_Batch_Export/")  #DEV/DEBUGGING BLOCK
    
    scene_startframe = ORBX_batch_node.parm("frame_min").eval()
    scene_endframe = ORBX_batch_node.parm("frame_max").eval()
    user_export_interval = ORBX_batch_node.parm("frame_range").eval()
    user_OctaneROP_selection = ORBX_batch_node.parm("user_OctaneROP").eval()
    user_naming_params = 'my_project'
    
    octane_ROP = hou.node(user_OctaneROP_selection)

    user_export_path = ORBX_batch_node.parm("user_export_path").eval()
    if user_export_path == "":
        hou.ui.displayMessage("Please add an export path to the node.")
        
    # check if the option is enable to export orbx. IF not, set it. 
    export_enabled_toggle = octane_ROP.parm("HO_abc_exportEnabled")
    if export_enabled_toggle.eval() == 0:
        export_enabled_toggle.set(1)
                                           
    #Octane ROP Frames and parms to modify.
    octane_ROP_startframe = octane_ROP.parm("f1")
    octane_ROP_endframe = octane_ROP.parm("f2")
    octane_ROP_orbx_filename = octane_ROP.parm("HO_abc_exportFileName")
    octane_ROP_render = octane_ROP.parm("execute")
    octane_ROP_cameraMB = octane_ROP.parm("HO_mbCamera")
    
    #removes the automatic setting of $FSTART and $FEND in the Octane ROP
    octane_ROP_startframe.deleteAllKeyframes()
    octane_ROP_endframe.deleteAllKeyframes()
    
    #remove the camera motion blur (causes extra dead frames)
    octane_ROP_cameraMB.set(0)
    
    #======================RENDER SECTION======================================   
    n = scene_startframe
    while (n + user_export_interval) < scene_endframe:
        section_endframe = n + user_export_interval
        octane_ROP_startframe.set(n)
        octane_ROP_endframe.set(section_endframe - 1)
        octane_ROP_orbx_filename.set('{uxp}{unp}_{n}_{section_endframe}'.format(uxp = user_export_path, unp=user_naming_params, n= int(n), section_endframe = int(section_endframe)))
        octane_ROP_render.pressButton()
        print(octane_ROP_orbx_filename.eval())
        n = section_endframe + 1
        #for when the scene interval doesnt fit into the final frames
    else:
        user_export_interval = scene_endframe - section_endframe
        final_section_startframe = section_endframe
        octane_ROP_startframe.set(final_section_startframe)
        octane_ROP_endframe.set(section_endframe)                       
        octane_ROP_orbx_filename.set('{uxp}{unp}_{sec_start}_{scn_end}'.format(uxp = user_export_path, unp = user_naming_params, sec_start= int(final_section_startframe), scn_end= int(scene_endframe)))
        octane_ROP_render.pressButton()
        print(octane_ROP_orbx_filename.eval())
        final_section_startframe += user_export_interval
    
    #FINISH
    print("Done!")
    
        
  

        
        
 
    