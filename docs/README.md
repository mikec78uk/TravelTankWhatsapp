# WhatsApp interaction specs

Status: **draft for review with the tech partner**. One flow is written in full (hold reminders) as a model. The other nine follow the same structure once this one is agreed.

These documents describe what the system must do. The clickable prototype shows what it looks like.

## How the docs are organised

| Path | What it holds |
|---|---|
| `flows/` | One spec per touchpoint, all with the same headings (see below) |
| `templates/templates.yaml` | Every pre-approved message template, in a machine-readable form |
| `events.md` | The site and back-office events that trigger messages, and which template each sends |
| `payloads/` | Example JSON for sends and webhooks, one file per message type |

Flows written so far:

- [07 Hold reminders](flows/07-hold-reminders.md)

## Headings every flow spec uses

1. **Summary**: one paragraph, plus the prototype scenario it matches.
2. **Trigger**: the event that starts it.
3. **Preconditions**: consent, data and window state that must be true.
4. **Sequence**: a diagram of who does what, in order.
5. **Messages**: every template and session message, with variables and buttons.
6. **Customer replies**: what each button tap or free-text reply does.
7. **Scheduling and idempotency**: when messages fire, and how duplicates are prevented.
8. **Failure handling**: what happens when sending or delivery fails.
9. **Data and consent**: what is stored.
10. **Metrics**: what to log so the owner can measure it.
11. **Acceptance tests**: given, when, then.
12. **Open questions**: decisions still needed, with an owner.

## Conventions

- **Names.** Templates are `purpose_detail_v{n}` in lower case, for example `hold_created_v1`. Changing the wording or variables means a new version, because approved templates cannot be edited in place.
- **Button payloads.** `ACTION:BOOKING_REF`, upper case action, for example `HOLD_PAY_CARD:TT7K2QPD`. Maximum 256 characters.
- **Phone numbers.** Stored and sent as E.164 digits without the plus sign, for example `2348012345678`.
- **Times.** Stored in UTC, shown to customers in Africa/Lagos (WAT), formatted `Mon 24 Aug, 14:30`.
- **Money.** Shown as `₦5,673,507` with thousands separators and no decimals unless the amount has kobo.
- **Marking uncertainty.** `[confirm]` marks anything that must be checked against current Meta documentation or with TravelTank before build.

## Sources and limits

- Template categories, rules and pricing change. Check the current WhatsApp Business Platform documentation and the chosen provider's rate card before relying on anything marked `[confirm]`.
- Example values (names, references, prices) are illustrative and match the prototype.
