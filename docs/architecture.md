\# Architecture v0.1



\## Deployment View



```mermaid

flowchart TB

&#x20;   I\[Internet]

&#x20;   N\[Azure NSG: 22, 80]

&#x20;   F\[UFW: 22, 80]

&#x20;   C\[Caddy :80]

&#x20;   G\[Gunicorn 127.0.0.1:8000]

&#x20;   A\[Flask]



&#x20;   I --> N --> F --> C --> G --> A

```



\## Resource Constraints

\- Azure Standard B2ats v2, 2 vCPU, 892 MiB RAM, 30 GB disk

\- Swap 1 GiB sebagai buffer



\## Security Decisions

\- Akses admin lewat user non-root (azureuseramel) dengan sudo

\- SSH key-only (Ed25519), password dan root login dinonaktifkan

\- Dua lapis firewall: Azure NSG dan UFW (hanya 22 dan 80)

\- Backend loopback-only; Caddy satu-satunya pintu publik

\- GitHub deploy key read-only



\## Current Limitations

\- HTTP saja, tanpa HTTPS

\- Satu VM, tanpa database, tanpa container, deployment manual



\## Planned Evolution

M04 DNS dan HTTPS, M05 database, M06 container, M07 IaC, M09 CI/CD.

