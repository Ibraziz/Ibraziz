# Put this README on your GitHub profile

This folder contains your profile README and its artwork. GitHub displays it above your pinned repositories when it lives in the public repository **Ibraziz/Ibraziz**.

Your local folder can keep the name `github-readme`; the repository on GitHub must be named `Ibraziz`.

## 1. Preview and review

Open `preview/index.html` in a browser to see a local approximation of the README. Switch your browser or operating system between light and dark appearance to check both versions. The preview is generated from `README.md`; GitHub's own rendering is the final reference.

Review the bio, project descriptions, location, and contact link in `README.md`. The artwork is stored locally in `assets/`, so it needs no image-hosting account, API key, or scheduled workflow.

## 2. Create the profile repository

1. Sign in to [GitHub](https://github.com).
2. Open [New repository](https://github.com/new).
3. Select **Ibraziz** as the owner.
4. Enter **Ibraziz** as the repository name.
5. Choose **Public**.
6. Turn **Add README** on, then select **Create repository**.

If `Ibraziz/Ibraziz` already exists when you do this, open it and continue with the next step.

GitHub's official instructions: [Managing your profile README](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme).

## 3. Upload the files

1. In the repository, choose **Add file → Upload files**.
2. From this local folder, drag **README.md** and the whole **assets** folder into the upload area. Keep the `assets/` folder structure.
3. Enter a commit message such as `Add personal profile README`.
4. Select **Commit changes**.

The required structure is:

```text
Ibraziz/
├── README.md
└── assets/
    ├── hero-dark.svg
    ├── hero-light.svg
    ├── hero-mobile-dark.svg
    ├── hero-mobile-light.svg
    ├── research-dark.svg
    ├── research-light.svg
    ├── research-mobile-dark.svg
    ├── research-mobile-light.svg
    ├── tools-dark.svg
    ├── tools-light.svg
    ├── tools-mobile-dark.svg
    └── tools-mobile-light.svg
```

`SETUP.md`, `tools/`, and `requirements-preview.txt` are optional maintenance files. You can keep them in the repository too. The generated `preview/` folder stays local.

## 4. Check your profile

Open [github.com/Ibraziz](https://github.com/Ibraziz). The README should appear above your pinned repositories. Check the banner, project links, and artwork in both light and dark appearance.

If it does not appear, check that the repository is **public**, its name is exactly **Ibraziz**, and a nonempty **README.md** is at the repository root. If images are missing, confirm the `assets/` folder was uploaded beside `README.md`, with the filenames shown above.

## 5. Complete the sidebar

On your profile, select **Edit profile**. Suggested values:

- **Bio:** AI engineer | LLM applications, agent workflows & multilingual NLP | FineOPUS contributor | MSc AI, University of Jyväskylä
- **Location:** Jyväskylä, Finland
- **Website:** https://www.linkedin.com/in/abdelaziz-ibrahim-740800172/

Use **Customize your pins** to feature DataAnalystAgent, FineOPUS, and Lawgic. FineOPUS and Lawgic are shared projects, so choose them from repositories you contributed to if needed. Your existing pins already include these three projects.

## Optional: publish with Git instead

Use this route instead of the browser upload. Create `Ibraziz/Ibraziz` as an **empty public repository**, with **Add README off**. Then run these commands from PowerShell:

```powershell
Set-Location 'D:\Study\github-readme'
git init -b main
git add README.md assets SETUP.md tools requirements-preview.txt .gitignore .gitattributes
git commit -m "Add personal profile README"
git remote add origin https://github.com/Ibraziz/Ibraziz.git
git push -u origin main
```

Git may ask you to sign in. If you already created the repository with a README, use the browser-upload route above, or clone that repository into a separate folder and copy these files into it before committing. Do not force-push over an existing repository.

## Maintain the design

Edit the prose in `README.md`. To change the banner, colors, metrics, or tool badges, edit `tools/generate_assets.py` and regenerate the artwork:

```powershell
python tools/generate_assets.py
```

That command uses Python's standard library. Publishing and displaying this profile require no Python installation.

To rebuild the optional local preview:

```powershell
python -m pip install -r requirements-preview.txt
python tools/build_preview.py
```

Re-upload the changed README and artwork, or commit and push the changes if you use Git.

## Content choices

The bio follows your existing CV and our previous work together. The technical descriptions were checked against the public [FineOPUS quality-estimation code](https://github.com/MaLA-LM/FineOPUS/tree/main/05_quality_estimation), [DataAnalystAgent](https://github.com/Ibraziz/DataAnalystAgent), and [Lawgic](https://github.com/bikhanal/lawgic). The [research paper](https://arxiv.org/abs/2606.00285) confirms authorship and the nine-evaluator, 41,412-direction benchmark. The 1.14-billion-pair scoring figure is scoped to the completed 421-direction subset described in your CV.

The README identifies your contribution to shared projects, distinguishes Flask from FastAPI, and describes knowledge graphs as an established academic and project foundation. It links to public research and code; it does not link to the private thesis repository.

Inspired by the bio-and-tools structure of [Bishwash Khanal's profile](https://github.com/bikhanal), with original artwork for your profile. This version has no external statistics widgets or visitor counters to maintain.
