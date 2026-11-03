"""Reassemble the unmodified benchmark ZIP and verify its published SHA-256."""
from pathlib import Path
import hashlib
import os
import tempfile

BASE = Path(__file__).resolve().parent
DEST = BASE / "model_comparison_v3_complete.zip"
EXPECTED = "75546e9d8e307b64191bd7dad27ccfabf76b082fda7a1c6211620b906c7a88a5"

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    if DEST.exists():
        if digest(DEST) != EXPECTED:
            raise SystemExit(f"Existing file has a different checksum; not overwriting: {DEST}")
        print(f"Already verified: {DEST.name}\nSHA-256: {EXPECTED}")
        return
    parts = [BASE / "archive-parts" / f"{DEST.name}.part{i:02}" for i in (1, 2)]
    for part in parts:
        if not part.is_file():
            raise SystemExit(f"Missing archive part: {part}")
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=BASE, prefix=DEST.name + ".", suffix=".tmp", delete=False) as output:
            temporary = Path(output.name)
            for part in parts:
                with part.open("rb") as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                        output.write(chunk)
        if temporary.stat().st_size != 14504294 or digest(temporary) != EXPECTED:
            raise SystemExit("Archive verification failed; original ZIP was not created.")
        if DEST.exists():
            raise SystemExit("Destination appeared during reconstruction; not overwriting it.")
        os.replace(temporary, DEST)
        temporary = None
        print(f"Restored and verified: {DEST.name}\nSHA-256: {EXPECTED}")
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
