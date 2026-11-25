"""Out-of-office reply entry generator."""
import pathlib
import sys

# Entry text
TEXT = "Out until Monday. I've left a smaller model in charge: it is cheerful, confident, and has already approved your budget twice."

def main():
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(TEXT, encoding="utf-8")
    print("Entry written successfully.", file=sys.stderr)

if __name__ == "__main__":
    main()


