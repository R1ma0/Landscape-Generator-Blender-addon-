import bpy



class PanelTemplate(bpy.types.Panel):
    """Template for all panels"""
    bl_space_type = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category = "TerrainGenerator"



class MeshSettingsPanel(PanelTemplate):
    """Panel for object preparation"""
    bl_label = "Settings"
    
    def draw(self, context):
        """MeshSettingsPanel rendering"""
        layout = self.layout
        obj = context.object
        
        # "Add Plane" button
        box = layout.box()
        box.operator("mesh.primitive_plane_add", icon='MESH_PLANE')
        
        # "Subdivide" button
        box.operator("mesh.subdivide", icon='MOD_SUBSURF')
        
        # "Add Material" button
        box.operator("object.create_material", icon='MATERIAL')
        
        # Enable cycles button
        box.operator("engine.engine_settings")



class MeshGeneratePanel(PanelTemplate):
    """Panel for generating landscape"""
    bl_label = "Generate"
    
    @classmethod
    def register(cls):
        """Creating properties"""
        # Terrain presets menu
        terrain_presets = [
            ("PLAIN",       "Hilly Plains",            "", 1),
            ("PLAIN_WATER", "Hilly Plains With Water", "", 2),
            ("MOUNTAINS",   "The Mountains",           "", 3),
            ("ISLANDS",     "Islands",                 "", 4),
        ]
        
        # Terrain menu property
        bpy.types.Scene.terrain_type = bpy.props.EnumProperty(items=terrain_presets, name="Terrain")
    
    @classmethod
    def unregister(cls):
        """Clearing properties"""
        del bpy.context.scene.terrain_type
    
    def draw(self, context):
        """MeshGeneratePanel rendering"""
        layout = self.layout
        box = layout.box()
        
        # "Generate button"
        box.operator("mesh.generate_landscape", icon='RNA_ADD')
        
        # Terrain types menu 
        box.prop(context.scene, "terrain_type")
        
        
        
class CustomizationPanel(PanelTemplate):
    """More precise mesh turning"""
    bl_label = "Customization"
    
    def draw(self, context):
        """CustomizationPanel rendering"""
        layout = self.layout
        box = layout.box()
    
    

def register():
    bpy.utils.register_class(MeshSettingsPanel)
    bpy.utils.register_class(MeshGeneratePanel)
    bpy.utils.register_class(CustomizationPanel)



def unregister():
    bpy.utils.unregister_class(MeshSettingsPanel)
    bpy.utils.unregister_class(MeshGeneratePanel)
    bpy.utils.unregister_class(CustomizationPanel)



# if __name__ == "__main__":
#     try:
#         unregister()
#     except Exception as e:
#         print(e)
#         pass
    
#     register()