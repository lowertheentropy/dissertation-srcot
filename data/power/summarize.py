"""Reproduce the battery-power measurements reported in Chapter 6, Table 6.1."""

import csv
from decimal import Decimal
from pathlib import Path


def summarize(path):
    with path.open(newline="", encoding="utf-8") as source:
        samples = list(csv.DictReader(source))

    watts = []
    for row in samples:
        current_ma = int(row["amperage_mA"])
        if current_ma >= 2**63:
            current_ma -= 2**64
        watts.append(Decimal(row["voltage_mV"]) * current_ma / 1_000_000)

    duration = Decimal(samples[-1]["ts_epoch"]) - Decimal(samples[0]["ts_epoch"])
    return len(samples), duration, sum(watts) / len(watts), min(watts)


if __name__ == "__main__":
    print("run,samples,duration_s,mean_battery_W,min_battery_W")
    for path in sorted(Path(__file__).parent.glob("power_*.csv")):
        count, duration, mean, minimum = summarize(path)
        print(f"{path.stem},{count},{duration:.3f},{mean:.2f},{minimum:.2f}")
