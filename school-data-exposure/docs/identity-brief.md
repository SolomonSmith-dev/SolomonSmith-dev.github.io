# Identity / SSO surface (public observation)

**Gate:** DI-11 (provisional)  
**Method:** unauthenticated HTTP only. No passwords. Query tokens redacted.

## Observed hop (Canvas)

1. Student hits `csusb.instructure.com/login/saml`
2. Browser is redirected to Instructure Identity host pattern `*.login.instructure.com`
3. OAuth/OIDC-style authorize flow references `sso.canvaslms.com` callback and returns toward `csusb.instructure.com`

## Related campus identity pieces (documented on ITS pages)

- myCoyote portal
- DUO MFA
- Coyote OneCard

## Abuse / risk framing

Cross-domain login is normal for modern SSO. The exposure issue is transparency: students see a CSUSB-branded academic relationship but type credentials into vendor identity infrastructure, then enter an LMS that can launch Turnitin and Respondus Monitor. Without a published hop diagram and processor list, consent is structural rather than informed.

## Still needed (DI-10)

Own-account capture after login to list third-party requests inside Canvas/myCoyote. Not done.
