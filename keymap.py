"""Keymap registration for pie menu."""

import bpy


addon_keymaps = []


def register():
    """Register keymap for pie menu."""
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        km = kc.keymaps.new(name="Screen", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "wm.call_menu_pie",
            "R",
            "PRESS",
            shift=True,
            alt=True,
        )
        kmi.properties.name = "ASPECT_MT_pie_menu"
        addon_keymaps.append((km, kmi))


def unregister():
    """Unregister keymap."""
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
