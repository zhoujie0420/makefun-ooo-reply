import pathlib

TEXT = "Out until Monday. I've left a smaller model in charge: it is cheerful, confident, and has already approved your budget twice."

out = pathlib.Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(TEXT, encoding="utf-8")
