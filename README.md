<p align="center">
  <img src="custom_components/fear_and_greed/brand/icon.png" alt="Fear and Greed Index" width="120" />
</p>

<h1 align="center">Fear and Greed Index</h1>

<p align="center">
  Crypto Fear &amp; Greed Index from alternative.me as two Home Assistant sensors — numeric value and text classification, updated every 30 minutes.
</p>

<p align="center">
  <a href="https://github.com/hacs/integration">
    <img src="https://img.shields.io/badge/HACS-Custom-orange.svg" alt="HACS Custom" />
  </a>
  <a href="https://github.com/macokay/hacs-fear-and-greed/releases">
    <img src="https://img.shields.io/github/v/release/macokay/hacs-fear-and-greed" alt="GitHub release" />
  </a>
  <a href="https://github.com/macokay/hacs-fear-and-greed/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License" />
  </a>
</p>

<p align="center">
  <a href="https://www.buymeacoffee.com/macokay">
    <img src="https://img.shields.io/badge/Buy%20Me%20A%20Coffee-%23FFDD00.svg?logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee" />
  </a>
</p>

---

## Features

- Numeric index sensor (0–100)
- Text classification sensor (Extreme Fear / Fear / Neutral / Greed / Extreme Greed)
- Single API call shared between both sensors
- No API key required
- GUI setup — no YAML needed

---

## Requirements

| Requirement | Version / Details |
|---|---|
| Home Assistant | 2023.1 or newer |
| alternative.me FNG API | Free, no API key required |

---

## Installation

### Automatic — via HACS

1. Open **HACS** in Home Assistant.
2. Go to **Integrations** → three-dot menu (⋮) → **Custom repositories**.
3. Add `https://github.com/macokay/hacs-fear-and-greed` as **Integration**.
4. Search for **Fear and Greed Index** and click **Download**.
5. Restart Home Assistant.

### Manual

1. Download the latest release from [GitHub Releases](https://github.com/macokay/hacs-fear-and-greed/releases).
2. Copy the `custom_components/fear_and_greed` folder to your `config/custom_components/` directory.
3. Restart Home Assistant.

---

## Configuration

1. Go to **Settings → Devices & Services → Add Integration**.
2. Search for **Fear and Greed Index**.
3. Click **Submit** — no further input required.

---

## Data

### Entities

| Entity | Type | Description |
|---|---|---|
| `sensor.fear_and_greed_index` | `int` | Numeric index value (0–100) |
| `sensor.fear_and_greed_classification` | `string` | Extreme Fear / Fear / Neutral / Greed / Extreme Greed |

### Update interval

Data is fetched every 30 minutes.

---

## Updating

**Via HACS:** HACS will notify you when an update is available. Click **Update** on the integration card.

**Manual:** Replace the `custom_components/fear_and_greed` folder with the new version and restart Home Assistant.

---

## Known Limitations

- Data is sourced from the [alternative.me FNG API](https://api.alternative.me/fng/) — availability depends on the upstream service

---

## Credits

- [alternative.me](https://alternative.me/crypto/fear-and-greed-index/) — Crypto Fear and Greed Index data

---

## License

&copy; 2026 Mac O Kay. Licensed under the MIT License. See [LICENSE](LICENSE) for details.
