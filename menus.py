"""Menus and pie menu for aspect ratio quick access."""

from bpy.types import Menu

from . import properties


LENS_PRESETS = [
    ("14mm", 14, "Ultra Wide Angle"),
    ("24mm", 24, "Wide Angle"),
    ("35mm", 35, "Standard Wide"),
    ("50mm", 50, "Normal"),
    ("85mm", 85, "Portrait"),
    ("135mm", 135, "Telephoto"),
    ("200mm", 200, "Long Telephoto"),
]


class ASPECT_MT_lens_wide_menu(Menu):
    """Wide angle lens presets menu."""

    bl_label = "Wide Angle Lenses"
    bl_idname = "ASPECT_MT_lens_wide_menu"

    def draw(self, context):
        """Draw the menu."""
        layout = self.layout
        for name, focal_length, desc in LENS_PRESETS[:3]:
            op = layout.operator("aspect.set_lens", text=f"{name} - {desc}")
            op.focal_length = focal_length


class ASPECT_MT_lens_tele_menu(Menu):
    """Telephoto lens presets menu."""

    bl_label = "Telephoto Lenses"
    bl_idname = "ASPECT_MT_lens_tele_menu"

    def draw(self, context):
        """Draw the menu."""
        layout = self.layout
        for name, focal_length, desc in LENS_PRESETS[4:]:
            op = layout.operator("aspect.set_lens", text=f"{name} - {desc}")
            op.focal_length = focal_length


class ASPECT_MT_cinema_menu(Menu):
    """Cinema aspect ratios menu."""

    bl_label = "Cinema Ratios"
    bl_idname = "ASPECT_MT_cinema_menu"

    def draw(self, context):
        """Draw the menu."""
        layout = self.layout
        for name, ratio, desc in properties.ASPECT_RATIOS[0][2]:
            op = layout.operator("aspect.set_ratio", text=f"{name} - {desc}")
            op.ratio = ratio
            op.name = name
            op.description = desc


class ASPECT_MT_photo_menu(Menu):
    """Photography aspect ratios menu."""

    bl_label = "Photo Ratios"
    bl_idname = "ASPECT_MT_photo_menu"

    def draw(self, context):
        """Draw the menu."""
        layout = self.layout
        for name, ratio, desc in properties.ASPECT_RATIOS[1][2]:
            op = layout.operator("aspect.set_ratio", text=f"{name} - {desc}")
            op.ratio = ratio
            op.name = name
            op.description = desc


class ASPECT_MT_social_menu(Menu):
    """Social media aspect ratios menu."""

    bl_label = "Social Media Ratios"
    bl_idname = "ASPECT_MT_social_menu"

    def draw(self, context):
        """Draw the menu."""
        layout = self.layout
        for name, ratio, desc in properties.ASPECT_RATIOS[2][2]:
            op = layout.operator("aspect.set_ratio", text=f"{name} - {desc}")
            op.ratio = ratio
            op.name = name
            op.description = desc


class ASPECT_MT_pie_menu(Menu):
    """Pie menu for quick access to aspect ratios and lens presets."""

    bl_label = "Aspect Ratio & Lens"
    bl_idname = "ASPECT_MT_pie_menu"

    def draw(self, context):
        """Draw the pie menu."""
        layout = self.layout
        pie = layout.menu_pie()

        pie.menu(
            ASPECT_MT_lens_wide_menu.bl_idname,
            text="Wide Angle Lenses",
            icon="DISCLOSURE_TRI_RIGHT",
        )

        pie.menu(
            ASPECT_MT_lens_tele_menu.bl_idname,
            text="Telephoto Lenses",
            icon="DISCLOSURE_TRI_RIGHT",
        )

        pie.menu(
            ASPECT_MT_cinema_menu.bl_idname,
            text="Cinema Ratios",
            icon="DISCLOSURE_TRI_RIGHT",
        )

        op = pie.operator("aspect.set_lens", text="50mm - Normal")
        op.focal_length = 50

        pie.menu(
            ASPECT_MT_photo_menu.bl_idname,
            text="Photo Ratios",
            icon="DISCLOSURE_TRI_RIGHT",
        )

        pie.menu(
            ASPECT_MT_social_menu.bl_idname,
            text="Social Media Ratios",
            icon="DISCLOSURE_TRI_RIGHT",
        )


def register():
    """Register menus."""


def unregister():
    """Unregister menus."""
