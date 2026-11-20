# Chapter 6 · Measuring local SRCoT power consumption

These two CSV files contain hardware readings collected on 17 January 2026 while running SRCoT locally on an Apple M4-family MacBook Pro with 128 GB of unified memory. LM Studio 0.3.39 served GPT-OSS-120b. The recording windows include the idle tail after inference. Both CSVs preserve the original readings and column names.

| Trace | Samples | Elapsed time, s | Mean battery power, W | Minimum battery power, W |
| --- | ---: | ---: | ---: | ---: |
| [Run 1](power_20260117_150126.csv) | 900 | 460.394 | −59.72 | −112.13 |
| [Run 2](power_20260117_151121.csv) | 2,433 | 1,248.062 | −38.06 | −136.47 |

## Reproduce the battery values in Table 6.1

From the repository root, run the following command with Python 3. It uses the standard library.

```sh
python3 data/power/summarize.py
```

The recording stores negative current as an unsigned 64-bit integer. Parse `amperage_mA` as an exact integer and subtract 2⁶⁴ when the value is at least 2⁶³. Battery power in watts equals the signed current in milliamperes multiplied by voltage in millivolts and divided by 1,000,000. Negative values indicate discharge. The mean gives each sample equal weight. Converting the raw current to floating point first loses precision.

## CSV columns

| Field | Meaning |
| --- | --- |
| `ts_iso`, `ts_epoch` | Local timestamp and Unix timestamp in seconds |
| `cpu_w`, `gpu_w`, `ane_w`, `dram_w`, `package_w` | Logged component power fields in watts. Empty cells denote missing readings. |
| `batt_pct`, `charging_pmset` | Battery charge percentage and recorded charging status |
| `batt_w_est` | Historical logger estimate. Use current and voltage to reproduce the dissertation's battery results. |
| `voltage_mV`, `amperage_mA` | Battery voltage and raw current used in the calculation above |

## File checksums

| File | SHA-256 |
| --- | --- |
| `power_20260117_150126.csv` | `8e3f443d6e5a5e19ec0de6a2e516db03e542e5626ceef2fbdda25a41f17cb9ef` |
| `power_20260117_151121.csv` | `6970fa5e792337da82119608f0665a27efd8bd052997a4bdfdc0e9d20911fa06` |
