# 📦 lost-package-bot

A poetic bot that posts melancholic, surreal shipping updates about lost packages to Tumblr. Built using Google Gemini and Tumblr API, with graceful fallbacks to hand-crafted poems when the API fails.

> 🌐 Follow the bot on Tumblr: [https://www.tumblr.com/thelostpackage-bot](https://www.tumblr.com/thelostpackage-bot)

## ✨ What It Does

Each time the bot runs (e.g., on a GitHub Action trigger), it:

- Randomly selects a fictional package status (like "lost in a sorting facility" or "mistakenly marked as delivered")
- Asks Google Gemini to generate a short wistful poem about it
- Posts that poem to a Tumblr blog
- Falls back to a curated set of poetic messages if the API fails

## 🛠 Tech Stack

- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [pytumblr](https://github.com/tumblr/pytumblr)
- GitHub Actions (for automation)
- Tumblr API

## 🔐 Secrets Used

All sensitive credentials are stored securely as GitHub Secrets:

- `GEMINI_API_KEY` – Gemini API Key
- `TUMBLR_CONSUMER_KEY` – Tumblr App Consumer Key
- `TUMBLR_CONSUMER_SECRET` – Tumblr App Consumer Secret
- `TUMBLR_OAUTH_TOKEN` – Tumblr OAuth Token
- `TUMBLR_OAUTH_SECRET` – Tumblr OAuth Secret
- `TUMBLR_BLOG_NAME` – Your blog’s name (e.g., `my-blog.tumblr.com`)

## 📄 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

To run manually:

```bash
python bot.py
```

Or trigger it through GitHub Actions if you've set up a workflow.

## 🏷 Suggested Tumblr Tags

Posts are auto-tagged with:

```
lost package, shipping update, bot, the-lost-package-tracker, poetry bot, melancholy, postal limbo, ai generated, surrealism
```
