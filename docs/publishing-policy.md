# Publishing Policy

This repository publishes cleaned, reusable skills. Local skills are source experience, not public artifacts.

## Public Criteria

A skill can be published here when it:

- has a clear user need
- has a complete `SKILL.md`
- has `skill.json`
- has at least one anonymized example input
- has expected output notes or a verification prompt
- works without private local paths
- does not require private account state to understand
- states what it does not do
- states when to stop for human judgment

## Language Policy

Public Skill runtime packages and ClawHub listings default to English. Apply the
rule to:

- `SKILL.md` frontmatter and instructions
- reader-facing `skill.json` values
- references, templates, examples, and runtime script messages
- ClawHub descriptions and creator hooks

The generated artifact may follow the user's requested language. Repository
documentation may have localized mirrors, including `README.zh-CN.md`; do not
bundle a second-language mirror into a public Skill merely for catalog
localization.

`config/public-skill-language.json` records temporary migration exceptions for
existing releases. Remove a Skill from that list and declare
`public_language: "en"` when it receives a material update. New public Skills
must use English unless the publishing policy records a deliberate exception.

## Do Not Publish

Do not publish:

- credentials or local configuration
- private account details
- private source repositories or local absolute paths
- real client, candidate, family, company, or private project material
- real content outputs unless they are intentionally public examples
- platform login automation that depends on an existing personal browser session
- after-sales, marketplace delivery, or private sales documents

## Migration Rule

Rewrite public skills from private-source experience. Do not copy private skills directly and then try to clean them afterward.

Preserve workflow shape, decision points, output contracts, reusable checks, and anonymized examples.

Remove or generalize private brand context, author-only identity, private file paths, private content archives, and external account assumptions.

## Third-party Inspiration

Third-party repositories can inspire structure and process. If code or skill text is adapted directly, preserve license requirements and add source attribution. The default approach is to re-express the workflow in this repository's own language.
