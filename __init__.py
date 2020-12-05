# Add-on information
bl_info = {
    "name": "Terrain Generator",
    "author": "Abdrazackov Damir",
    "description": "Creating landscapes using nodes",
    "version": (0, 3, 3),
    "blender": (2, 83, 5),
    "location": "View3D > Sidebar > TerrainGenerator",
    "category": "Mesh",
    "support": "COMMUNITY",
}



# Imports
if "bpy" in locals():
    import importlib
    importlib.reload(ui)
    importlib.reload(material)
    importlib.reload(generate)
    importlib.reload(engine_settings)
    importlib.reload(properties)
else:
    import bpy
    from . import ui
    from . import material
    from . import generate
    from . import engine_settings
    from . import properties



# Registering modules
def register():
    ui.register()
    material.register()
    generate.register()
    engine_settings.register()
    properties.register()



# Unregistering modules
def unregister():
    ui.unregister()
    material.unregister()
    generate.unregister()
    engine_settings.unregister()
    properties.unregister()



if __name__ == "__main__":
    try:
        unregister()
    except Exception as e:
        print(e)
        pass
    
    register()