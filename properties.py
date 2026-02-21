"""Property group and preset data for aspect ratio settings."""

import bpy
from bpy.props import BoolProperty, EnumProperty
from bpy.types import PropertyGroup


ASPECT_RATIOS = [
    (
        "CINEMA",
        "Cinema",
        [
            ("2.39:1", 2.39, "Anamorphic Widescreen"),
            ("1.85:1", 1.85, "Standard Widescreen"),
            ("1.43:1", 1.43, "IMAX"),
        ],
    ),
    (
        "PHOTO",
        "Photography",
        [
            ("3:2", 1.5, "Standard DSLR"),
            ("4:3", 1.33, "Medium Format"),
            ("1:1", 1.0, "Square Format"),
            ("16:9", 1.77, "HD Video"),
        ],
    ),
    (
        "SOCIAL",
        "Social Media",
        [
            ("9:16", 0.5625, "Instagram Story/TikTok"),
            ("4:5", 0.8, "Instagram Portrait"),
            ("1:1", 1.0, "Instagram Square"),
            ("16:9", 1.77, "YouTube"),
        ],
    ),
]


def update_camera_guides(self, context):
    """Update camera composition guides based on selected guide type.

    :param self: The property group instance.
    :param context: The Blender context.
    """
    if context.scene.camera:
        camera = context.scene.camera.data
        camera.show_composition_thirds = False
        camera.show_composition_golden = False
        camera.show_composition_center = False

        if self.guide_type == "THIRDS":
            camera.show_composition_thirds = True
        elif self.guide_type == "GOLDEN":
            camera.show_composition_golden = True
        elif self.guide_type == "CENTER":
            camera.show_composition_center = True

        camera.show_composition_grid = True
        camera.show_name = True
        camera.show_passepartout = True
        camera.passepartout_alpha = 1.0


class AspectRatioSettings(PropertyGroup):
    """Property group for aspect ratio addon settings."""

    adjust_width: BoolProperty(
        name="Adjust Width",
        description="Adjust width instead of height when setting aspect ratio",
        default=True,
    )

    guide_type: EnumProperty(
        name="Composition Guide",
        description="Type of composition guide to display",
        items=[
            ("NONE", "None", "No guides"),
            ("THIRDS", "Rule of Thirds", "Display rule of thirds grid"),
            ("GOLDEN", "Golden Ratio", "Display golden ratio"),
            ("CENTER", "Center", "Display center lines"),
        ],
        default="THIRDS",
        update=update_camera_guides,
    )

    category: EnumProperty(
        name="Category",
        items=[(cat[0], cat[1], "") for cat in ASPECT_RATIOS],
        default="CINEMA",
    )

    show_overlay: BoolProperty(
        name="Show Overlay",
        description="Show aspect ratio overlay in viewport",
        default=True,
    )

    show_info: BoolProperty(
        name="Show Info",
        description="Show aspect ratio info in viewport",
        default=True,
    )

    overlay_opacity: EnumProperty(
        name="Overlay Opacity",
        description="Opacity of the overlay",
        items=[
            ("0.25", "25%", ""),
            ("0.5", "50%", ""),
            ("0.75", "75%", ""),
            ("1.0", "100%", ""),
        ],
        default="0.5",
    )


def register():
    """Register properties."""


def unregister():
    """Unregister properties."""
