# ChatGPT Capability, Connector, Skill, RDC, and Email Integration Report

> **Agent:** ChatGPT (GPT-5.6 Luna)  
> **Audit timestamp:** 2026-09-19 11:34 -05:00  
> **Purpose:** Capability and integration audit only. No irreversible actions were performed.

## 1. Connectors — currently active/verified

### GitHub
- **(a) Status:** Active; authenticated account **DeOdini** was verified.
- **(b) Linkage:** GitHub MCP connector authenticated to the connected account.
- **(c) Purpose:** Repository, code, issues, pull requests, branches, commits and CI/CD inspection.
- **(d) Active usage:** Read/search repositories, inspect diffs/logs, and perform authorized development operations.
- **(e) Safe tests:** Search a repository; inspect a PR; read CI logs; create a test branch without merging.

### Figma
- **(a) Status:** Active; authenticated user/team access verified.
- **(b) Linkage:** Figma MCP authentication; current account reports a Starter team with a View seat.
- **(c) Purpose:** Design inspection, design-to-code, code-to-design, components, variables, diagrams and motion.
- **(d) Active usage:** Inspect designs and use Figma operations subject to file/seat permissions.
- **(e) Safe tests:** Inspect a frame; read design context; generate a test diagram; create a disposable test file.

### Supabase
- **(a) Status:** Active; one organization was verified.
- **(b) Linkage:** Authenticated Supabase MCP organization access.
- **(c) Purpose:** PostgreSQL, Auth, Storage, Edge Functions, Realtime, vectors and migrations.
- **(d) Active usage:** Inspect schemas, query databases, review migrations and work with authorized project resources.
- **(e) Safe tests:** List tables; run a read-only SELECT; inspect migrations; generate database types.

### Render
- **(a) Status:** Active; a Render workspace was verified.
- **(b) Linkage:** Authenticated Render workspace access.
- **(c) Purpose:** Hosting, web services, static sites, workers, cron, PostgreSQL, Key Value, logs and deployments.
- **(d) Active usage:** Inspect services/deployments/logs/metrics and perform authorized infrastructure operations.
- **(e) Safe tests:** List services; inspect a deployment; read logs; validate a render.yaml without deploying.

### Microsoft Outlook Email
- **(a) Status:** Active; connected mailbox profile verified.
- **(b) Linkage:** Authenticated Outlook/Microsoft Graph integration.
- **(c) Purpose:** Regular email search, reading, drafting, replying and organization.
- **(d) Active usage:** Search/read messages, inspect attachments and create drafts; sending requires explicit authorization.
- **(e) Safe tests:** Search a subject; summarize a message; create an unsent draft; inspect attachment metadata.

### Brevo
- **(a) Status:** Active; connected marketing account verified.
- **(b) Linkage:** Authenticated Brevo integration.
- **(c) Purpose:** Marketing email, contacts, lists, segments, templates, campaigns and analytics.
- **(d) Active usage:** Inspect lists/campaigns/templates and perform authorized marketing operations.
- **(e) Safe tests:** Read campaign statistics; inspect a list; create a non-sent draft/test campaign.

## 2. Skills — actively installed

> Skill linkage means the instruction package is available to the agent; a skill does **not** itself grant external credentials.

### Base44
- **base44-cli:** (a) Installed/active. (b) Skill registry. (c) Base44 resource configuration and deployment. (d) Guides project implementation. (e) **Test:** inspect a disposable project configuration.
- **base44-remote-dev:** (a) Installed/active. (b) Skill registry + Base44 connector when authenticated. (c) Remote sandbox development. (d) Guides edit→preview→verify. (e) **Test:** read/write a test sandbox file.
- **base44-sandbox:** (a) Installed/active. (b) Skill registry. (c) Cloud sandbox development. (d) Guides entities/functions/agents. (e) **Test:** create a disposable test entity.
- **base44-sdk:** (a) Installed/active. (b) Skill registry. (c) Base44 SDK integration. (d) Guides remote resource calls/backend functions. (e) **Test:** inspect SDK types or example usage.
- **base44-troubleshooter:** (a) Installed/active. (b) Skill registry. (c) Production error diagnosis. (d) Analyzes backend-function logs. (e) **Test:** analyze synthetic/test logs.

### Supabase
- **supabase:** (a) Installed/active. (b) Skill registry + Supabase connector. (c) Database/Auth/Storage/Functions/Realtime work. (d) Applied before Supabase tasks. (e) **Test:** inspect a schema read-only.
- **supabase-postgres-best-practices:** (a) Installed/active. (b) Skill registry. (c) PostgreSQL optimization. (d) Reviews queries/schema. (e) **Test:** analyze a SELECT plan without changing data.

### Email
- **resend-cli:** (a) Installed/active. (b) Skill registry + Resend CLI when authenticated. (c) Resend domains, templates, logs, broadcasts and sending. (d) Guides safe CLI usage. (e) **Test:** preview a test email.
- **react-email:** (a) Installed/active. (b) Skill registry. (c) React HTML email templates. (d) Builds/renders responsive email. (e) **Test:** render a sample template locally.
- **email-best-practices:** (a) Installed/active. (b) Skill registry. (c) Deliverability, authentication, compliance and accessibility. (d) Audits email implementations. (e) **Test:** audit SPF/DKIM/DMARC guidance or a template.
- **agent-email-inbox:** (a) Installed/active. (b) Skill registry. (c) Secure inbound-email automation. (d) Guides filtering/sandboxing of untrusted email. (e) **Test:** process synthetic inbound email.

### Render
- **render-background-workers:** (a) Installed. (b) Skill registry. (c) Queue/async workers. (d) Guides worker configuration. (e) **Test:** validate a worker design.
- **render-blueprints:** (a) Installed. (b) Skill registry + Render. (c) render.yaml IaC. (d) Authors/validates blueprints. (e) **Test:** validate YAML without deployment.
- **render-cli:** (a) Installed. (b) Skill registry + Render CLI when configured. (c) Deploy/logs/SSH/psql automation. (d) Guides non-interactive CLI use. (e) **Test:** inspect CLI help/status.
- **render-cron-jobs:** (a) Installed. (b) Skill registry. (c) Scheduled Render jobs. (d) Designs cron schedules. (e) **Test:** validate a cron expression.
- **render-debug:** (a) Installed. (b) Skill registry + Render. (c) Deployment debugging. (d) Analyzes logs/metrics/database state. (e) **Test:** diagnose a synthetic failure.
- **render-deploy:** (a) Installed. (b) Skill registry + Render. (c) Application deployment. (d) Generates deployment configuration. (e) **Test:** generate a non-applied blueprint.
- **render-disks:** (a) Installed. (b) Skill registry + Render. (c) Persistent disks/storage. (d) Guides mount/size/snapshot configuration. (e) **Test:** inspect storage requirements.
- **render-docker:** (a) Installed. (b) Skill registry. (c) Docker deployment. (d) Guides Dockerfiles/multi-stage builds. (e) **Test:** lint a Dockerfile conceptually.
- **render-domains:** (a) Installed. (b) Skill registry + Render. (c) Domains/TLS/DNS. (d) Guides HTTPS/domain configuration. (e) **Test:** review DNS records without changing them.
### Render skills continued
- **render-env-vars:** (a) Installed. (b) Skill registry + Render. (c) Environment variables/secrets. (d) Guides safe configuration. (e) **Test:** inspect variable names only.
- **render-keyvalue:** (a) Installed. (b) Skill registry + Render. (c) Redis-compatible Key Value. (d) Guides cache/session/queue setup. (e) **Test:** design a non-production cache.
- **render-mcp:** (a) Installed. (b) Skill registry + Render. (c) Render MCP setup/authentication. (d) Guides MCP configuration. (e) **Test:** inspect MCP setup requirements.
- **render-migrate-from-heroku:** (a) Installed. (b) Skill registry + Render. (c) Heroku migration. (d) Maps local configuration to Render. (e) **Test:** generate a migration plan without applying it.
- **render-monitor:** (a) Installed. (b) Skill registry + Render. (c) Service health/metrics/logs. (d) Monitors authorized services. (e) **Test:** read current service health.
- **render-networking:** (a) Installed. (b) Skill registry + Render. (c) Private networking/service discovery. (d) Guides inter-service connections. (e) **Test:** map a proposed network.
- **render-postgres:** (a) Installed. (b) Skill registry + Render. (c) Managed PostgreSQL. (d) Guides connections/backups/replicas. (e) **Test:** inspect connection architecture without changing DB.
- **render-private-services:** (a) Installed. (b) Skill registry + Render. (c) Internal services/microservices. (d) Guides private-service architecture. (e) **Test:** design a private API.
- **render-scaling:** (a) Installed. (b) Skill registry + Render. (c) Autoscaling/cost optimization. (d) Guides instance counts and targets. (e) **Test:** model scaling settings without applying.
- **render-static-sites:** (a) Installed. (b) Skill registry + Render. (c) Static-site/CDN deployment. (d) Guides SPA routing/build/publish paths. (e) **Test:** validate static-site configuration.
- **render-web-services:** (a) Installed. (b) Skill registry + Render. (c) Web services/health/TLS. (d) Guides service configuration. (e) **Test:** inspect health-check configuration.
- **render-workflows:** (a) Installed. (b) Skill registry + Render. (c) Render Workflows. (d) Guides tasks/retries/deployment. (e) **Test:** design a local workflow without deploying.

### Figma
- **figma-code-connect:** (a) Installed. (b) Skill registry + Figma. (c) Maps Figma components to code. (d) Creates/maintains Code Connect templates. (e) **Test:** generate a mapping file.
- **figma-create-new-file:** (a) Installed. (b) Skill registry + Figma. (c) New Design/FigJam/Slides files. (d) Mandatory prerequisite for create_new_file. (e) **Test:** create a disposable blank file.
- **figma-design-to-code:** (a) Installed. (b) Skill registry + Figma. (c) Figma→code implementation. (d) Prerequisite for design-context reads. (e) **Test:** inspect a sample design.
- **figma-generate-design:** (a) Installed. (b) Skill registry + Figma. (c) Code/description→Figma layouts. (d) Builds composed views incrementally. (e) **Test:** generate a test landing-page frame.
- **figma-generate-diagram:** (a) Installed. (b) Skill registry + Figma. (c) Architecture/flow/ERD diagrams. (d) Guides diagram generation. (e) **Test:** generate a test architecture diagram.
- **figma-generate-library:** (a) Installed. (b) Skill registry + Figma. (c) Design systems/components/tokens. (d) Builds library foundations. (e) **Test:** plan a disposable component library.
- **figma-generative-plugins:** (a) Installed. (b) Skill registry + Figma. (c) Generative plugin development. (d) Prerequisite for plugin creation/editing. (e) **Test:** inspect a plugin specification.
- **figma-implement-motion:** (a) Installed. (b) Skill registry + Figma. (c) Figma motion→production code. (d) Translates motion context. (e) **Test:** map sample animation to CSS.
- **figma-shaders:** (a) Installed. (b) Skill registry + Figma. (c) Shader effects/fills. (d) Prerequisite for shader operations. (e) **Test:** design a non-applied shader effect.
- **figma-swiftui:** (a) Installed. (b) Skill registry + Figma. (c) SwiftUI↔Figma translation. (d) Routes iOS design/code workflows. (e) **Test:** translate a sample component.
- **figma-use:** (a) Installed. (b) Skill registry + Figma. (c) Programmatic Figma operations. (d) Mandatory prerequisite for use_figma. (e) **Test:** inspect a test node.
- **figma-use-figjam:** (a) Installed. (b) Skill registry + Figma. (c) FigJam use_figma context. (d) Guides FigJam operations. (e) **Test:** inspect a test board.
- **figma-use-motion:** (a) Installed. (b) Skill registry + Figma. (c) Motion editing context. (d) Used alongside figma-use. (e) **Test:** inspect sample keyframes.
- **figma-use-slides:** (a) Installed. (b) Skill registry + Figma. (c) Slides use_figma context. (d) Guides slide operations. (e) **Test:** inspect a test slide.

### Stripe
- **stripe-connect-recommend:** (a) Installed. (b) Skill registry; Stripe account access separate. (c) Connect/payment-routing design. (d) Guides marketplaces and payouts. (e) **Test:** review a test Connect architecture.
- **stripe-apps:** (a) Installed. (b) Skill registry + Stripe when authenticated. (c) Stripe Dashboard apps/extensions. (d) Guides scaffold/preview/upload/versioning. (e) **Test:** inspect a test manifest.
- **stripe-best-practices:** (a) Installed. (b) Skill registry. (c) Secure payments/billing/Connect. (d) Reviews integration choices. (e) **Test:** audit a test-mode integration.
- **stripe-directory:** (a) Installed. (b) Skill registry. (c) Provider/service discovery. (d) Finds relevant services. (e) **Test:** search a development service category.
- **stripe-docs:** (a) Installed. (b) Skill registry. (c) Stripe documentation/API reference. (d) Searches official docs. (e) **Test:** look up a test API endpoint.
- **stripe-projects:** (a) Installed. (b) Skill registry + Stripe when authenticated. (c) Cloud-service provisioning/catalog. (d) Guides project resources. (e) **Test:** inspect available providers without provisioning.
- **upgrade-stripe:** (a) Installed. (b) Skill registry. (c) Stripe API/SDK upgrades. (d) Guides version migrations. (e) **Test:** analyze a version migration without applying changes.

### Other installed skills
- **plugin-management:** (a) Installed. (b) Skill registry + plugin connector. (c) Discover/inspect/manage integrations. (d) Checks availability and permissions. (e) **Test:** inspect a named plugin's permissions.
- **grok-bot-control:** (a) Installed. (b) Skill registry; installation does not grant Grok access. (c) Authorized Grok handoffs. (d) Coordinates bounded interactions when access exists. (e) **Test:** reconcile a synthetic handoff.

## 3. Other Connectors and Skills — available but not all verified

### Base44
- **(a)** Connector available; current app listing returned none. **(b)** Would authenticate via Base44 MCP/CLI. **(c)** AI app builder/sandbox. **(d)** Can create/edit/test authorized apps. **(e)** **Safe test:** create a disposable app.

### Replit
- **(a)** Connector available; current app listing returned none. **(b)** Would use authenticated Replit connector. **(c)** Rapid application development/deployment. **(d)** Can inspect/build authorized apps. **(e)** **Safe test:** create a throwaway Hello World app.

### Resend
- **(a)** Connector/CLI skill available; account linkage not independently verified. **(b)** OAuth/API/CLI authentication when configured. **(c)** Transactional email, templates, domains, logs and webhooks. **(d)** Can operate authenticated resources. **(e)** **Safe test:** preview a test template.

### Stripe
- **(a)** Connector available; account linkage not independently verified. **(b)** Authenticated Stripe MCP when configured. **(c)** Payments/subscriptions/Connect/API. **(d)** Can inspect and build test-mode integrations. **(e)** **Safe test:** inspect API schemas without creating charges.

### Upwork
- **(a)** Connector available; account linkage not independently verified. **(b)** Would use authenticated Upwork connector. **(c)** Jobs, proposals, contracts and messaging. **(d)** Can search/inspect authorized marketplace data. **(e)** **Safe test:** search jobs without applying or messaging.

### Outlook Calendar
- **(a)** Connector available; account linkage not independently verified. **(b)** Microsoft calendar authentication when configured. **(c)** Events and availability. **(d)** Can read/schedule authorized calendar resources. **(e)** **Safe test:** inspect availability without creating an event.

## 4. RDC — Remote Desktop Commander

### DESKTOP-DHRIH27
- **(a)** Online; authenticated RDC device.
- **(b)** Access rating: **Full operational** within the exposed RDC filesystem/process scope; this does not prove Windows Administrator privileges.
- **(c)** Can inspect/write files, run processes, read outputs, search code and perform developer workflows.
- **(d)** **Safe examples:** list a project, read package.json, run tests, run a type-check, inspect logs, create a harmless test-output file.

### localhost
- **(a)** Registered/authenticated but **offline** at audit time.
- **(b)** Access rating: **None while offline**; stored registration is not active operational access.
- **(c)** No active work can be relied upon until it reconnects.
- **(d)** **Safe example after reconnection:** ping it, inspect a project directory, or run a read-only test.

## 5. Emails

### Microsoft Outlook — regular email
- **(a)** Active connected mailbox.
- **(b)** Authenticated Outlook/Microsoft Graph integration.
- **(c)** Regular correspondence, search, reading, drafting and organization.
- **(d)** I can search/read messages and create drafts; sending requires explicit authorization.
- **(e)** **Safe test:** search a test subject and create an unsent reply draft.

### Brevo — marketing email
- **(a)** Active connected marketing account.
- **(b)** Authenticated Brevo integration.
- **(c)** Campaigns, contacts, lists, segments, templates and analytics.
- **(d)** I can inspect and prepare authorized marketing resources.
- **(e)** **Safe test:** inspect campaign statistics or create a non-sent test campaign.

### Resend — potential/available
- **(a)** Connector/skill available; account not verified in this audit.
- **(b)** Would link via Resend authentication/API/CLI.
- **(c)** Transactional and developer email.
- **(d)** Usable after authentication.
- **(e)** **Safe test:** render an email without sending.

## Limitations and uncertainties
- Connector availability is not equivalent to account authorization.
- GitHub, Figma, Supabase, Render, Outlook and Brevo were directly verified.
- Base44/Replit currently returned no user apps.
- Resend/Stripe/Upwork/Outlook Calendar were not counted as verified account connections.
- RDC exposes broad filesystem/process operations, but Administrator/root privileges were not established.
- No production data was intentionally modified, no email was sent, no payment was made, and no destructive command was run.
- Figma access is constrained by the connected plan/seat and file permissions; Figma documents that access depends on plan/seat and that read-tool rate limits apply. fileciteturn0file0L5-L8
- Figma also states that content access is limited to resources the authenticated user is permitted to view/edit. fileciteturn0file0L72-L78
- If a category is not currently verified, it is explicitly labeled as available/potential rather than active.

## Audit completion
- **Agent name:** ChatGPT
- **File path:** `C:\Users\USER\DEODINI_BRAINBOX\BRAINBOX\CHATGPT_FUNC_BRAINBOX.md`
- **Status:** Created
- **Timestamp:** 2026-09-19 11:34 -05:00
