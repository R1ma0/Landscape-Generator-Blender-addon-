import bpy
import random



class GenerateLandscape(bpy.types.Operator):
    """Landscape generation depending on the selected settings"""
    bl_idname = "mesh.generate_landscape"
    bl_label = "Generate"
    
    @classmethod
    def poll(cls, context):
        """Condition under which button will be active"""
        return context.active_object is not None
    
    @classmethod
    def description(cls, context, properties):
        """Tooltip for a button"""
        return "Generate a new terrain variant"
    
    def execute(self, context):
        """Generates terrain depending on the selected type"""
        # Enum with landscape types
        terrain = context.scene.my_tool.terrain_type
        # List of material nodes
        node_tree = bpy.data.materials["Landscape"].node_tree
        
        generate_position(node_tree)

        # Plain generation
        if terrain == "PLAIN":
            # Scale
            node_tree.nodes["TG_DisplacementNode"].inputs['Scale'].default_value = random.uniform(0.05, 0.1)
            # Pos
            node_tree.nodes["TG_ColorRamp"].color_ramp.elements[0].position = random.uniform(0.0, 0.2)
            # Roughness
            node_tree.nodes["TG_NoiseTextureNode"].inputs[4].default_value = random.uniform(0.0, 0.5)
            # Distortion
            node_tree.nodes["TG_NoiseTextureNode"].inputs[5].default_value = random.uniform(-0.8, 0.8)
        elif terrain == "PLAIN_WATER":  
                     
            node_tree.nodes["TG_DisplacementNode"].inputs['Scale'].default_value = random.uniform(0.05, 0.10)
            node_tree.nodes["TG_ColorRamp"].color_ramp.elements[0].position = random.uniform(0.35, 0.5)
            node_tree.nodes["TG_NoiseTextureNode"].inputs[4].default_value = random.uniform(0.0, 0.5)
            node_tree.nodes["TG_NoiseTextureNode"].inputs[5].default_value = random.uniform(-0.8, 0.8)
        elif terrain == "MOUNTAINS":
            
            node_tree.nodes["TG_DisplacementNode"].inputs['Scale'].default_value = random.uniform(0.2, 0.4)
            node_tree.nodes["TG_ColorRamp"].color_ramp.elements[0].position = random.uniform(0.0, 0.2)
            node_tree.nodes["TG_NoiseTextureNode"].inputs[4].default_value = random.uniform(0.0, 0.5)
            node_tree.nodes["TG_NoiseTextureNode"].inputs[5].default_value = random.uniform(-0.8, 0.8)
        elif terrain == "ISLANDS":
            
            node_tree.nodes["TG_DisplacementNode"].inputs['Scale'].default_value = random.uniform(0.1, 0.25)
            node_tree.nodes["TG_ColorRamp"].color_ramp.elements[0].position = random.uniform(0.5, 0.65)
            node_tree.nodes["TG_NoiseTextureNode"].inputs[4].default_value = random.uniform(0.0, 0.5)
            node_tree.nodes["TG_NoiseTextureNode"].inputs[5].default_value = random.uniform(-0.8, 0.8)
        elif terrain == "CUSTOM":
            
            min = context.scene.my_tool.displacement_scale_min
            max = context.scene.my_tool.displacement_scale_max
            node_tree.nodes["TG_DisplacementNode"].inputs['Scale'].default_value = random.uniform(min, max)
            
            min = context.scene.my_tool.colorRamp_pos_min
            max = context.scene.my_tool.colorRamp_pos_max
            node_tree.nodes["TG_ColorRamp"].color_ramp.elements[0].position = random.uniform(min, max)
            
            min = context.scene.my_tool.noise_texture_roughness_min
            max = context.scene.my_tool.noise_texture_roughness_max
            node_tree.nodes["TG_NoiseTextureNode"].inputs[4].default_value = random.uniform(min, max)
            
            min = context.scene.my_tool.noise_texture_distortion_min
            max = context.scene.my_tool.noise_texture_distortion_max
            node_tree.nodes["TG_NoiseTextureNode"].inputs[5].default_value = random.uniform(min, max)
        else:
            pass
        
        context.scene.my_tool.displacement_scale_current = node_tree.nodes["TG_DisplacementNode"].inputs['Scale'].default_value
        context.scene.my_tool.colorRamp_pos_current = node_tree.nodes["TG_ColorRamp"].color_ramp.elements[0].position
        context.scene.my_tool.noise_texture_roughness_current = node_tree.nodes["TG_NoiseTextureNode"].inputs[4].default_value
        context.scene.my_tool.noise_texture_distortion_current = node_tree.nodes["TG_NoiseTextureNode"].inputs[5].default_value

        return {'FINISHED'}



class RefreshLandscape(bpy.types.Operator):
    """Updating Terrain Values"""
    bl_idname = "mesh.refresh_landscape"
    bl_label = "Refresh"
    
    @classmethod
    def description(cls, context, properties):
        """Tooltip for a button"""
        return "Update the values of the current variant"
    
    def execute(self, context):
        node_tree = bpy.data.materials["Landscape"].node_tree
        prop = context.scene.my_tool
        
        node_tree.nodes["TG_DisplacementNode"].inputs['Scale'].default_value = prop.displacement_scale_current
        node_tree.nodes["TG_ColorRamp"].color_ramp.elements[0].position = prop.colorRamp_pos_current
        node_tree.nodes["TG_NoiseTextureNode"].inputs[4].default_value = prop.noise_texture_roughness_current
        node_tree.nodes["TG_NoiseTextureNode"].inputs[5].default_value = prop.noise_texture_distortion_current
        
        return {'FINISHED'}


        
def generate_position(node_tree):
    """Location and rotation generation"""
    # Location
    location_value = [-10000.0, 10000.0]
    # x
    node_tree.nodes["TG_MappingNode"].inputs[1].default_value[0] = random.uniform(location_value[0], location_value[1])
    # y
    node_tree.nodes["TG_MappingNode"].inputs[1].default_value[1] = random.uniform(location_value[0], location_value[1])
    # z
    node_tree.nodes["TG_MappingNode"].inputs[1].default_value[2] = random.uniform(location_value[0], location_value[1])
    
    # Rotation
    rotation_value = [-6.28319, 6.28319] # radians (360 degree)
    # x
    node_tree.nodes["TG_MappingNode"].inputs[2].default_value[0] = random.uniform(rotation_value[0], rotation_value[1])
    # y
    node_tree.nodes["TG_MappingNode"].inputs[2].default_value[1] = random.uniform(rotation_value[0], rotation_value[1])
    # z
    node_tree.nodes["TG_MappingNode"].inputs[2].default_value[2] = random.uniform(rotation_value[0], rotation_value[1])
    
    
    
def register():
    bpy.utils.register_class(GenerateLandscape)
    bpy.utils.register_class(RefreshLandscape)
    
    
    
def unregister():
    bpy.utils.unregister_class(GenerateLandscape)
    bpy.utils.unregister_class(RefreshLandscape)
