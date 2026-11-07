# Evidence schema

## Source record (`evidence/sources/SRC-*.json`)

Required: `id`, `title`, `type`, `url`, `retrieved_at`, `sha256`, `bytes`  
Optional: `final_url`, `content_type`, `notes`, `claim_use`

## Finding (`evidence/findings/FIND-*.json`)

Required: `id`, `title`, `claim_grade`, `severity`, `summary`, `evidence_ids`, `status`  
`claim_grade`: `Alleged` | `Documented` | `Verified`  
Publishable on the site only when `Documented` or `Verified`.
