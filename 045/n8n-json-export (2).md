# n8n Workflow JSON Export
## AeroWisch AI - Customer Support Automation v1.0

```json
{
  "name": "AeroWisch AI - Email Support Automation",
  "nodes": [
    {
      "parameters": {
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        },
        "options": {
          "filter": {
            "unread": true
          },
          "allowSelfSignedCerts": true
        }
      },
      "id": "1",
      "name": "Email Trigger - IMAP",
      "type": "n8n-nodes-base.emailTrigger",
      "typeVersion": 1,
      "position": [
        100,
        300
      ],
      "credentials": {
        "imap": "IMAP_CREDENTIAL_ID"
      }
    },
    {
      "parameters": {
        "mode": "manual",
        "jsonData": {
          "content_combined": "={{ $json.subject }} {{ $json.text }}",
          "sender_email": "={{ $json.from.address }}",
          "sender_name": "={{ $json.from.name || 'Lieber Kunde' }}",
          "email_subject_sanitized": "={{ $json.subject.replace(/Re:/g, '').trim() }}"
        }
      },
      "id": "2",
      "name": "Prepare Content",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        300,
        300
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.content_combined.toLowerCase() }}",
              "value2": "preis|kosten|kostenpunkt|euro|€|eur|price|cost",
              "operation": "regex"
            }
          ]
        }
      },
      "id": "3",
      "name": "IF - Preisanfrage?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        500,
        200
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.content_combined.toLowerCase() }}",
              "value2": "defekt|schaden|kaputt|fehler|beschäd|nicht.*?funktioniert|broken|error|problem|issue",
              "operation": "regex"
            }
          ]
        }
      },
      "id": "4",
      "name": "IF - Defekt/Schaden?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        700,
        450
      ]
    },
    {
      "parameters": {
        "fromEmail": "support@aerowisch.de",
        "fromName": "AeroWisch Support Team",
        "to": "={{ $json.sender_email }}",
        "subject": "Ihre Anfrage zum Preis von AeroWisch AI",
        "text": "Guten Tag {{ $json.sender_name }},\n\nvielen Dank für Ihre Nachricht und Ihr Interesse an unserem AeroWisch AI.\nDer aktuelle Preis für den AeroWisch AI beträgt 249,99 EUR (inkl. MwSt.).\n\nIm Lieferumfang enthalten sind:\n- AeroWisch AI Gerät\n- Premium Ladestation\n- 2 Sätze Reinigungspads\n- Digitaler Schnellstart-Guide\n- 24 Monate Herstellergarantie\n\nGern beraten wir Sie, welche Variante am besten zu Ihrem Haushalt oder Büro passt.\n\nMit freundlichen Grüßen\nIhr AeroWisch-Supportteam",
        "html": true
      },
      "id": "5",
      "name": "Send Email - Preis",
      "type": "n8n-nodes-base.sendEmail",
      "typeVersion": 1,
      "position": [
        700,
        100
      ],
      "credentials": {
        "smtp": "GMAIL_SMTP_CREDENTIAL_ID"
      }
    },
    {
      "parameters": {
        "fromEmail": "support@aerowisch.de",
        "fromName": "AeroWisch Support Team",
        "to": "={{ $json.sender_email }}",
        "subject": "Wir kümmern uns um Ihren AeroWisch AI",
        "text": "Guten Tag {{ $json.sender_name }},\n\nvielen Dank für Ihre Nachricht und den Hinweis auf den Defekt/Schaden an Ihrem AeroWisch AI.\nEs tut uns leid, dass es zu Problemen mit Ihrem Gerät gekommen ist.\n\nWir haben soeben ein Support-Ticket für Sie erstellt.\nUnser Serviceteam prüft Ihren Fall und meldet sich in der Regel innerhalb von 24–48 Stunden mit den nächsten Schritten bei Ihnen.\n\nFür eine schnellere Bearbeitung können Sie uns folgende Informationen zukommen lassen:\n- Seriennummer des Geräts\n- Kaufdatum und Händler\n- Eine kurze Fehlerbeschreibung\n- Ggf. Fotos oder ein kurzes Video\n\nVielen Dank für Ihre Unterstützung und Ihr Vertrauen.\n\nMit freundlichen Grüßen\nIhr AeroWisch-Supportteam",
        "html": true
      },
      "id": "6",
      "name": "Send Email - Defekt",
      "type": "n8n-nodes-base.sendEmail",
      "typeVersion": 1,
      "position": [
        900,
        400
      ],
      "credentials": {
        "smtp": "GMAIL_SMTP_CREDENTIAL_ID"
      }
    },
    {
      "parameters": {
        "fromEmail": "support@aerowisch.de",
        "fromName": "AeroWisch Support Team",
        "to": "={{ $json.sender_email }}",
        "subject": "Ihre Nachricht an den AeroWisch-Support",
        "text": "Guten Tag {{ $json.sender_name }},\n\nvielen Dank für Ihre Nachricht.\nWir haben Ihre Anfrage erhalten und leiten sie an das zuständige Team weiter.\n\nIn der Regel erhalten Sie innerhalb von 24–48 Stunden eine persönliche Rückmeldung von uns.\n\nSollten Sie in der Zwischenzeit weitere Informationen ergänzen wollen, können Sie einfach auf diese E-Mail antworten.\n\nMit freundlichen Grüßen\nIhr AeroWisch-Supportteam",
        "html": true
      },
      "id": "7",
      "name": "Send Email - Fallback",
      "type": "n8n-nodes-base.sendEmail",
      "typeVersion": 1,
      "position": [
        900,
        600
      ],
      "credentials": {
        "smtp": "GMAIL_SMTP_CREDENTIAL_ID"
      }
    },
    {
      "parameters": {
        "httpMethod": "POST",
        "url": "{{ env.FRESHDESK_API_URL }}/tickets",
        "authentication": "headerAuth",
        "headerAuth_headers": {
          "Authorization": "Basic {{ Buffer.from(env.FRESHDESK_API_KEY + ':X').toString('base64') }}"
        },
        "contentType": "application/json",
        "body": {
          "subject": "{{ $json.email_subject_sanitized }}",
          "description": "E-Mail von: {{ $json.from.name }} <{{ $json.sender_email }}>\nDatum: {{ $json.date }}\n\n---\nOriginal-Email-Text:\n\n{{ $json.text }}",
          "email": "{{ $json.sender_email }}",
          "priority": 2,
          "status": 2,
          "tags": [
            "aerowisch",
            "defect",
            "auto-ticket"
          ],
          "custom_fields": {
            "aerowisch_ticket_type": "Defect Report",
            "original_email_id": "{{ $json.messageId }}"
          }
        }
      },
      "id": "8",
      "name": "Create Ticket - Freshdesk",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4,
      "position": [
        900,
        250
      ]
    },
    {
      "parameters": {
        "mode": "manual",
        "jsonData": {
          "marked_as_processed": true,
          "processed_timestamp": "={{ new Date().toISOString() }}",
          "processed_category": "={{ $json.category || 'unknown' }}"
        }
      },
      "id": "9",
      "name": "Mark Email as Read",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        1100,
        300
      ]
    }
  ],
  "connections": {
    "Email Trigger - IMAP": {
      "main": [
        [
          {
            "node": "Prepare Content",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Prepare Content": {
      "main": [
        [
          {
            "node": "IF - Preisanfrage?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF - Preisanfrage?": {
      "main": [
        [
          {
            "node": "Send Email - Preis",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "IF - Defekt/Schaden?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF - Defekt/Schaden?": {
      "main": [
        [
          {
            "node": "Create Ticket - Freshdesk",
            "type": "main",
            "index": 0
          },
          {
            "node": "Send Email - Defekt",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send Email - Fallback",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send Email - Preis": {
      "main": [
        [
          {
            "node": "Mark Email as Read",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send Email - Defekt": {
      "main": [
        [
          {
            "node": "Mark Email as Read",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send Email - Fallback": {
      "main": [
        [
          {
            "node": "Mark Email as Read",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create Ticket - Freshdesk": {
      "main": [
        [
          {
            "node": "Send Email - Defekt",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1",
    "saveManualExecutions": true,
    "callerPolicy": "workflowsFromPublicAPI"
  },
  "staticData": null,
  "versionId": "1.0.0"
}
```

## Import-Anleitung:

1. n8n öffnen → Menu → Import
2. Diese JSON hier reinkopieren
3. Credentials setzen:
   - `IMAP_CREDENTIAL_ID` → deine Gmail IMAP Credentials
   - `GMAIL_SMTP_CREDENTIAL_ID` → dein Gmail App-Password
   - Umgebungsvariablen setzen:
     - `FRESHDESK_API_URL` = https://domain.freshdesk.com/api/v2
     - `FRESHDESK_API_KEY` = dein API Key
4. Workflow speichern und testen

