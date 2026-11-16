from pathlib import Path

print("name           suffix")
for name in ["config.py", "settings.json", ".env", "id_demo"]:
    print(f"{name:<14} {Path(name).suffix!r}")
