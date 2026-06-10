# Provenance and Clean-Room Policy

This project is published as a clean-room scientific plotting library.

The public repository should contain reusable source code, generated demo data,
documentation, validation scripts, and gallery images rendered from the code in
this repository. It should not contain private source packs, copied journal
figures, courseware screenshots, encrypted MATLAB files, local workspace caches,
or hard-to-audit binary project files.

## What Can Be Added

- Original Python, MATLAB, Go, OriginPro, or LabTalk plotting templates.
- Synthetic demo data generated with a fixed random seed.
- Documentation written specifically for this library.
- Gallery images regenerated from the public templates.
- Small machine-readable metadata files such as `manifest.json`.

## What Must Stay Out

- `.p`, `.fig`, `.mat`, `.opj`, `.opju`, Office files, PDFs, archives, or other
  opaque source materials.
- Screenshots or scans from journals, books, paid courses, papers, or private
  folders.
- Files that contain private paths, email addresses, phone numbers, student
  numbers, watermarks, or school/person identifiers unrelated to the public
  project.
- Code copied from third-party projects unless the license is compatible and the
  attribution is kept intact.

## Review Checklist

Before a release:

1. Run `python scripts/check_publication_ready.py`.
2. Run `python scripts/build_manifest.py` after adding or removing templates.
3. Run `python -m pytest tests/`.
4. Run `python scripts/verify_all.py` when dependencies are available.
5. Check that gallery images are generated from public templates, not copied
   from outside sources.

## Local Resource Intake

Private local folders may be used only as inspiration for requirements, chart
types, or user needs. Public code should be rewritten from scratch using the
style and APIs of this repository.

When in doubt, write a new minimal template with synthetic data and document the
intended use case instead of importing an existing file.
