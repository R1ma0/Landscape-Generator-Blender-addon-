import bpy



class MaterialSettings(bpy.types.Operator):
    """Working with object material"""
    bl_idname = "object.create_material"
    bl_label = "Create Material"
    
    @classmethod
    def poll(cls, context):
        """Condition under which button will be active"""
        return context.active_object is not None
    
    def execute(self, context):
        """Creating material. Deleting, linking and adding nodes"""
        # Creating material
        create_new_material(context)
        
        # Material selection
        material = bpy.data.materials["Landscape"]
        
        # Removing nodes
        delete_nodes(context, material)
        
        # Adding nodes
        add_nodes(context, material)
        
        # Linking nodes
        link_nodes(context, material)
        return {'FINISHED'}



def create_new_material(context):
    """Material creation and application to object"""
    # Select active object
    active_object = bpy.context.active_object
    
    # Get material
    material = bpy.data.materials.get("Landscape")
        
    # If there is no such material
    if material is None:
        # Create material
        material = bpy.data.materials.new(name="Landscape")
    
    # Placing material in the first slot
    if active_object.data.materials:
        active_object.data.materials[0] = material
    else:
        # If there are no sloth then add
        active_object.data.materials.append(material)
        
    # Enable display of nodes
    material.use_nodes = True



def add_nodes(context, material):
    """Adding the necessary nodes to customize the landscape"""
    tree = material.node_tree.nodes
    
    # Material Output node
    output = tree.new('ShaderNodeOutputMaterial')
    output.name = "TG_MaterialOutput"
    output.location = (250, 0)
    
    # Fresnel
    fresnel = tree.new('ShaderNodeFresnel')
    fresnel.name = "TG_FresnelNode"
    fresnel.location = (50, 150)
    
    # Add displacement node
    displacement = tree.new('ShaderNodeDisplacement')
    displacement.name = "TG_DisplacementNode"
    displacement.location = (50, 0)
    
    # Add noise texture node
    noise = tree.new('ShaderNodeTexNoise')
    noise.name = "TG_NoiseTextureNode"
    noise.location = (-450, 0)
    
    # Add Color Ramp node
    color_ramp = tree.new('ShaderNodeValToRGB')
    color_ramp.name = "TG_ColorRamp"
    color_ramp.location = (-250, 0)
    
    # Mapping node
    mapping = tree.new('ShaderNodeMapping')
    mapping.name = "TG_MappingNode"
    mapping.location = (-650, 0)
    
    # Texture coordinate node
    tex_coord = tree.new('ShaderNodeTexCoord')
    tex_coord.name = "TG_TexCoordNode"
    tex_coord.location = (-850, 0)
    
    
    
def delete_nodes(context, material):
    """Remove nodes so that they do not overlap"""
    for node in list(material.node_tree.nodes):
        material.node_tree.nodes.remove(node)
    
    
    
def link_nodes(context, material):
    """Linking nodes together"""
    # Getting a tree of nodes
    node_tree = bpy.data.materials["Landscape"].node_tree
    
    # Linking nodes
    material.node_tree.links.new(node_tree.nodes["TG_DisplacementNode"].outputs['Displacement'], node_tree.nodes["TG_MaterialOutput"].inputs['Displacement'])
    material.node_tree.links.new(node_tree.nodes["TG_FresnelNode"].outputs['Fac'], node_tree.nodes["TG_MaterialOutput"].inputs['Surface'])
    material.node_tree.links.new(node_tree.nodes["TG_ColorRamp"].outputs['Color'], node_tree.nodes["TG_DisplacementNode"].inputs['Height'])
    material.node_tree.links.new(node_tree.nodes["TG_NoiseTextureNode"].outputs['Fac'], node_tree.nodes["TG_ColorRamp"].inputs['Fac'])
    material.node_tree.links.new(node_tree.nodes["TG_MappingNode"].outputs['Vector'], node_tree.nodes["TG_NoiseTextureNode"].inputs['Vector'])
    material.node_tree.links.new(node_tree.nodes["TG_TexCoordNode"].outputs['Generated'], node_tree.nodes["TG_MappingNode"].inputs['Vector'])



def register():
    bpy.utils.register_class(MaterialSettings)
    
    
    
def unregister():
    bpy.utils.unregister_class(MaterialSettings)