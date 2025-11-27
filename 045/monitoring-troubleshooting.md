# Troubleshooting & Monitoring Guide
## AeroWisch AI Email Automation Workflow

---

## 📊 DAILY MONITORING CHECKLIST

### Morning Check (5 minutes)

**Dashboard Metrics to Review:**
```
□ Emails Processed Last 24h: ___ (target: > 10)
□ Success Rate: ___ % (target: > 95%)
□ Average Response Time: ___ ms (target: < 5000ms)
□ Error Count: ___ (target: 0)
□ Tickets Created: ___ (should match defect emails)
```

**Log Review:**
```
□ Any failed workflows? YES / NO
□ Any timeouts? YES / NO
□ Any classification errors? YES / NO
□ Any IMAP connection issues? YES / NO
□ Any SMTP delivery failures? YES / NO
```

**Quick Actions If Issues:**
- Error rate > 5%? → Check last 10 execution logs
- No emails detected? → Test IMAP connection manually
- Responses not sent? → Check SMTP credentials + rate limits

---

### Weekly Review (30 minutes)

**Accuracy Analysis:**
```
Total emails processed: ___
Correctly classified: ___
Misclassified: ___ (acceptable: < 5%)

Breakdown:
├─ Price emails: ___ correct, ___ wrong
├─ Defect emails: ___ correct, ___ wrong
└─ Other emails: ___ correct, ___ wrong
```

**Customer Feedback:**
```
□ Any complaints about auto-replies?
□ Any positive feedback?
□ Any emails that should NOT have been auto-handled?
□ Any patterns in misclassifications?
```

**Keyword Refinement:**
```
If misclassifications > 5%:
1. Document misclassified emails
2. Identify missing keywords
3. Update IF conditions in n8n
4. Test with 10 sample emails
5. Deploy updated keywords
```

---

## 🔧 COMMON ISSUES & SOLUTIONS

### Issue 1: Workflow Not Running / Trigger Not Firing

**Symptoms:**
- No emails being processed
- IMAP Trigger shows "inactive"
- n8n dashboard shows "paused"

**Solutions:**

**Step 1: Check if Workflow is Active**
```
1. Go to n8n dashboard
2. Click on workflow: "AeroWisch AI - Email Support"
3. Look for toggle in top-right
4. Status should be: "Active" (blue toggle)
5. If inactive: Click toggle to activate
```

**Step 2: Check IMAP Connection**
```
In n8n, click IMAP Trigger node:
1. "Test" button → Execute test
2. Expected: Email received ✓ or "No new emails"
3. If error: "Connection refused" or "Authentication failed"
   → Check credentials (see Issue 2)
```

**Step 3: Check n8n Logs**
```
1. Click workflow name → "Executions" tab
2. Look for recent executions
3. If last execution > 1 hour ago → Trigger not running
4. Restart: Deactivate + Activate workflow
```

**Quick Fix:**
```bash
# If n8n self-hosted, restart service:
docker restart n8n
# or
pm2 restart n8n
```

---

### Issue 2: IMAP Authentication Failed

**Error Message:**
```
"Email Trigger (IMAP) failed with: 
Authentication failed or connection refused"
```

**Root Causes & Solutions:**

**Cause A: Wrong Password (Most Common)**
```
Gmail Setup:
1. Go to https://myaccount.google.com/apppasswords
2. Generate NEW app password (if never done)
3. Copy the 16-character password
4. In n8n: Update IMAP credential with new password
5. Test connection: Should work ✓
```

**Cause B: 2FA Not Enabled**
```
Gmail Setup:
1. Go to https://myaccount.google.com/security
2. Find "2-Step Verification"
3. Click "Get started" if not enabled
4. Complete 2FA setup
5. Now generate App Password (see Cause A)
```

**Cause C: IMAP Not Enabled in Gmail**
```
Gmail Settings:
1. Go to Gmail: Settings → Forwarding and POP/IMAP
2. Look for: "IMAP Access"
3. Select: "Enable IMAP"
4. Save changes
5. Wait 5 minutes
6. Test connection in n8n
```

**Cause D: Using Wrong Email**
```
Double-check:
1. n8n IMAP credential: support@aerowisch.de
2. Gmail account: support@aerowisch.de
3. Are they the same account? YES / NO
4. If not same: Update n8n credential
```

**Cause E: Credentials Expired or Revoked**
```
Solution:
1. Remove existing credential: Credentials → Delete
2. Create NEW credential: Add new → Email (IMAP)
3. Re-authenticate Gmail account
4. Follow 2FA + App Password steps
5. Test connection
```

---

### Issue 3: Emails Received But Not Being Processed

**Symptoms:**
- Emails arrive in inbox
- Trigger fires (you see execution)
- But no auto-reply sent
- No error shown

**Root Cause:** Email is being marked as read before processing

**Solutions:**

**Check 1: Email Filter Issue**
```
n8n IMAP Trigger settings:
1. Click trigger node → scroll down
2. Check "Filter only unread emails" setting
3. If enabled: emails auto-marked as read = never processed again
4. Solution: Mark support email as "unread" manually
5. Or: Disable filter, process all emails
```

**Check 2: Email Already Processed**
```
1. Check n8n execution history
2. Search for original email (by subject)
3. If found: Email was already processed
4. To reprocess: Manually mark as unread in Gmail
5. Workflow will trigger again
```

**Check 3: Workflow Paused at IF Node**
```
1. Go to workflow executions
2. Click on failed/stuck execution
3. Look for "IF - Preisanfrage?" or other IF node
4. Expanded: Shows what happened at decision point
5. If stuck: Click "Resume" or "Retry"
```

---

### Issue 4: Email Response Not Being Sent

**Symptoms:**
- Workflow executes
- Trigger fires
- IF conditions pass
- But no email arrives at customer

**Root Cause:** SMTP delivery failure

**Solutions:**

**Step 1: Check SMTP Credentials**
```
n8n: Click "Send Email" node
1. Check "From" field: support@aerowisch.de
2. Check credentials dropdown
3. Test connection: Click "Test credentials"
4. Expected: "Connection successful" ✓
```

**Step 2: Check Gmail Rate Limits**
```
Gmail free account: 99 emails/day limit

Check:
1. How many emails sent today?
2. Gmail: Settings → Forwarding/IMAP
3. Check usage stats (if available)
4. If > 99: Try again tomorrow OR upgrade account
```

**Step 3: Check Email Recipient**
```
In n8n Send Email node:
1. "To" field should contain: {{ $json.sender_email }}
2. Test: Click node → "Execute test"
3. Check output: "To" field populated correctly?
4. If empty: Original email format problem
```

**Step 4: Check Gmail Blocked Senders**
```
Gmail may block mass sending:
1. Gmail: Search for emails from n8n
2. Any in spam folder? → Add to contacts
3. Any blocked? → Whitelist sender
4. Try sending one test email manually
5. If works: Restart workflow
```

---

### Issue 5: Freshdesk Ticket Not Being Created

**Symptoms:**
- Defect email received
- Send Email works
- But no ticket in Freshdesk
- No error in n8n

**Root Cause:** API authentication or request format issue

**Solutions:**

**Step 1: Check API Credentials**
```
n8n: Click HTTP Request node (Create Ticket)
1. Check "Authorization" field
2. Credentials should be: "Basic Auth"
3. Check Authorization field is populated
4. Click "Test credentials" (if available)
```

**Step 2: Test API Manually**
```
Using Postman or curl:

curl -X GET \
  -H "Authorization: Basic BASE64_ENCODED_KEY:X" \
  https://domain.freshdesk.com/api/v2/tickets

Replace:
- BASE64_ENCODED_KEY = base64(API_KEY:X)
- domain = your Freshdesk subdomain

Expected response: 200 OK + list of tickets
If error: 401 Unauthorized → API key wrong
```

**Step 3: Check Freshdesk Custom Fields**
```
If tickets created but without data:

1. Freshdesk: Admin → Custom Fields
2. Check custom fields exist:
   - aerowisch_ticket_type
   - original_email_id
3. If missing: Remove from n8n request
4. Simplify body to only required fields:
   - subject
   - description
   - email
   - priority
   - status
```

**Step 4: Verify API URL**
```
n8n HTTP Request node:
1. URL field: https://domain.freshdesk.com/api/v2/tickets
2. Check: Replace "domain" with YOUR Freshdesk subdomain
3. If wrong: Update URL
4. Test again: Should work ✓
```

---

### Issue 6: Wrong Email Classification

**Symptoms:**
- Price email classified as "Other"
- Defect email marked as regular inquiry
- Random misclassifications

**Root Cause:** Keywords not matching due to typos or wording variation

**Solutions:**

**Step 1: Analyze Misclassified Email**
```
1. Find the misclassified email
2. Copy the full subject + body
3. Check: Does it contain keywords?
   - Price: "kosten", "preisliste", "wie teuer"?
   - Defect: "defekt", "funktioniert nicht", "kaputt"?
4. Document the missing keyword
```

**Step 2: Update IF Conditions**
```
n8n: Click IF node (e.g., "IF - Preisanfrage?")
1. Edit conditions
2. Current regex: preis|kosten|euro|...
3. Add missing keyword: preis|kosten|euro|...|NEW_KEYWORD
4. Example: "wie teuer" → add "teuer"
   Updated: preis|kosten|euro|...|teuer
5. Save
```

**Step 3: Test Updated Keyword**
```
1. Send test email with the problematic wording
2. Workflow should now classify correctly
3. If still wrong: Keyword case sensitivity?
   - Try lowercase: teuer → teuer (should work)
   - Or make case-insensitive (n8n does by default)
```

**Step 4: Document for Future**
```
Keep a "Keywords Misses" log:
Date | Email Subject | Missed Keyword | Fixed?
11/27 | "Wie teuer?" | "teuer" | ✓
11/28 | "Gerät defekt" | "defekt" | ✓
```

---

### Issue 7: Workflow Runs But Takes Too Long

**Symptoms:**
- Workflow executes
- But takes > 10 seconds
- Customer notices delayed response

**Root Cause:** External API delays, overloaded IMAP, or network issues

**Solutions:**

**Step 1: Identify Bottleneck**
```
n8n execution details (click execution):
Node 1 (IMAP): 100ms ← Expected
Node 2 (Set): 50ms ← Expected
Node 3 (IF): 50ms ← Expected
Node 4 (HTTP Freshdesk): 3000ms ← SLOW!
Node 5 (Email): 500ms
Total: 3700ms (acceptable)

If > 10000ms (10 seconds):
- Likely culprit: Freshdesk API or network delay
- Solutions: See below
```

**Step 2: Optimize Freshdesk Call**
```
If Freshdesk API is slow:
1. Parallel execution: Create ticket + Send email at same time
   (instead of sequential)
2. Async operation: Fire ticket creation but don't wait
3. Reduce request payload: Remove unnecessary fields
```

**Step 3: Check Network/Infrastructure**
```
1. n8n server location: Close to users?
2. Freshdesk datacenter: US/EU?
3. If far apart: Expect 500-1000ms just for network
4. Solutions: Choose geographically closer servers
```

---

## 📋 MONITORING TEMPLATE (Daily Log)

Use this template to track workflow health daily:

```
═══════════════════════════════════════════
WORKFLOW MONITORING LOG
Date: 2025-11-27
═══════════════════════════════════════════

METRICS:
├─ Emails Processed: 12
├─ Success Rate: 100% ✓
├─ Avg Response Time: 2.3s ✓
├─ Error Rate: 0% ✓
├─ Tickets Created: 3
└─ Manual Interventions: 0

CLASSIFICATION BREAKDOWN:
├─ Price Inquiries: 5 (100% correct)
├─ Defects: 3 (100% correct)
└─ Other: 4 (100% correct)

ISSUES FOUND:
□ None
□ Minor (describe): _______________
□ Major (describe): _______________

ACTIONS TAKEN:
□ None
□ Adjusted keywords: _______________
□ Updated templates: _______________
□ Restarted workflow: _______________

NOTES:
_________________________________
_________________________________

Checked by: Tech Lead
Time: 09:00 CET
═══════════════════════════════════════════
```

---

## 🚨 ESCALATION MATRIX

### When to Escalate Issues:

| Issue | Severity | Action | Escalate To |
|-------|----------|--------|------------|
| Single email misclassified | Low | Document, adjust keywords | Tech Lead |
| 5%+ misclassification rate | Medium | Emergency keyword update | Product Manager |
| 0 emails processed (> 1 hour) | High | Check IMAP, restart workflow | DevOps / Tech Lead |
| Freshdesk API down (30+ min) | Critical | Manual backup process | VP Support + DevOps |
| SMTP rate limit exceeded | Medium | Upgrade account or use second account | VP Support + Finance |
| Customer complaints (3+) | High | Review templates, adjust, apologize | Customer Success |
| Data breach / credentials exposed | CRITICAL | Immediate rotation, incident report | Security + Legal |

---

## 📞 SUPPORT CONTACTS

```
Tech Issues: tech-lead@aerowisch.de
API Issues: devops@aerowisch.de
Customer Complaints: support-manager@aerowisch.de
Escalations: product-manager@aerowisch.de
Emergency (after hours): CTO-on-call
```

---

**Last Updated:** 2025-11-27
**Version:** 1.0
**Owner:** Tech Lead

