"""Operators for aspect ratio and lens management."""

import bpy
from bpy.props import FloatProperty, StringProperty
from bpy.types import Operator


class ASPECT_OT_SetRatio(Operator):
    """Set render resolution aspect ratio.

    :param ratio: The aspect ratio to apply.
    :param name: Display name of the aspect ratio.
    :param description: Description of the aspect ratio.
    :type ratio: float
    :type name: str
    :type description: str
    """

    bl_idname = "aspect.set_ratio"
    bl_label = "Set Aspect Ratio"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "Set render resolution aspect ratio"

    ratio: FloatProperty()
    name: StringProperty()
    description: StringProperty()

    def execute(self, context):
        """Execute the operator."""
        scene = context.scene
        settings = scene.aspect_ratio_settings
        render = scene.render

        if settings.adjust_width:
            render.resolution_x = int(render.resolution_y * self.ratio)
        else:
            render.resolution_y = int(render.resolution_x / self.ratio)

        self.report({"INFO"}, f"Set aspect ratio to {self.name}")
        return {"FINISHED"}


class ASPECT_OT_SetLens(Operator):
    """Set camera lens focal length.

    :param focal_length: The focal length in millimeters.
    :type focal_length: float
    """

    bl_idname = "aspect.set_lens"
    bl_label = "Set Lens"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "Set camera lens focal length"

    focal_length: FloatProperty(
        default=50.0,
        min=1.0,
        max=10000.0,
        unit="LENGTH",
    )

    def execute(self, context):
        """Execute the operator."""
        camera = context.scene.camera
        if camera:
            camera.data.lens = self.focal_length
            self.report({"INFO"}, f"Set lens to {self.focal_length}mm")
        else:
            self.report({"WARNING"}, "No active camera")
        return {"FINISHED"}


def register():
    """Register operators."""


def unregister():
    """Unregister operators."""
