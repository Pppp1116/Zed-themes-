# LumenFold — Zed Theme Pack

A curated set of **dark** Zed themes designed for long coding sessions (OLED-friendly / low-glare).

## Previews

| Theme | File | Preview |
|---|---|---|
| NightKerning | `themes/lumenfold-nightkerning.json` | ![NightKerning](screenshots/nightkerning.png) |
| Convergence | `themes/lumenfold-convergence.json` | ![Convergence](screenshots/convergence.png) |
| EmberKerning | `themes/lumenfold-emberkerning.json` | ![EmberKerning](screenshots/emberkerning.png) |
| VioletKerning | `themes/lumenfold-violetkerning.json` | ![VioletKerning](screenshots/violetkerning.png) |
| OpticNeutral | `themes/lumenfold-opticneutral.json` | ![OpticNeutral](screenshots/opticneutral.png) |

### Screenshot note

> **Important:** The blue circular shape visible in some screenshots is a **screenshot artifact only**.  
> It **does not appear in the theme**, **does not ship with LumenFold**, and **will not be visible in Zed during normal use**.

### Experimental

| Theme | File | Preview |
|---|---|---|
| GhostTrial | `themes/experimental/lumenfold-ghosttrial.json` | ![GhostTrial](screenshots/ghosttrial.png) |
| Flawless1 | `themes/experimental/flawless1.json` | ![Flawless1](screenshots/flawless1.png) |

## Install (Local Themes)

Put any theme JSON file into your Zed themes directory:

- **macOS / Linux:** `~/.config/zed/themes/`
- **Windows:** `%USERPROFILE%\AppData\Roaming\Zed\themes\`

Then restart Zed and pick the theme in the Theme Selector.

### Quick install (Linux/macOS)
```bash
bash scripts/install.sh
```

### Quick install (Windows PowerShell)
```powershell
powershell -ExecutionPolicy Bypass -File scripts/install.ps1
```

## Notes

- Theme payloads (colors) are intentionally kept stable. Changes in this repo should be limited to packaging, naming, documentation, and screenshots unless explicitly requested.

## Repository layout

- `themes/` — primary theme files
- `themes/experimental/` — drafts / A-B variants
- `screenshots/` — reference screenshots
- `scripts/` — install helpers

## License

MIT — see `LICENSE`.
