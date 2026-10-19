# Google OAuth Branding Site

Static home page, privacy policy, and terms of service for a Google OAuth consent screen, ready for GitHub Pages.

## 1. Fill in your details

Edit `config.json` (app name, your name, contact email, what Google data you access and why), then run:

```
python3 build.py
```

This regenerates `index.html`, `privacy.html`, `terms.html`, and `style.css` in the repo root. Re-run after any change.

Make `DATA_ACCESSED` match the scopes you request under **Data Access** in Google Auth Platform exactly. A mismatch is a common reason verification is rejected.

## 2. Publish on GitHub Pages

1. Create a **public** repo (e.g. `myapp-site`) and push this folder to it.
2. Go to **Settings -> Pages**, choose **Deploy from a branch**, branch `main`, folder `/ (root)`.
3. After about a minute your pages are live:
   - Home page: `https://<username>.github.io/<repo>/`
   - Privacy: `https://<username>.github.io/<repo>/privacy.html`
   - Terms: `https://<username>.github.io/<repo>/terms.html`

## 3. Paste into Google Auth Platform -> Branding

| Field | Value |
|---|---|
| Application home page | the home page URL |
| Application privacy policy link | the privacy URL |
| Application terms of service link | the terms URL |

## Custom domain (needed before publishing to production)

While the app is in **Testing**, a `github.io` URL is fine. For production verification, Google expects a domain you own:

1. Buy a domain and add it under **Settings -> Pages -> Custom domain** (GitHub shows the DNS records to add).
2. Enable **Enforce HTTPS**.
3. Verify the domain in Google Search Console.
4. Add it under **Authorized domains** on the Branding page, and update the three URLs.

## Notes

- Don't upload an app logo until you're ready to publish; it triggers a verification requirement.
- `templates/` holds the source pages; the root `.html` files are generated. Edit templates or `config.json`, not the root files.
- This is general-purpose template text, not legal advice. Have a lawyer review it if your app handles sensitive data.
