import bpy



class PanelTemplate(bpy.types.Panel):
    """Template for all panels"""
    bl_space_type = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category = "TerrainGenerator"



class MeshSettingsPanel(PanelTemplate):
    """Panel for object preparation"""
    bl_label = "Settings"
    bl_options = {"DEFAULT_CLOSED"}
    
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
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        """MeshGeneratePanel rendering"""
        layout = self.layout
        box = layout.box()
        
        # "Generate button"
        box.operator("mesh.generate_landscape", icon='RNA_ADD')
        
        # Terrain types menu 
        box.prop(context.scene.my_tool, "terrain_type")
        
        
        
class CustomizationPanel(PanelTemplate):
    """More precise mesh turning"""
    bl_idname = "CustomizationPanel"
    bl_label = "Customization"
    bl_options = {"DEFAULT_CLOSED"}
    
    @classmethod
    def poll(cls, context):
        """Condition under which menu will be active"""
        return context.scene.my_tool.terrain_type == "CUSTOM"
    
    def draw(self, context):
        """CustomizationPanel rendering"""
        layout = self.layout
        
        # Refresh button
        layout.operator("mesh.refresh_landscape", icon="FILE_REFRESH")
    


class HeightCustomizationSubPanel(PanelTemplate, bpy.types.Panel):
    """Sub-panel CustomizationPanel (Height)"""
    bl_parent_id = "CustomizationPanel"
    bl_label = "Terrain Height"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        tool = context.scene.my_tool
        
        box = layout.box()
        
        box.prop(tool, "displacement_scale_max")
        box.prop(tool, "displacement_scale_min")
        box.prop(tool, "displacement_scale_current")




class WaterCustomizationSubPanel(PanelTemplate, bpy.types.Panel):
    """Sub-panel CustomizationPanel (Water)"""
    bl_parent_id = "CustomizationPanel"
    bl_label = "Terrain Water"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        tool = context.scene.my_tool
        
        box = layout.box()
        
        box.prop(tool, "colorRamp_pos_max")
        box.prop(tool, "colorRamp_pos_min")
        box.prop(tool, "colorRamp_pos_current")
        
        
        
class RoughnessCustomizationSubPanel(PanelTemplate, bpy.types.Panel):
    """Sub-panel CustomizationPanel (Roughness)"""
    bl_parent_id = "CustomizationPanel"
    bl_label = "Terrain Roughness"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        tool = context.scene.my_tool
        
        box = layout.box()
        box.prop(tool, "noise_texture_roughness_max")
        box.prop(tool, "noise_texture_roughness_min")
        box.prop(tool, "noise_texture_roughness_current")
        
        
        
class DistortionCustomizationSubPanel(PanelTemplate, bpy.types.Panel):
    """Sub-panel CustomizationPanel (Distortion)"""
    bl_parent_id = "CustomizationPanel"
    bl_label = "Terrain Distortion"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        tool = context.scene.my_tool
        
        box = layout.box()
        box.prop(tool, "noise_texture_distortion_max")
        box.prop(tool, "noise_texture_distortion_min")
        box.prop(tool, "noise_texture_distortion_current")
        
        

def register():
    bpy.utils.register_class(MeshSettingsPanel)
    bpy.utils.register_class(MeshGeneratePanel)
    bpy.utils.register_class(CustomizationPanel)
    bpy.utils.register_class(HeightCustomizationSubPanel)
    bpy.utils.register_class(RoughnessCustomizationSubPanel)
    bpy.utils.register_class(DistortionCustomizationSubPanel)
    bpy.utils.register_class(WaterCustomizationSubPanel)



def unregister():
    bpy.utils.unregister_class(MeshSettingsPanel)
    bpy.utils.unregister_class(MeshGeneratePanel)
    bpy.utils.unregister_class(CustomizationPanel)
    bpy.utils.unregister_class(HeightCustomizationSubPanel)
    bpy.utils.unregister_class(RoughnessCustomizationSubPanel)
    bpy.utils.unregister_class(DistortionCustomizationSubPanel)
    bpy.utils.unregister_class(WaterCustomizationSubPanel)