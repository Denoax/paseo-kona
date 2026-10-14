# Repository artwork and capture sources

The README banner is a documentation composition: original typography, spatial
SVG lines, a localized navy light field, and a crop of the real Paseo editor.
It is not a fabricated interface or an unedited app recording. The static social
preview uses the same typography and palette, with the upstream Paseo mark.

## References

- [Kona Desktop](https://github.com/Denoax/konata-hyprland-dotfiles): inspected its
  current README, wide banner, centered introduction, real screenshots, paired
  galleries, and install/source documentation. Borrow the reading order and
  screenshot-led presentation. No character or wallpaper art is copied.
- [Portfolio](https://github.com/Denoax/portfolio): inspected its README and owned
  showcase captures. Borrow restrained typography, low-brightness local light,
  and spatial line work. The banner geometry is original; no galaxy or intro
  pixels are copied.

## Actual app captures

`sources/workspace-original.png` is a 1440×900 capture of the installed Paseo
0.11.2 Electron renderer, using this fork's actual theme plugin and source file.
The isolated preview daemon/profile registered only this public repository and
an empty local workspace. No agent prompt or private session import was used.
`workspace.webp` is a lossless conversion; `workspace-detail.webp` is its exact
crop `[320, 0, 1440, 680]` for the banner.

`sources/appearance-original.png` is the earlier validated 1440×900 Kona
Appearance capture. Its palette and font settings match the included theme.
`appearance.webp` is a lossless conversion. `launcher.png` crops the genuine
Kona Applications panel to show the Paseo pin; the avatar and other desktop
content are outside the crop. Application icons retain their owners' rights.

The captures establish these states and geometry, not motion smoothness,
physical-display brightness, or human approval.

## Recreate the artwork

Serve the checkout locally and capture `banner.html` after fonts/images load:

- README: `banner.html`, 1600×600, `banner.webp`.
- Social preview: `banner.html?layout=type`, 1280×640, `social-preview.png`.

The font is the portfolio's licensed Inter Medium file, retained with its OFL
notice. The Paseo mark is loaded from the unchanged upstream
`packages/website/public/logo.svg`. `sources.json` records source and output
hashes. Keep source media and notices when regenerating the artwork.

## GitHub social preview

Use `social-preview.png` in **Repository Settings → Social preview → Edit →
Upload an image**. It is 1280×640 and under 1 MB, following
[GitHub's image guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).
Committing the image makes it available; setting the repository preview is a
separate GitHub setting.
