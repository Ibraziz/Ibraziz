# Maintain your GitHub profile

Your profile README is published from [Ibraziz/Ibraziz](https://github.com/Ibraziz/Ibraziz) and appears on [your GitHub profile](https://github.com/Ibraziz).

## Edit the content and colors

- Edit your introduction and contact links in `README.md`.
- Edit `BADGE_ROWS` in `tools/generate_assets.py` to change the tools, categories, or badge colors. Keep the `tools:start` and `tools:end` markers in the README; the script updates the table between them.
- Edit `PALETTES` and the banner functions in that script to change the light and dark banners.

Regenerate the artwork and tool table:

```powershell
python tools/generate_assets.py
```

The banner and colored badges are local SVG files. GitHub displays them without an API key, image-hosting account, or scheduled workflow.

## Preview changes

The local preview is generated from the README. It approximates GitHub's appearance; check your published profile after uploading changes.

```powershell
python -m pip install -r requirements-preview.txt
python tools/build_preview.py
```

Open `preview/index.html` and use the appearance selector to check the light and dark themes. Badge images wrap within the table on smaller screens.

## Publish updates

From this folder, commit the files you changed and push to the existing repository:

```powershell
git add README.md assets tools SETUP.md
git commit -m "Update profile tools and styling"
git push
```

Keep `README.md` at the repository root and preserve the paths under `assets/`. The generated preview and local dependencies are ignored by Git.

## Design and content

The tool table uses colorful gradient badges inspired by your supplied screenshot. Its contents come from your CV and project work. AWS is explicitly labeled **Fundamentals**. The detailed project descriptions and research metrics have been removed from the profile.
