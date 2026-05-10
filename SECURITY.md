# Security Policy

## Supported versions

The following table describes which versions of this project are currently receiving security updates.

| Version   | Status          |
|----------|-----------------|
| `main`   | ✅ Actively supported |
| Older tags/releases | ⚠️ Best-effort only (no guaranteed fixes) |

If you are using a fork or a significantly modified version, you are responsible for reviewing and applying upstream security fixes.

---

## Reporting a vulnerability

**Please do not open public GitHub issues for security vulnerabilities.**

Instead, report security concerns through one of the following private channels:

- **Email:** `youremail@example.com` (replace with your preferred contact)
- **GitHub Security Advisories:** Use the “Report a vulnerability” feature on the repository’s **Security** tab, if enabled.

When reporting, include as much detail as possible:

- **Description:** Clear explanation of the issue and potential impact  
- **Steps to reproduce:** Minimal, reproducible example or script  
- **Environment details:** OS, Python version, dependencies, and configuration  
- **Proof of concept (if applicable):** Any exploit or sample input demonstrating the issue

You will receive an acknowledgment within **3 business days**, and we aim to provide an initial assessment or next steps within **7 business days**.

---

## Disclosure policy

- **Responsible disclosure:** Please give us a reasonable opportunity to investigate and remediate before any public disclosure.
- **No public exploits:** Avoid publishing exploit code or detailed attack steps until a fix has been released and users have had time to update.
- **Coordinated release:** When possible, we will:
  - Develop and test a fix
  - Tag a new release or update `main`
  - Update documentation and/or changelog
  - Coordinate a disclosure window if the issue is high impact

If we determine that a reported issue is not a security vulnerability, we’ll explain why and, where appropriate, track it as a regular bug.

---

## Data handling and scraping ethics

This project is a **web scraper**, which means security and ethics overlap:

- **Respect target sites’ policies:**  
  - Review and honor `robots.txt` where applicable  
  - Follow the website’s Terms of Service  
- **Rate limiting:**  
  - Use reasonable request rates to avoid denial-of-service behavior  
- **No unauthorized access:**  
  - Do not use this project to bypass authentication, paywalls, or access data you are not permitted to access  
- **Personal data:**  
  - Avoid scraping sensitive personal information  
  - If you must process personal data, ensure compliance with relevant privacy laws and regulations

---

## API keys, credentials, and secrets

If this project uses any credentials (for example, to access APIs or proxies), follow these rules:

- **Never commit secrets:**  
  - Do **not** commit API keys, passwords, tokens, or cookies to the repository  
  - Do **not** store secrets in source files, example configs, or test data
- **Use environment variables:**  
  - Store secrets in environment variables (e.g., `.env` files) that are **ignored** by Git (`.gitignore`)  
  - Provide a sample file like `.env.example` with placeholder values only
- **Local configuration only:**  
  - Keep machine-specific or user-specific configuration out of version control  
- **Key rotation:**  
  - If a secret is accidentally exposed, revoke and rotate it immediately

If you discover any leaked credentials in this repository’s history, please report them as a security vulnerability.

---

## Secure development guidelines

Contributors are expected to follow these practices when modifying or extending the project:

- **Input validation:**
  - Treat all external input (URLs, query parameters, scraped content) as untrusted  
  - Validate and sanitize user-provided URLs before fetching
- **Dependency hygiene:**
  - Prefer pinned versions in `requirements.txt` or similar  
  - Regularly update dependencies to patch known vulnerabilities
- **Error handling and logging:**
  - Avoid logging secrets, cookies, or full HTML responses that may contain sensitive data  
  - Use structured, minimal logs suitable for debugging without exposing private information
- **File system safety:**
  - Validate file paths and filenames if user-controlled  
  - Avoid writing arbitrary content to arbitrary paths
- **Network safety:**
  - Use HTTPS endpoints whenever possible  
  - Be cautious with redirects and untrusted domains

Before opening a pull request, consider:

- **Could this change expose more data than before?**  
- **Does it introduce new external input or dependencies?**  
- **Are secrets still fully excluded from the codebase and logs?**

---

## Security contact and feedback

If you have questions about this security policy or suggestions for improving it, please reach out via the same contact used for vulnerability reports:

- **Security contact:** jhgarci4@asu.edu

We appreciate responsible security research and thoughtful reports that help keep this project and its users safer.
