# Kona integration

This fork starts at Paseo `v0.11.2`, commit
`75953250959979b8f088bbca8dbd6ee61d0151b1`. The `kona` branch carries the theme,
Kona launcher patch, and repository presentation. Keep upstream updates explicit:
fetch upstream, review its changes, then merge the chosen release into `kona`.
Retain upstream copyrights, licenses, and release history.

## Theme

Follow [the theme instructions](theme/README.md). The plugin uses Paseo's
supported API and can be installed into an existing Paseo 0.11.2 app.

## Pin in Kona Desktop

Create a working `Paseo.desktop` entry with `StartupWMClass=Paseo` before pinning.
Its `Exec` must point to your installed Paseo launcher. See the
[desktop-entry template](integration/Paseo.desktop.example); replace the absolute
paths with your installation paths and validate it with `desktop-file-validate`.

The patch adds Paseo to the original five pinned apps and derives the grid limit
from the preferred list. Apply it from a checkout of
[Kona Desktop](https://github.com/Denoax/konata-hyprland-dotfiles):

```sh
git apply --check /path/to/paseo-kona/kona/integration/pin-paseo.patch
git apply /path/to/paseo-kona/kona/integration/pin-paseo.patch
```

If your launcher has been customized, edit its `preferredAppNames` to include
`"paseo"`, and replace the two fixed pin limits with `preferredAppNames.length`.
Reload the Kona sidebar afterward. A running app is focused on click; a stopped
app is launched through its desktop entry. Existing pins are retained.

## Existing conversations

Paseo's native provider import handles existing Codex sessions. Preserve your
Codex home and backups, keep the working directory consistent, and close the
current writer before importing a session. Active-writer conflicts require a
handoff; this theme performs no chat migration or lock recovery.

Use `paseo agent import --help` for the installed version's import options.
See [upstream provider documentation](../docs/providers.md) for the provider
boundary. No transcripts, credentials, or local daemon state belong in Git.

## Validation boundary

The included dark palette and launcher integration were rendered on Arch Linux
with Wayland/Hyprland and Paseo 0.11.2. Generation and plugin type checks are
covered locally. [Showcase sources](../showcase/kona/README.md) distinguish real
screenshots from banner compositions. There is no separately packaged Kona app
release yet. Full upstream mobile/desktop test suites were not rerun for this
theme and documentation change.
