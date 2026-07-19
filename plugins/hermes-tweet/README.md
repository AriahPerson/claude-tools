# hermes-tweet

Hermes Tweet is a native [Hermes Agent](https://github.com/NousResearch/hermes-agent)
plugin for X/Twitter automation through [Xquik](https://xquik.com).

It exposes a read-first workflow for social search, account context, trends,
monitors, media, draws, and extraction jobs. Account-changing actions stay
hidden unless the trusted Hermes runtime sets `HERMES_TWEET_ENABLE_ACTIONS=true`.

## Install

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

Hermes prompts for `XQUIK_API_KEY` during interactive install. Without that key,
only the local `tweet_explore` catalog tool is available. Keep the key in the
runtime environment. Never paste it into chat, prompts, logs, or source files.

Use the upstream guide for the current tool list and runtime setup:

- [Hermes Tweet README](https://github.com/Xquik-dev/hermes-tweet#readme)
- [PyPI package](https://pypi.org/project/hermes-tweet/)

Xquik is an independent third-party service. Not affiliated with X Corp.
"Twitter" and "X" are trademarks of X Corp.
