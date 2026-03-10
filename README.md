# Fear and Greed Index — Home Assistant Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

Custom integration for Home Assistant that pulls the [Crypto Fear and Greed Index](https://alternative.me/crypto/fear-and-greed-index/) from alternative.me and exposes it as two sensors.

---

## Sensors

| Entity | Type | Description |
|--------|------|-------------|
| `sensor.fear_and_greed_index` | `int` (0–100) | Numeric index value |
| `sensor.fear_and_greed_classification` | `string` | Text label: Extreme Fear / Fear / Neutral / Greed / Extreme Greed |

Both sensors share a single API call and update every 30 minutes.

---

## Installation via HACS

1. In Home Assistant, go to **HACS → Integrations → ⋮ → Custom repositories**
2. Add `https://github.com/macokay/hacs-fear-and-greed` as category **Integration**
3. Find **Fear and Greed Index** in HACS and click **Download**
4. Restart Home Assistant

### Manual installation

Copy the `custom_components/fear_and_greed` folder into your `config/custom_components/` directory and restart.

---

## Configuration

No YAML required. After installation:

1. Go to **Settings → Devices & Services → Add Integration**
2. Search for **Fear and Greed Index**
3. Click **Submit** — that's it

---

## Data source

Data is fetched from the free [alternative.me FNG API](https://api.alternative.me/fng/) — no API key required.

---

## License

© 2026 Mac O Kay
Free to use and modify for personal, non-commercial use.
Credit appreciated if you share or build upon this work.
Commercial use is not permitted.
