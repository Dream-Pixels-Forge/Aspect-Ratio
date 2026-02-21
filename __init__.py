from . import keymap
from . import properties
from . import menus
from . import panels
from . import operators
from importlib import reload
from types import ModuleType
import sys
import bpy

bl_info = {
    "name": "Advanced Aspect Ratio",
    "author": "Dimona Patrick",
    "version": (1, 4, 0),
    "blender": (5, 0, 0),
    "location": "Properties > Render > Aspect Ratio",
    "description": "Advanced aspect ratio manager with camera overlay and composition guides",
    "category": "Render",
    "doc_url": "",
    "tracker_url": "",
    "license": "GPL-3.0-or-later",
}


modules = (
    "operators",
    "panels",
    "menus",
    "properties",
    "keymap",
)

if "bpy" in locals():
    for mod_name in modules:
        if mod_name in locals():
            reload(locals()[mod_name])


classes = (
    properties.AspectRatioSettings,
    operators.ASPECT_OT_SetRatio,
    operators.ASPECT_OT_SetLens,
    panels.ASPECT_PT_Panel,
    menus.ASPECT_MT_lens_wide_menu,
    menus.ASPECT_MT_lens_tele_menu,
    menus.ASPECT_MT_cinema_menu,
    menus.ASPECT_MT_photo_menu,
    menus.ASPECT_MT_social_menu,
    menus.ASPECT_MT_pie_menu,
)


def register():
    """Register all addon classes and properties."""
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.aspect_ratio_settings = bpy.props.PointerProperty(
        type=properties.AspectRatioSettings
    )

    keymap.register()


def unregister():
    """Unregister all addon classes and properties."""
    keymap.unregister()

    del bpy.types.Scene.aspect_ratio_settings

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
