"""Panel for aspect ratio management in render properties."""

import bpy
from bpy.types import Panel

from . import properties


class ASPECT_PT_Panel(Panel):
    """Advanced Aspect Ratio Panel for Render settings."""

    bl_label = "Aspect Ratio"
    bl_idname = "ASPECT_PT_Panel"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "render"
    bl_options = {"DEFAULT_CLOSED"}
    bl_description = "Manage aspect ratios and camera settings"

    def draw(self, context):
        """Draw the panel UI."""
        layout = self.layout
        settings = context.scene.aspect_ratio_settings

        box = layout.box()
        row = box.row()
        row.label(text="Overlay Settings", icon="OVERLAY")

        row = box.row(align=True)
        row.prop(settings, "show_overlay", icon="RESTRICT_VIEW_OFF")
        row.prop(settings, "show_info", icon="INFO")

        row = box.row(align=True)
        row.prop(settings, "overlay_opacity")
        row.prop(settings, "guide_type")

        camera = context.scene.camera
        if camera:
            cam_data = camera.data

            box = layout.box()
            row = box.row()
            row.label(text="Camera Display", icon="CAMERA_DATA")

            col = box.column(align=True)
            col.prop(cam_data, "show_composition_grid", text="Show Grid")
            col.prop(cam_data, "show_name", text="Show Camera Name")
            col.prop(cam_data, "show_passepartout", text="Show Passepartout")
            if cam_data.show_passepartout:
                col.prop(cam_data, "passepartout_alpha", text="Passepartout Opacity")

        box = layout.box()
        row = box.row()
        row.label(text="Aspect Ratios", icon="CAMERA_DATA")
        row = box.row()
        row.prop(settings, "category", expand=True)

        for cat in properties.ASPECT_RATIOS:
            if cat[0] == settings.category:
                ratios = cat[2]
                buttons_per_row = 2

                for i in range(0, len(ratios), buttons_per_row):
                    row = box.row(align=True)
                    row_ratios = ratios[i : i + buttons_per_row]

                    for name, ratio, desc in row_ratios:
                        op = row.operator(
                            "aspect.set_ratio", text=f"{name}", icon="CAMERA_DATA"
                        )
                        op.ratio = ratio
                        op.name = name
                        op.description = desc
                break

        box = layout.box()
        row = box.row()
        row.label(text="Settings", icon="PREFERENCES")
        row = box.row()
        row.prop(settings, "adjust_width", icon="ARROW_LEFTRIGHT")

        box = layout.box()
        row = box.row()
        row.label(text="Current Settings", icon="INFO")

        render = context.scene.render
        current_ratio = render.resolution_x / render.resolution_y

        col = box.column(align=True)
        row = col.row(align=True)
        row.label(text=f"Resolution: {render.resolution_x} x {render.resolution_y}")
        row = col.row(align=True)
        row.label(text=f"Aspect Ratio: {current_ratio:.3f}:1")


def register():
    """Register panel."""


def unregister():
    """Unregister panel."""
