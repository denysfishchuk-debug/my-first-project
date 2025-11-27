# n8n Workflow Visual Setup Guide
## Mit Screenshots-Beschreibungen für jeden Node

---

## 🎯 WORKFLOW ÜBERSICHT

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    AEROWISCH AI - EMAIL SUPPORT AUTOMATION                 │
│                         (n8n Workflow Diagram)                             │
└────────────────────────────────────────────────────────────────────────────┘

                           START
                             │
                             ▼
        ┌────────────────────────────────────────┐
        │  NODE 1: Email Trigger (IMAP)          │
        │  ├─ Type: Trigger                      │
        │  ├─ Checks: Every 1 minute             │
        │  ├─ Mailbox: INBOX                     │
        │  ├─ Filter: Only unread                │
        │  └─ Output: email metadata             │
        └────────────┬─────────────────────────┘
                     │
                     ▼
        ┌────────────────────────────────────────┐
        │  NODE 2: Prepare Content (Set)         │
        │  ├─ Combines: subject + body           │
        │  ├─ Extracts: sender info              │
        │  ├─ Cleans: subject line               │
        │  └─ Output: enriched data              │
        └────────────┬─────────────────────────┘
                     │
                     ▼
        ┌────────────────────────────────────────┐
        │  NODE 3: IF - Price Inquiry?           │
        │  ├─ Check: Regex pattern               │
        │  ├─ Keywords: preis|kosten|euro|...   │
        │  └─ Routes:                            │
        │     ├─ TRUE  → Price Response          │
        │     └─ FALSE → Next IF                 │
        └────┬────────────────────────────────┬─┘
             │                                │
        TRUE │                            FALSE│
             ▼                                │
        ┌─────────────────┐                  │
        │ Send Email:     │                  ▼
        │ Price List      │      ┌────────────────────────────────────────┐
        │ Template        │      │  NODE 4: IF - Defect/Damage?           │
        │ ├─ To:          │      │  ├─ Check: Regex pattern               │
        │ │ {{sender}}    │      │  ├─ Keywords: defekt|schaden|kaputt   │
        │ ├─ Subject:     │      │  └─ Routes:                            │
        │ │ Preis Info    │      │     ├─ TRUE  → Create Ticket+Email    │
        │ └─ Body:        │      │     └─ FALSE → Generic Response       │
        │   Price Tmpl.   │      └─┬───────────────────────────────────┬─┘
        └────────┬────────┘       │                                   │
                 │                │                                   │
        Mark Read│              TRUE                              FALSE
                 │               │                                   │
                 │               ▼                                   ▼
                 │      ┌──────────────────┐              ┌──────────────────┐
                 │      │ Create Ticket:   │              │ Send Email:      │
                 │      │ Freshdesk        │              │ Generic Response │
                 │      ├─ Title: {{..}}   │              │                  │
                 │      ├─ Desc: {{text}}  │              ├─ To: {{sender}}  │
                 │      └─ Priority: High  │              ├─ Template:       │
                 │                         │              │ Generic          │
                 │      ┌──────────────────┐              └──────────────────┘
                 │      │ Send Email:      │
                 │      │ Defect Response  │
                 │      ├─ To: {{sender}}  │
                 │      ├─ Template:       │
                 │      │ Defect           │
                 │      └─ Include Ticket  │
                 │      Mark Read          │
                 │                    Mark Read
                 │      (All paths    │
                 │       converge)    │
                 │          │          │
                 └─────────┬──────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ NODE 9: Mark Email   │
                │ as Read + Log        │
                │ ├─ Timestamp         │
                │ ├─ Category          │
                │ └─ Success           │
                └──────────┬───────────┘
                           │
                           ▼
                        SUCCESS ✓
                    (Workflow Complete)
```

---

## 🔧 NODE-BY-NODE SETUP GUIDE

### NODE 1: EMAIL TRIGGER (IMAP)

**Position in Workflow:** Start Node (Leftmost)

**Visual Layout:**
```
┌──────────────────────────────────┐
│  📧 Email Trigger (IMAP)         │
├──────────────────────────────────┤
│ Trigger Type:  Every interval    │
│ Interval:      1 minute          │
│ Protocol:      IMAP (SSL/TLS)    │
│ Host:          imap.gmail.com    │
│ Port:          993               │
│ Credentials:   [Gmail IMAP]      │
│ Mailbox:       INBOX             │
│ Filter:        Unread only ✓     │
│ Mark as read:  After processing  │
└──────────────────────────────────┘
```

**Configuration Steps:**
1. Click n8n "+" button → Search "Email Trigger"
2. Select "Email Trigger (IMAP)"
3. Create NEW credentials:
   - Click "Create New" in Credentials dropdown
   - Protocol: IMAP
   - Host: imap.gmail.com
   - Port: 993
   - User: support@aerowisch.de
   - Password: [App-Password from Google]
   - Encryption: SSL/TLS
   - Test: Should show ✓
4. Back in trigger node:
   - Mailbox: INBOX
   - Poll Times: Set "1 minute"
   - Options → Check "Download Attachments" (optional)
5. Save node

**Output (Example):**
```json
{
  "messageId": "<abc123@example.com>",
  "from": {
    "name": "Max Mustermann",
    "address": "max@example.com"
  },
  "to": [{"address": "support@aerowisch.de"}],
  "subject": "Frage zum Preis des AeroWisch AI",
  "text": "Hallo, wie viel kostet der AeroWisch AI?",
  "html": "<p>Hallo, wie viel kostet der AeroWisch AI?</p>",
  "date": "2025-11-27T12:30:00Z"
}
```

---

### NODE 2: PREPARE CONTENT (SET)

**Position in Workflow:** Right of Node 1

**Visual Layout:**
```
┌──────────────────────────────────┐
│  ⚙️ Prepare Content (Set Node)   │
├──────────────────────────────────┤
│ Mode: Manual mode (Edit fields)  │
│                                  │
│ New Fields:                      │
│  1. content_combined (String)    │
│     Value: {{subject}} {{text}}  │
│                                  │
│  2. sender_email (String)        │
│     Value: {{from.address}}      │
│                                  │
│  3. sender_name (String)         │
│     Value: {{from.name||'Kunde'}}│
│                                  │
│  4. email_subject_sanitized      │
│     Value: {{subject.replace...}}│
└──────────────────────────────────┘
```

**Configuration Steps:**
1. Click "+" → Search "Set"
2. Select "Set" node
3. Mode: "Manual mode (edit fields)"
4. Click "Add Field" four times:

**Field 1:**
- Name: content_combined
- Type: String (Expression)
- Value: `{{ $json.subject }} {{ $json.text }}`

**Field 2:**
- Name: sender_email
- Type: String (Expression)
- Value: `{{ $json.from.address }}`

**Field 3:**
- Name: sender_name
- Type: String (Expression)
- Value: `{{ $json.from.name || 'Lieber Kunde' }}`

**Field 4:**
- Name: email_subject_sanitized
- Type: String (Expression)
- Value: `{{ $json.subject.replace(/Re:/g, '').trim() }}`

5. Save node

**Output (Example):**
```json
{
  ...original fields...,
  "content_combined": "Frage zum Preis des AeroWisch AI Hallo, wie viel kostet der AeroWisch AI?",
  "sender_email": "max@example.com",
  "sender_name": "Max Mustermann",
  "email_subject_sanitized": "Frage zum Preis des AeroWisch AI"
}
```

---

### NODE 3: IF - PRICE INQUIRY?

**Position in Workflow:** Below Node 2

**Visual Layout:**
```
┌──────────────────────────────────┐
│  🔀 IF - Preisanfrage?           │
├──────────────────────────────────┤
│ Condition Type: String           │
│ Field 1 (Value 1):               │
│ {{ $json.content_combined }}     │
│                                  │
│ Operation: Regex                 │
│ Field 2 (Value 2):               │
│ preis|kosten|euro|€|eur|price    │
│ |cost|rabatt|discount            │
│                                  │
│ 📌 Case Insensitive: ON ✓        │
└──────────────────────────────────┘
```

**Configuration Steps:**
1. Click "+" → Search "IF"
2. Select "IF" node
3. Configure condition:
   - Condition Type: "String"
   - Field 1 (compare): `{{ $json.content_combined }}`
   - Operation: "Regex"
   - Field 2 (against): `preis|kosten|euro|€|eur|price|cost|kosten?|rabatt|angebot`
   - Case Insensitive: Enable ✓

4. Connect:
   - True output (green) → to "Send Email - Preis" node
   - False output (red) → to next IF node

**Decision Logic:**
```
If content_combined matches regex (case-insensitive):
  ✓ preis          → Price Inquiry
  ✓ kosten         → Price Inquiry
  ✓ euro           → Price Inquiry
  ✓ €              → Price Inquiry
  ✓ price          → Price Inquiry
  ✓ cost           → Price Inquiry
  ✓ rabatt/discount → Price Inquiry
  
Then: Send Price Response
Else: Continue to next IF (Defect check)
```

---

### NODE 4: IF - DEFECT/DAMAGE?

**Position in Workflow:** Below Node 3 (FALSE path)

**Visual Layout:**
```
┌──────────────────────────────────┐
│  🔀 IF - Defekt/Schaden?         │
├──────────────────────────────────┤
│ Condition Type: String           │
│ Field 1 (Value 1):               │
│ {{ $json.content_combined }}     │
│                                  │
│ Operation: Regex                 │
│ Field 2 (Value 2):               │
│ defekt|schaden|kaputt|fehler|    │
│ beschäd|nicht.*?funktioniert|    │
│ broken|error|problem|issue       │
│                                  │
│ 📌 Case Insensitive: ON ✓        │
└──────────────────────────────────┘
```

**Configuration Steps:**
1. Click "+" → Search "IF"
2. Select "IF" node
3. Configure condition:
   - Condition Type: "String"
   - Field 1 (compare): `{{ $json.content_combined }}`
   - Operation: "Regex"
   - Field 2 (against): `defekt|schaden|kaputt|fehler|beschäd|nicht.*?funktioniert|broken|error|problem|issue|bruch|riss`
   - Case Insensitive: Enable ✓

4. Connect:
   - True output (green) → to "Create Ticket" + "Send Email - Defekt"
   - False output (red) → to "Send Email - Fallback"

**Decision Logic:**
```
If content_combined matches regex (case-insensitive):
  ✓ defekt            → Defect Report
  ✓ schaden           → Defect Report
  ✓ kaputt            → Defect Report
  ✓ fehler            → Defect Report
  ✓ nicht funktioniert → Defect Report
  ✓ broken/error      → Defect Report
  ✓ problem/issue     → Defect Report
  
Then: Create Ticket + Send Defect Response
Else: Send Generic Response
```

---

### NODE 5: SEND EMAIL - PREIS

**Position in Workflow:** Right of Node 3 (TRUE path)

**Visual Layout:**
```
┌──────────────────────────────────┐
│  📧 Send Email - Preis           │
├──────────────────────────────────┤
│ Credentials: Gmail SMTP          │
│ From Email: support@aerowisch.de │
│ From Name: AeroWisch Support     │
│ To: {{ $json.sender_email }}     │
│                                  │
│ Subject:                         │
│ "Ihre Anfrage zum Preis..."      │
│                                  │
│ Body (HTML):                     │
│ [See email template section]     │
│                                  │
│ Headers: Optional                │
└──────────────────────────────────┘
```

**Configuration Steps:**
1. Click "+" → Search "Send Email"
2. Select "Send Email" node
3. Credentials: Select Gmail SMTP (create if needed)
4. Set fields:
   - From Email: `support@aerowisch.de`
   - From Name: `AeroWisch Support Team`
   - To: `{{ $json.sender_email }}`
   - Subject: `Ihre Anfrage zum Preis von AeroWisch AI`
   - Email Type: HTML
   - Body: [Copy from training-materials.md "Template 1"]

5. Replace placeholders:
   - `{{ $json.sender_name }}` → Customer name
   - `€249.99` → Your product price
   - URLs → Your store links

6. Save node

**Body Template (Simplified):**
```
Guten Tag {{ $json.sender_name }},

vielen Dank für Ihre Nachricht. Der AeroWisch AI kostet 249,99 EUR.

Im Lieferumfang: Gerät, Ladestation, 2x Pads, Guide, 24-Monate Garantie.

→ Jetzt bestellen: https://aerowisch.de/bestellung

Mit freundlichen Grüßen
Ihr AeroWisch-Supportteam
```

---

### NODE 6: SEND EMAIL - DEFEKT

**Position in Workflow:** Right of Node 4 (TRUE path, parallel)

**Visual Layout:**
```
┌──────────────────────────────────┐
│  📧 Send Email - Defekt          │
├──────────────────────────────────┤
│ Credentials: Gmail SMTP          │
│ From Email: support@aerowisch.de │
│ From Name: AeroWisch Support     │
│ To: {{ $json.sender_email }}     │
│                                  │
│ Subject:                         │
│ "Wir kümmern uns um..."          │
│                                  │
│ Body (HTML):                     │
│ [See email template section]     │
└──────────────────────────────────┘
```

**Configuration Steps:**
1. Click "+" → Search "Send Email"
2. Select "Send Email" node
3. Credentials: Select Gmail SMTP
4. Set fields:
   - From Email: `support@aerowisch.de`
   - From Name: `AeroWisch Support Team`
   - To: `{{ $json.sender_email }}`
   - Subject: `Wir kümmern uns um Ihren AeroWisch AI`
   - Email Type: HTML
   - Body: [Copy from training-materials.md "Template 2"]

5. Add variables:
   - `{{ $json.sender_name }}` → Customer name
   - Include ticket number when available

6. Save node

---

### NODE 7: SEND EMAIL - FALLBACK

**Position in Workflow:** Right of Node 4 (FALSE path)

**Visual Layout:**
```
┌──────────────────────────────────┐
│  📧 Send Email - Fallback        │
├──────────────────────────────────┤
│ Credentials: Gmail SMTP          │
│ From Email: support@aerowisch.de │
│ From Name: AeroWisch Support     │
│ To: {{ $json.sender_email }}     │
│                                  │
│ Subject:                         │
│ "Ihre Nachricht an Support..."   │
│                                  │
│ Body (HTML):                     │
│ [Generic holding response]       │
└──────────────────────────────────┘
```

**Configuration Steps:**
1. Click "+" → Search "Send Email"
2. Select "Send Email" node
3. Credentials: Select Gmail SMTP
4. Set fields:
   - From Email: `support@aerowisch.de`
   - From Name: `AeroWisch Support Team`
   - To: `{{ $json.sender_email }}`
   - Subject: `Ihre Nachricht an den AeroWisch-Support`
   - Email Type: HTML
   - Body: [Copy from training-materials.md "Template 3"]

5. Variables:
   - `{{ $json.sender_name }}` → Customer name

6. Save node

---

### NODE 8: CREATE TICKET - FRESHDESK

**Position in Workflow:** Above Node 6 (Defect path, before email)

**Visual Layout:**
```
┌──────────────────────────────────┐
│  🎟️ Create Ticket - Freshdesk    │
├──────────────────────────────────┤
│ Request Type: HTTP Request       │
│ Method: POST                     │
│ URL: https://[domain].freshdesk. │
│      com/api/v2/tickets          │
│                                  │
│ Auth: Basic Auth                 │
│ Username: [API Key]              │
│ Password: X                      │
│                                  │
│ Headers: Content-Type: JSON      │
│                                  │
│ Body (JSON):                     │
│ {                                │
│   "subject": "...",              │
│   "description": "...",          │
│   "email": "...",                │
│   "priority": 2,                 │
│   "status": 2,                   │
│   "tags": ["aerowisch"]          │
│ }                                │
└──────────────────────────────────┘
```

**Configuration Steps:**
1. Click "+" → Search "HTTP Request"
2. Select "HTTP Request" node
3. Set basic fields:
   - Method: POST
   - URL: `https://[YOUR-DOMAIN].freshdesk.com/api/v2/tickets`
   - Authentication: Basic Auth
   - Username: [Your Freshdesk API Key]
   - Password: `X` (required by API)

4. Headers:
   - Content-Type: `application/json`

5. Body (JSON):
```json
{
  "subject": "{{ $json.email_subject_sanitized }}",
  "description": "Von: {{ $json.from.name }} <{{ $json.sender_email }}>\nDatum: {{ $json.date }}\n\n--- Original Email ---\n\n{{ $json.text }}",
  "email": "{{ $json.sender_email }}",
  "priority": 2,
  "status": 2,
  "tags": ["aerowisch", "defect", "auto-ticket"]
}
```

6. Save node

**Important:**
- Replace `[YOUR-DOMAIN]` with your Freshdesk subdomain
- Get API key from: Admin → API & Custom Fields → API Tokens
- Test with GET /tickets first to verify credentials

---

### NODE 9: MARK AS READ

**Position in Workflow:** Converge point (bottom)

**Visual Layout:**
```
┌──────────────────────────────────┐
│  ✅ Mark Email as Read + Log     │
├──────────────────────────────────┤
│ Type: Set Node                   │
│                                  │
│ New Fields:                      │
│  1. processed_status = "done"    │
│  2. processed_at = timestamp     │
│  3. processed_category = result  │
│                                  │
│ Purpose: Audit trail & logging   │
└──────────────────────────────────┘
```

**Configuration Steps:**
1. Click "+" → Search "Set"
2. Select "Set" node
3. Mode: "Manual mode"
4. Add fields:
   - processed_status: `done`
   - processed_at: `{{ new Date().toISOString() }}`
   - processed_category: `{{ $json.processed_category }}`

5. Save node

---

## 🔌 NODE CONNECTIONS SUMMARY

```
NODE 1 (IMAP Trigger)
  └─ main output → NODE 2 (Prepare Content)

NODE 2 (Prepare Content)
  └─ main output → NODE 3 (IF Price?)

NODE 3 (IF Price?)
  ├─ TRUE → NODE 5 (Send Email Preis) → NODE 9 (Mark)
  └─ FALSE → NODE 4 (IF Defekt?)

NODE 4 (IF Defekt?)
  ├─ TRUE → NODE 8 (Create Ticket)
  │         └─ → NODE 6 (Send Email Defekt) → NODE 9 (Mark)
  └─ FALSE → NODE 7 (Send Email Fallback) → NODE 9 (Mark)

NODE 5,6,7 (Send Email nodes)
  └─ All converge → NODE 9 (Mark as Read)

NODE 9 (Mark as Read)
  └─ Workflow ends ✅
```

---

## 📱 QUICK n8n UI NAVIGATION

**Creating a Workflow:**
```
1. Click "+" in sidebar
2. Select "New Workflow"
3. Name: "AeroWisch AI - Email Support"
4. Save (Ctrl+S)

Adding Nodes:
1. Click "+" in center of canvas
2. Search node name (e.g., "Email Trigger")
3. Click to add
4. Configure in right panel
5. Connect to other nodes

Connecting Nodes:
1. Hover over output circle (right side of node)
2. Drag to input circle (left side of target node)
3. Connection appears as line

Testing:
1. Click node → "Execute" button
2. See output in "Output" tab
3. Debug using "Inspector" mode

Saving:
1. Ctrl+S or click Save button
2. Shows green checkmark when saved

Activating:
1. Top right: "Activate" toggle
2. Shows blue when active
3. Workflow now watches for triggers
```

---

## ✅ FINAL VALIDATION CHECKLIST

**Before Activating Workflow:**

- [ ] All 9 nodes created and visible
- [ ] Node 1 (IMAP): Connected to support email
- [ ] Node 2 (Set): Creates 4 new fields
- [ ] Node 3 (IF): Regex patterns working
- [ ] Node 4 (IF): Regex patterns working
- [ ] Node 5 (Email): Template filled in
- [ ] Node 6 (Email): Template filled in
- [ ] Node 7 (Email): Template filled in
- [ ] Node 8 (HTTP): Freshdesk URL correct
- [ ] Node 9 (Set): Logging fields ready
- [ ] All connections correct (9 arrows)
- [ ] Test with sample email: Response received
- [ ] Test with defect email: Ticket created
- [ ] Monitor dashboard: All executions green ✓

**Then: ACTIVATE WORKFLOW ✅**

---

**Version:** 1.0
**Last Updated:** 2025-11-27
**Status:** Ready for Build

