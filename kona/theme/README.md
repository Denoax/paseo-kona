# Kona theme

Install this directory through Paseo's theme plugin API. It contributes one dark
theme and runs no backend entrypoint. Paseo 0.11.2 is the tested host.

```sh
paseo plugin install ./kona/theme
```

Enable plugins in **Settings → Plugins**, then select **Kona** in Appearance.
Use **Noto Sans**, interface size **14**, content **16**, and code size **13** to
match the screenshots. Font preferences are set in Paseo, not by the plugin.

`palette.json` is the bundled Kona dark palette. `index.client.ts` is generated.
To use an installed Kona palette, select Dark on the desktop and refresh:

```sh
python3 kona/theme/tools/sync-theme.py --source "$HOME/.config/kona/theme/current/tokens.json"
paseo plugin reload kona
```

To restore this repository's palette:

```sh
python3 kona/theme/tools/sync-theme.py
paseo plugin reload kona
```

The palette adapts Paseo's shared border/fill and focus/muted-text roles. It
changes colors; animation behavior and the agent engine remain upstream.

Development checks:

```sh
npm --prefix kona/theme ci --legacy-peer-deps
npm --prefix kona/theme run typecheck
python3 kona/theme/tools/sync-theme.py --check
python3 -m unittest discover -s kona/theme/tools -p 'test_*.py'
```
