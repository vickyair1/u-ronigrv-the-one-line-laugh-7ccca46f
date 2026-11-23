"""The One-Line Laugh — one funny line, written to /output/entry.txt."""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = "My smart fridge emailed me a diet plan, then ordered pizza behind my back and blamed the Wi-Fi."


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
