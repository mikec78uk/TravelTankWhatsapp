# TravelTank on WhatsApp

A clickable concept prototype showing eleven ways WhatsApp could fit into the TravelTank journey, from the homepage to refunds. Each touchpoint pairs a TravelTank screen with the WhatsApp conversation it triggers, with notes for design, the business and the build.

## View it

Open `TravelTank-WhatsApp-Prototype.html` in a browser. It is a single self-contained file (images are embedded, fonts load from Google Fonts). Use the arrow keys or the Next and Back buttons to step through each touchpoint.

If you open it straight from disk and it looks unstyled, serve it instead:

```bash
python3 -m http.server 8000
```

then visit `http://localhost:8000/TravelTank-WhatsApp-Prototype.html`.

## Touchpoints

1. Homepage: help, refund status and weekly fares
2. Trip ideas on WhatsApp, then a link to traveller details (tap the questions, or type in your own words, with a handover to a Shark or a call when the assistant is unsure)
3. Ask a Shark about a hotel, with the details attached
4. Track the price, or share the trip
5. Opt in at checkout
6. Let each traveller add their own details
7. A 72-hour hold with reminders
8. Bank transfer, with proof of payment in the chat
9. Tickets, and a Shark on tap
10. Pre-trip care and notification settings
11. Cancel, change and refund tracker

## Developer specs

The `docs/` folder holds draft interaction specs for developers, starting with one fully written flow (hold reminders), a template catalogue, an event map and example payloads. Start at [docs/README.md](docs/README.md).

## Rebuilding

The page is built from `src/index.src.html` by `src/build.py`, which inlines the images in `assets/`.

```bash
python3 src/build.py
```

## Notes

- All screens are illustrative concepts based on the current TravelTank site. Names, prices, times and service promises are examples.
- WhatsApp message categories, pricing and policies change. Confirm them with Meta or the chosen provider before launch.
- WhatsApp is a trademark of Meta. This prototype is not affiliated with it.
