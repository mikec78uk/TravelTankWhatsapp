# Event map

Which events in the TravelTank platform cause something to happen on WhatsApp. Status: draft. Only flow 07 rows are filled in. Other flows will add rows.

## Outbound: platform events to messages

| Event | Raised by | Key fields | What happens on WhatsApp | Flow |
|---|---|---|---|---|
| `hold.created` | Booking service | booking_ref, expires_at, customer id | Send `hold_created_v1`. Schedule 24h and 6h reminders. | 07 |
| `hold.reminder_due` (24h) | Scheduler | booking_ref | Re-check the hold. If `placed`, send `hold_reminder_24h_v1`. | 07 |
| `hold.reminder_due` (6h) | Scheduler | booking_ref | Re-check the hold. If `placed`, send `hold_reminder_6h_v1`. | 07 |
| `hold.expired` | Booking service | booking_ref | Send `hold_expired_v1`. Cancel remaining jobs. | 07 |
| `hold.cancelled` | Booking service | booking_ref | Cancel pending jobs. Send nothing. | 07 |
| `payment.confirmed` | Payment or finance service | booking_ref, amount, method | Cancel pending hold jobs. Send `payment_confirmed_v1`. | 07, 08 |
| `customer.opted_in` | Site (checkout or My Account) | customer id, phone, source, wording_version | Store consent. Send `optin_welcome_v1` if it came from checkout. | 05 |
| `customer.opted_out` | Webhook (STOP) or My Account | customer id | Set `opted_out_at`. Cancel all pending jobs. Send one confirmation. | all |

## Inbound: WhatsApp webhooks to actions

| Webhook | Identified by | Action | Flow |
|---|---|---|---|
| Message, type `button` | `button.payload` starts with `HOLD_` | See the customer replies table in the flow spec | 07 |
| Message, type `text` | Any text | Route to agent inbox with booking attached. `STOP` opts out. | all |
| Message, type `image` or `document` | Media | Route to agent inbox. Receipts are handled in flow 08. | 08 |
| Status `sent`, `delivered`, `read` | `statuses[].status` | Update the message record | all |
| Status `failed` | `statuses[].errors` | Apply the failure handling table in the flow spec | all |

## Rules that apply to every event

- Handlers are idempotent. Webhooks and scheduled jobs can both arrive more than once.
- Re-read the current booking and hold state immediately before sending, not when the job was scheduled.
- Acknowledge webhooks with HTTP 200 straight away, then process asynchronously.
- Never send when consent is missing, opted out, or the number is marked unreachable.
