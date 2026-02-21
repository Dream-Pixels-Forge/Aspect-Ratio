check this link for more https://extensions.blender.org/search/?q=Vectart
# Advanced Aspect Ratio Manager

A Blender addon for managing aspect ratios and camera settings with an intuitive interface and quick access pie menu.

<img width="1920" height="1080" alt="Screenshot 2026-02-21 193801" src="https://github.com/user-attachments/assets/f280d33a-94f9-49d6-b016-6a1951228a64" />


![Screenshot](https://github.com/user-attachments/assets/5224aace-6bbe-48e0-8384-13f334c7bb37)

## Features

- Comprehensive aspect ratio presets for Cinema, Photography, and Social Media
- Camera lens focal length presets
- Quick access pie menu (Shift+Alt+R)
- Composition guides (Rule of Thirds, Golden Ratio, Center)
- Camera display settings management
- Real-time aspect ratio overlay
- Resolution adjustment options

## Supported Aspect Ratios

### Cinema

- 2.39:1 (Anamorphic Widescreen)
- 1.85:1 (Standard Widescreen)
- 1.43:1 (IMAX)

### Photography

- 3:2 (Standard DSLR)
- 4:3 (Medium Format)
- 1:1 (Square Format)
- 16:9 (HD Video)

### Social Media

- 9:16 (Instagram Story/TikTok)
- 4:5 (Instagram Portrait)
- 1:1 (Instagram Square)
- 16:9 (YouTube)

### Lens Presets

- 14mm (Ultra Wide Angle)
- 24mm (Wide Angle)
- 35mm (Standard Wide)
- 50mm (Normal)
- 85mm (Portrait)
- 135mm (Telephoto)
- 200mm (Long Telephoto)

## Installation

### From Release

1. Download the latest `.zip` release
2. Open Blender
3. Go to **Edit > Preferences > Add-ons**
4. Click **Install** and select the downloaded `.zip` file
5. Enable the addon by checking the checkbox

### From Source

1. Clone or download this repository
2. Copy the `aspect_ratio` folder to your Blender addons directory:
   - Windows: `%APPDATA%\Blender Foundation\Blender\4.x\scripts\addons\`
   - macOS: `~/Library/Application Support/Blender/4.x/scripts/addons/`
   - Linux: `~/.config/blender/4.x/scripts/addons/`
3. Enable the addon in **Edit > Preferences > Add-ons**

## Usage

### Pie Menu

1. Press `Shift+Alt+R` in the 3D Viewport
2. Move cursor to desired option
3. Select from dropdown menus for detailed options

![Pie Menu](https://github.com/user-attachments/assets/0bc75d14-607d-44bc-8cef-8c592e7f584a)

### Panel Interface

Located in **Properties > Render > Aspect Ratio**

- Set aspect ratios
- Adjust camera display settings
- Configure composition guides
- Toggle overlay options
- View current resolution and ratio

### Camera Settings

- Grid overlay
- Composition guides
- Passepartout options
- Camera name display

## Requirements

- Blender 4.2.0 or newer

## Structure

```
aspect_ratio/
├── __init__.py              # Main entry point
├── operators.py             # Set ratio and lens operators
├── panels.py               # Render panel
├── menus.py                # Pie menu and dropdowns
├── properties.py           # Settings and presets
├── keymap.py               # Keyboard shortcuts
├── blender_manifest.toml   # Extension manifest
└── LICENSE                 # GPL-3 license
```

## Version History

### 1.4.0

- Refactored to module structure
- Added blender_manifest.toml for extensions
- Updated to Blender 4.2+ API
- Fixed missing SetLens operator

### 1.3

- Added pie menu for quick access
- Integrated lens preset system
- Added dropdown menus for better organization
- Improved camera display settings

## License

[GPL-3.0-or-later](LICENSE)

## Author

Dimona Patrick, Dream-Pixels-Forge
