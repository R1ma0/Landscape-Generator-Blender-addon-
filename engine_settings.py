import bpy



class EngineSettings(bpy.types.Operator):
    """Setting the required engine settings"""
    bl_idname = "engine.engine_settings"
    bl_label = "Switch To Cycles"
    
    @classmethod
    def poll(cls, context):
        """Condition under which button will be active"""
        return context.scene.render.engine == 'BLENDER_EEVEE'
    
    def execute(self, context):
        """Switches engine and sets settings"""
        # Switching to the Cycles engine
        context.scene.render.engine = 'CYCLES'
        
        # Turn on "Displacement Only"
        context.object.active_material.cycles.displacement_method = 'DISPLACEMENT'
        
        return {'FINISHED'}
    


def register():
    bpy.utils.register_class(EngineSettings)



def unregister():
    bpy.utils.unregister_class(EngineSettings)
    

    
# if __name__ == "__main__":
#     register()