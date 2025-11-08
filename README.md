# EVIDENCE AUTHENTICATION AND CHAIN OF CUSTODY

## REPOSITORY: All_Events – 201 Evidentiary PDF Documents

**Case Reference:** R202518589_00 | R202518214_00 (Residential Tenancies – VCAT)
**Property:** 1803-243 Franklin Street, Melbourne VIC 3000 | 33 Camberwell Road, Hawthorn East VIC 3123
**Document Custodian:** Chawakorn Kamnuansil
**Repository Established:** 8 November 2025
**Last Updated:** 9 November 2025

---

## TABLE OF CONTENTS

1. [Authentication Certificate](#authentication-certificate)
2. [Chain of Custody](#chain-of-custody)
3. [Evidence Summary](#evidence-summary)
4. [Technical Verification](#technical-verification)
5. [File Manifest and Metadata](#file-manifest-and-metadata)
6. [Admissibility & Procedural Framework](#admissibility--procedural-framework)
7. [Access & Integrity Protocols](#access--integrity-protocols)
8. [References](#references)
9. [Document Control](#document-control)

---

## AUTHENTICATION CERTIFICATE

### DECLARATION OF AUTHENTICITY

I, **Chawakorn Kamnuansil**, declare that:

1. **Collection and Custody**: I am the originating party and custodian of the evidence stored in this repository. Materials were collected during Residential Tenancies proceedings before VCAT (Case Nos. R202518589_00 and R202518214_00).

2. **Completeness**: The repository contains **201 PDF documents** representing the complete, unaltered set of evidence for the periods relevant to these proceedings. Where redactions appear, they are limited to lawful privacy/security needs.

3. **Authenticity & Integrity**: Each document:
   • originates from correspondence, notices, receipts, applications, orders, or records issued by or to the parties;
   • was scanned or converted to PDF without material alteration;
   • is tracked with SHA-256 and SHA-512 cryptographic hashes;
   • is accompanied by filename metadata and CSV manifests. Under the *Evidence Act 2008 (Vic)*, “document” includes electronic records and reproductions [s 3](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/s3.html); proof of contents and machine-produced documents is governed by [ss 48, 147](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/).

4. **Chain of Possession**: From collection to present, materials remained under my control with local encrypted storage and a version-controlled backup on GitHub. Git object IDs (SHA-1 by default, with an option to use SHA-256) identify content; commit/tag signing and “Verified” status further attest origin where used [git-scm.com](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work), [GitHub Docs](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification).

5. **Compliance with Evidence Rules (Victoria)**:
   • **Business records & documents**: records created/kept in the course of business are generally admissible subject to reliability [Evidence Act ss 69, 48, 51](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/).
   • **Electronic communications**: limited hearsay exception for identity/date/destination particulars [s 71](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/s71.html); statutory presumptions as to sending/receipt/timing [s 161](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/s161.html).
   • **Machine-generated proof**: documents produced by processes/machines (e.g., scans, system exports) are provable under [s 147](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/s147.html).
   • **VCAT procedure**: VCAT may inform itself as it sees fit and is not bound by strict rules of evidence [VCAT Act 1998 (Vic) s 98](https://classic.austlii.edu.au/au/legis/vic/consol_act/vcaata1998377/s98.html).
   • **AI disclosure**: AI tools assisted with hashing and manifest preparation; responsibility for accuracy remains mine, consistent with the Supreme Court of Victoria’s guideline on responsible AI use (6 May 2024) [SCV](https://www.supremecourt.vic.gov.au/news/supreme-court-issues-guidelines-for-litigants-responsible-use-of-ai-in-litigation).

6. **No Tampering or Loss**: To the best of my knowledge, no document has been lost, destroyed, altered, or accessed without authority.

**Signature**: Chawakorn Kamnuansil
**Date**: 9 November 2025
**Location**: Melbourne, Victoria, Australia

---

## CHAIN OF CUSTODY

### Chronology of Collection & Preservation

| Date                      | Stage         | Action                                                                         | Custody Holder                     | Purpose                         | Notes                                                                                                                                                                                                                                                                        |
| ------------------------- | ------------- | ------------------------------------------------------------------------------ | ---------------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 16 Oct 2024 – 31 Oct 2025 | Collection    | Emails, notices, receipts, tribunal/court documents gathered contemporaneously | Chawakorn Kamnuansil               | Ongoing dispute response        | Originals retained where possible                                                                                                                                                                                                                                            |
| Oct – Dec 2024            | Organisation  | Exports from email; scans of physical records to PDF/A where practical         | Chawakorn Kamnuansil               | Archival & disclosure readiness | No substantive edits                                                                                                                                                                                                                                                         |
| 2 Nov 2025                | Manifesting   | SHA-256/SHA-512 computed for all files; metadata extracted                     | Chawakorn Kamnuansil (AI-assisted) | Integrity & traceability        | Hashes recorded in APPENDIX A                                                                                                                                                                                                                                                |
| 8 Nov 2025                | Repository    | 201 PDFs pushed to GitHub repo “All_Events” (with LFS for large binaries)      | Chawakorn Kamnuansil               | Versioned backup & transparency | Git LFS used for binaries [GitHub Well-Architected](https://wellarchitected.github.com/library/architecture/recommendations/scaling-git-repositories/when-to-use-git-lfs/); billing model [GitHub Docs](https://docs.github.com/en/billing/concepts/product-billing/git-lfs) |
| 8–9 Nov 2025              | Documentation | CSV manifests created (message IDs, subjects, dates); README published         | Chawakorn Kamnuansil               | Cross-reference & navigation    | APPENDIX B (Message_id.csv)                                                                                                                                                                                                                                                  |
| 9 Nov 2025                | Verification  | Re-hash check against originals; review of Git history                         | Chawakorn Kamnuansil               | Final integrity check           | No discrepancies detected                                                                                                                                                                                                                                                    |

### Custody Locations & Safeguards

**Primary Storage (GitHub)**
• Repo: github.com/ck999kk/All_Events (public read, owner write)
• Git object IDs + optional commit/tag signatures [Git](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work), [GitHub](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)
• GitHub encrypts source code at rest on GitHub.com [GitHub Blog](https://github.blog/changelog/2019-05-22-git-data-encryption-at-rest/)

**Secondary Storage (Local)**
• Encrypted macOS FileVault volume; offline copies of PDFs and CSVs.

**Disclosure Contexts**
• VCAT Residential Tenancies List filings and directions hearings (service and evidence under VCAT Rules & Practice Notes) [VCAT Rules 2018](https://www.legislation.vic.gov.au/in-force/statutory-rules/victorian-civil-and-administrative-tribunal-rules-2018), [PNVCAT1](https://www.vcat.vic.gov.au/documents/practice-notes/practice-note-pnvcat1-common-procedures), evidence guidance for residential tenancies cases [VCAT](https://www.vcat.vic.gov.au/case-types/residential-tenancies/generally-how-send-and-access-evidence-residential-tenancies-case).
• If a matter is transferred or related litigation arises, County Court discovery procedures apply under the **County Court Civil Procedure Rules 2018** (Order 29 – Discovery) [AustLII index](https://classic.austlii.edu.au/au/legis/vic/consol_reg/cccpr2018/).

---

## EVIDENCE SUMMARY

### Quantitative Overview

| Category                         | Count | Date Range                | Primary Subjects                          |
| -------------------------------- | ----- | ------------------------- | ----------------------------------------- |
| Email communications             | 78    | 2 Feb 2025 – 28 Aug 2025  | Maintenance, access, lease administration |
| Tribunal/court orders & listings | 25    | 22 Jul 2025 – 15 Aug 2025 | VCAT/RDRV orders, hearing notices         |
| Maintenance/repair notices       | 40    | 16 Apr 2025 – 9 Jul 2025  | Leak, wall/carpet damage, inspections     |
| Receipts & payments              | 23    | 25 Feb 2025 – 28 Oct 2025 | Rent, bond, tax invoices                  |
| Tenancy/legal notices            | 17    | 11 Jul 2025 – 28 Aug 2025 | NTV, NOE, vacating instructions, demands  |
| Legal documents                  | 3     | 24 Jun 2025 – 12 Aug 2025 | Affidavits, applications                  |
| Employment records               | 2     | 1 Sep 2025 – 15 Sep 2025  | Attendance letters (contextual)           |
| Medical documentation            | 2     | 23–24 Jun 2025            | Certificates, expenses                    |
| Exhibits (photos/inspections)    | 4     | 1 Jul 2025                | A–D                                       |
| Administrative/insurance         | 7     | 7 Oct 2024 – 20 Oct 2025  | Agreements, manager notices, insurer      |

**Total files: 201 PDFs**

---

## TECHNICAL VERIFICATION

**Standards**
• **SHA-256 / SHA-512** per NIST FIPS 180-4 [NIST](https://csrc.nist.gov/publications/detail/fips/180/4/final).
• **PDF/A** for long-term preservation where applicable (ISO 19005) [ISO](https://www.iso.org/standard/38920.html).

**Verification Steps**

1. Download any PDF from the repository.
2. Compute a local SHA-256 digest (e.g., macOS/Linux: shasum -a 256 filename; Windows PowerShell: Get-FileHash -Algorithm SHA256).
3. Compare against the value in APPENDIX A (SHA256_512.csv).
4. A match indicates integrity; a mismatch indicates tampering or transfer error.

---

## FILE MANIFEST AND METADATA

**APPENDIX A – SHA256_512.csv**
• 201 rows: file number, filename, SHA-256, SHA-512, category, path, size, modified date.
• Primary integrity cross-reference (see FIPS 180-4) [NIST](https://csrc.nist.gov/publications/detail/fips/180/4/final).

**APPENDIX B – Message_id.csv**
• 201 rows: ID, filename, date, subject, message-ID, domain, email address, size, modified date.
• 146 files include a message-ID; 55 are non-email documents.
• Email particulars are corroborated by Evidence Act [s 71](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/s71.html) (limited hearsay exception) and presumptions in [s 161](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/s161.html).

---

## ADMISSIBILITY & PROCEDURAL FRAMEWORK

**VCAT Evidence Handling**
• VCAT may receive written/electronic material and is not bound by strict evidence rules; weight is for the Tribunal to assess [VCAT Act s 98](https://classic.austlii.edu.au/au/legis/vic/consol_act/vcaata1998377/s98.html).
• Residential tenancies guidance on sending/receiving evidence: filing timelines, page limits, and service requirements [VCAT guidance](https://www.vcat.vic.gov.au/case-types/residential-tenancies/generally-how-send-and-access-evidence-residential-tenancies-case), with procedures supplemented by [VCAT Rules 2018](https://www.legislation.vic.gov.au/in-force/statutory-rules/victorian-civil-and-administrative-tribunal-rules-2018) and [PNVCAT1](https://www.vcat.vic.gov.au/documents/practice-notes/practice-note-pnvcat1-common-procedures).
• Residential Tenancies List includes specific service provisions (e.g., Order 8) such as **r 8.03** (mode of service for certain applications) [AustLII](https://classic.austlii.edu.au/au/legis/vic/num_reg/vcaatr2018n77o2018558/s8.03.html).

**Evidence Act (key pathways)**
• **Business records**: s 69 permits admission of business records subject to conditions [AustLII index](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/).
• **Electronic communications**: s 71 hearsay exception (identity/date/destination) and s 161 presumptions of sending/receipt [s 71](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/s71.html), [s 161](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/s161.html).
• **Machine-produced documents**: s 147 for documents produced by processes/machines in business [s 147](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/s147.html).

**County Court (if applicable)**
• Discovery/disclosure governed by **Order 29 (Discovery)** in the *County Court Civil Procedure Rules 2018* [AustLII index](https://classic.austlii.edu.au/au/legis/vic/consol_reg/cccpr2018/). (Note: r 37.02 concerns inspection/preservation orders and is not the general discovery rule.)

**Responsible Use of AI**
• Any AI assistance is disclosed in accordance with the Supreme Court of Victoria guideline (6 May 2024). Human accountability for content and correctness remains with the party filing the material [SCV](https://www.supremecourt.vic.gov.au/news/supreme-court-issues-guidelines-for-litigants-responsible-use-of-ai-in-litigation).

---

## ACCESS & INTEGRITY PROTOCOLS

**Repository**: [https://github.com/ck999kk/All_Events](https://github.com/ck999kk/All_Events)
• Public read; owner-restricted write access.
• Git LFS used for large binaries [Well-Architected](https://wellarchitected.github.com/library/architecture/recommendations/scaling-git-repositories/when-to-use-git-lfs/).
• Data at rest encrypted by GitHub infrastructure [GitHub Blog](https://github.blog/changelog/2019-05-22-git-data-encryption-at-rest/).
• For confidential filings, provide sealed/limited-access copies per VCAT directions and practice notes [PNVCAT1](https://www.vcat.vic.gov.au/documents/practice-notes/practice-note-pnvcat1-common-procedures).

**For Proceedings**

1. Download required PDFs.
2. Compute and record local SHA-256 digests.
3. Compare with APPENDIX A to confirm integrity.
4. Serve and lodge evidence per VCAT directions, Rules, and list-specific guidance [VCAT evidence guidance](https://www.vcat.vic.gov.au/case-types/residential-tenancies/generally-how-send-and-access-evidence-residential-tenancies-case), [VCAT Rules](https://www.legislation.vic.gov.au/in-force/statutory-rules/victorian-civil-and-administrative-tribunal-rules-2018).

---

## REFERENCES

• *Evidence Act 2008 (Vic)*: authorised version & index [legislation.vic.gov.au](https://www.legislation.vic.gov.au/in-force/acts/evidence-act-2008), [AustLII index](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/); definitions [s 3](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/s3.html); business records [s 69](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/s69.html); electronic communications hearsay exception [s 71](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/s71.html); presumptions about electronic communications [s 161](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/s161.html); machine-produced documents [s 147](https://classic.austlii.edu.au/au/legis/vic/consol_act/ea200880/s147.html).
• *VCAT Act 1998 (Vic)*: evidence flexibility [s 98](https://classic.austlii.edu.au/au/legis/vic/consol_act/vcaata1998377/s98.html).
• *VCAT Rules 2018*: current version & Order 8 (Residential Tenancies) [legislation.vic.gov.au](https://www.legislation.vic.gov.au/in-force/statutory-rules/victorian-civil-and-administrative-tribunal-rules-2018); mode of service (example) [r 8.03](https://classic.austlii.edu.au/au/legis/vic/num_reg/vcaatr2018n77o2018558/s8.03.html); Practice Note PNVCAT1 [VCAT](https://www.vcat.vic.gov.au/documents/practice-notes/practice-note-pnvcat1-common-procedures).
• VCAT guidance: sending/accessing evidence in residential tenancies [VCAT](https://www.vcat.vic.gov.au/case-types/residential-tenancies/generally-how-send-and-access-evidence-residential-tenancies-case).
• *County Court Civil Procedure Rules 2018*: discovery (Order 29) [AustLII index](https://classic.austlii.edu.au/au/legis/vic/consol_reg/cccpr2018/).
• NIST FIPS 180-4 (SHA-2 standard) [NIST](https://csrc.nist.gov/publications/detail/fips/180/4/final).
• ISO 19005 (PDF/A) [ISO](https://www.iso.org/standard/38920.html).
• Git signing & verification: [git-scm.com](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work), [GitHub Docs](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification).
• GitHub encryption at rest: [GitHub Blog](https://github.blog/changelog/2019-05-22-git-data-encryption-at-rest/).
• Supreme Court of Victoria AI guideline (6 May 2024): [SCV](https://www.supremecourt.vic.gov.au/news/supreme-court-issues-guidelines-for-litigants-responsible-use-of-ai-in-litigation).

---

## DOCUMENT CONTROL

| Field               | Value                                                                          |
| ------------------- | ------------------------------------------------------------------------------ |
| **Document Title**  | Evidence Authentication and Chain of Custody                                   |
| **Type**            | Repository README / Authentication Certificate                                 |
| **Version**         | 1.1 (corrected legal references; refined VCAT/County Court citations)          |
| **Date Created**    | 9 November 2025                                                                |
| **Custodian**       | Chawakorn Kamnuansil                                                           |
| **Repository**      | [https://github.com/ck999kk/All_Events](https://github.com/ck999kk/All_Events) |
| **Jurisdiction**    | Victoria, Australia                                                            |
| **Related Matters** | VCAT R202518589_00; VCAT R202518214_00                                         |

---
