# The Record — Indiana Sixth District

A sourced accountability archive for Indiana's Sixth Congressional District.

## Current release

The current layer is checked through **July 18, 2026** and lives at [`current/in6/index.html`](current/in6/index.html). It adds four source-bound records covering House roll calls, Appropriations authority and project requests, and the 2026 general-election field.

The legacy single-file archive remains preserved under `archive/` when this overlay is applied. The current layer does not claim to independently revalidate every historical entry.

## Apply the overlay

Run:

```bash
bash apply_overlay.sh /path/to/cloned/the-record-in6
```

The script backs up the existing root `index.html`, installs the current site, and then validates the result.
