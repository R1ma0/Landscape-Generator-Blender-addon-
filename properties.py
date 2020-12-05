import bpy
from bpy.props import FloatProperty, IntProperty, EnumProperty



class CustomizationProperties(bpy.types.PropertyGroup):
    """Customization panel sub-panels"""
    precision = 3
    default = 0.000
    
    # --------------------------------------------------
    # Displacement scale
    min = 0.000
    max = 1000.000
    
    displacement_scale_max: FloatProperty(
        name = "Max",
        description = "Displacement scale max value",
        default = max,
        min = min,
        max = max,
        precision = precision
    )

    displacement_scale_min: FloatProperty(
        name = "Min",
        description = "Displacement scale min value",
        default = min,
        min = min,
        max = max,
        precision = precision
    )

    displacement_scale_current: FloatProperty(
        name = "Current",
        description = "Displacement scale current value",
        default = default,
        min = min,
        max = max,
        precision = precision
    )
    # --------------------------------------------------
    
    
    # --------------------------------------------------
    # ColorRamp pos
    min = 0.000
    max = 1.000
    
    colorRamp_pos_max: FloatProperty(
        name = "Max",
        description = "ColorRamp pos max value",
        default = max,
        min = min,
        max = max,
        precision = precision
    )

    colorRamp_pos_min: FloatProperty(
        name = "Min",
        description = "ColorRamp pos min value",
        default = min,
        min = min,
        max = max,
        precision = precision
    )

    colorRamp_pos_current: FloatProperty(
        name = "Current",
        description = "ColorRamp pos current value",
        default = default,
        min = min,
        max = max,
        precision = precision
    )
    # --------------------------------------------------
    
    
    # --------------------------------------------------
    # Noise texture roughness
    
    min = 0.000
    max = 1.000
    
    noise_texture_roughness_max: FloatProperty(
        name = "Max",
        description = "Noise texture roughness max value",
        default = max,
        min = min,
        max = max,
        precision = precision
    )

    noise_texture_roughness_min: FloatProperty(
        name = "Min",
        description = "Noise texture roughness min value",
        default = min,
        min = min,
        max = max,
        precision = precision
    )

    noise_texture_roughness_current: FloatProperty(
        name = "Current",
        description = "Noise texture roughness current value",
        default = default,
        min = min,
        max = max,
        precision = precision
    )
    # --------------------------------------------------
    
    
    # --------------------------------------------------
    # Noise texture distortion 
    
    min = -1000.000
    max = 1000.000
    
    noise_texture_distortion_max: FloatProperty(
        name = "Max",
        description = "Noise texture distortion max value",
        default = max,
        min = min,
        max = max,
        precision = precision
    )

    noise_texture_distortion_min: FloatProperty(
        name = "Min",
        description = "Noise texture distortion min value",
        default = min,
        min = min,
        max = max,
        precision = precision
    )

    noise_texture_distortion_current: FloatProperty(
        name = "Current",
        description = "Noise texture distortion current value",
        default = default,
        min = min,
        max = max,
        precision = precision
    )
    # --------------------------------------------------
        
    
    # --------------------------------------------------
    # Terrain presets drop down menu
    terrain_type: EnumProperty (
        name = "Terrain",
        items = [
            ("PLAIN",       "Hilly Plains",            "", 1),
            ("PLAIN_WATER", "Hilly Plains With Water", "", 2),
            ("MOUNTAINS",   "The Mountains",           "", 3),
            ("ISLANDS",     "Islands",                 "", 4),
            ("CUSTOM",      "Custom",                  "", 5),
        ]
    )
    


def register():
    bpy.utils.register_class(CustomizationProperties)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=CustomizationProperties)
    
def unregister():
    bpy.utils.unregister_class(CustomizationProperties)
    del bpy.types.Scene.my_tool