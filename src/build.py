#!/usr/bin/env python3
"""Inline the brand assets into the prototype template and write the single-file artifact."""
import base64, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "src" / "index.src.html").read_text(encoding="utf-8")


def uri(name, mime):
    data = (root / "assets" / name).read_bytes()
    return f"data:{mime};base64," + base64.b64encode(data).decode()


src = src.replace("__LOGO_GREEN__", uri("logo-green.png", "image/png"))
src = src.replace("__LOGO_WHITE__", uri("logo-white.png", "image/png"))
src = src.replace("__LONDON__", uri("london.jpg", "image/jpeg"))
src = src.replace("__HOTELT__", uri("hotel-thumb.jpg", "image/jpeg"))
src = src.replace("__HOTEL__", uri("hotel.jpg", "image/jpeg"))

out = root / "TravelTank-WhatsApp-Prototype.html"
out.write_text(src, encoding="utf-8")
print(out, round(out.stat().st_size / 1024), "kB")

# Stand-alone page: only the typed-conversation path of touchpoint 2, for sharing with stakeholders.
solo = src.replace("var SOLO=false;", "var SOLO=true;", 1)
solo = solo.replace("<title>TravelTank on WhatsApp</title>", "<title>WhatsApp Trip Ideas</title>", 1)
out2 = root / "TravelTank-WhatsApp-Typed-Conversation.html"
out2.write_text(solo, encoding="utf-8")
print(out2, round(out2.stat().st_size / 1024), "kB")
