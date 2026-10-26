---
name: replica-deploy
description: >
  Orchestrates the preflight verification gate, production configuration, DNS mapping,
  and deployment checklist to ship an app clone safely to production. Step 11 of the Replica suite.
  Trigger: When preparing for production deployment, configuring DNS, running preflight gates, or releasing an app clone.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# replica-deploy

> **PHILOSOPHY: VERIFY EVERYTHING BEFORE SHIPMENT.**
> Nothing goes to production based on hope.
> An automated preflight gate ensures tests pass, must-haves are 100% complete, and the codebase is completely scrubbed of competitor references.

Reads all assets in `replica/`.
Writes `replica/deploy.md` based on `replica/deploy/preflight.md`.

---

## 1. The Preflight Gate (MANDATORY)

Execute every verification command and log results in `replica/deploy.md`:

```bash
# 1. End-to-End Test Suite
npx playwright test

# 2. Must-Have Feature Parity (Exit 0 required)
python tools/parity.py replica/features.csv

# 3. Clean Brand Sweep (Exit 0 required: no competitor names/colors)
python tools/sweep.py . --config replica/brand.json

# 4. App Store Listing Validation (if releasing mobile apps)
python tools/listing.py replica/launch/listing.json
```

> [!CAUTION]
> If ANY check fails or exits with an error code, **the deployment is blocked immediately**.
> Resolve the underlying failure before proceeding.

---

## 2. Production Environment & Infrastructure

1. **Isolated Production Database:** Never share development or staging instances. Verify automated daily backups and point-in-time recovery (PITR) are enabled.
2. **Environment Variables:** Populate production secrets directly in your hosting platform (Vercel, Cloudflare, Fly.io, AWS) matching `.env.example`.
3. **Stripe Live Mode Activation:**
   - Switch Stripe API keys to `pk_live_...` and `sk_live_...`.
   - Recreate products and price IDs in the live environment.
   - Configure live webhook endpoints and record the live `whsec_...` signing secret.
   - Execute one end-to-end real card test purchase and refund it immediately.
4. **OAuth Redirect Origins:** Add your production domain (`https://app.yourdomain.com`) to authorized origins in Google Cloud Console, Apple Developer Portal, and GitHub OAuth apps.

---

## 3. DNS & Domain Configuration

Provide explicit DNS records for the domain registrar:

| Type | Host | Value | Purpose |
| :--- | :--- | :--- | :--- |
| `A` | `@` | Host IP (e.g. `76.76.21.21`) | Root web domain |
| `CNAME` | `www` | Host CNAME alias | WWW redirect |
| `CNAME` | `app` | Host CNAME alias | Application subdomain |
| `TXT` | `@` | SPF verification string | Transactional email auth |
| `CNAME` | `resend._domainkey` | DKIM public key | DKIM email deliverability |
| `TXT` | `_dmarc` | `v=DMARC1; p=none;` | DMARC policy |

---

## 4. Operational Monitoring & Health

- Configure error reporting (Sentry or Highlight) with production sourcemaps.
- Establish uptime monitoring (Better Uptime, Checkly, or Cronitor).
- Verify transactional email delivery rates and webhook status logs.

---

## Deliverables Checklist
- [ ] Preflight gate executed and 100% green.
- [ ] Production database migrated and isolated.
- [ ] Stripe live keys and webhooks verified.
- [ ] DNS and email records propagated.
- [ ] Sentry / error monitoring active.
- [ ] Application live on custom domain.
