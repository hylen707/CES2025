#!/usr/bin/env python3
"""Extract text in presentation order; no slide-number inference from filenames."""
import argparse
import hashlib
import json
import posixpath
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

NS = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}


def extract(path):
    raw = Path(path).read_bytes()
    with zipfile.ZipFile(path) as package:
        relationships = ET.fromstring(package.read("ppt/_rels/presentation.xml.rels"))
        targets = {r.attrib["Id"]: r.attrib["Target"] for r in relationships}
        presentation = ET.fromstring(package.read("ppt/presentation.xml"))
        slides = []
        for number, entry in enumerate(presentation.findall("p:sldIdLst/p:sldId", NS), 1):
            rel_id = entry.attrib[f"{{{NS['r']}}}id"]
            target = targets[rel_id]
            part = target.lstrip("/") if target.startswith("/") else posixpath.normpath(posixpath.join("ppt", target))
            if not part.startswith("ppt/slides/"):
                raise ValueError(f"Unexpected slide target: {part}")
            slide = ET.fromstring(package.read(part))
            slides.append({"slide_number": number, "presentation_id": entry.attrib["id"],
                           "relationship_id": rel_id, "part": part,
                           "text": [t.text or "" for t in slide.findall(".//a:t", NS)]})
    return {"sha256": hashlib.sha256(raw).hexdigest(),
            "order_verified_from": "ppt/presentation.xml and ppt/_rels/presentation.xml.rels",
            "scope": "Text runs only; visual layout, images, speaker notes, authorship and attendance not verified.",
            "slides": slides}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("presentation", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    result = extract(args.presentation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Extracted {len(result['slides'])} slides; SHA-256 {result['sha256']}")


if __name__ == "__main__":
    main()
