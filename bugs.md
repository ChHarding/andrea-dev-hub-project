# Bug Sheet

Track known issues here as you encounter them. For each bug, note how it
happened so it can be reproduced and fixed later.

## Open bugs
_(none yet)_

## Fixed bugs
- **Review note always asked for both items.** In Version 1 the "Needs Information" note always said "review the API guide and provide a technical contact", even if only one answer was "no". Fixed in Version 2: `suggest_review_note()` only mentions what is actually missing.
- **App only worked when started from the project folder.** Running `python main.py` from another folder failed because `data/` paths were relative. Fixed in Version 2: paths are built from `__file__` in `hub_logic.py`.
- **Ctrl+C / closed input crashed the CLI with a traceback.** Fixed: `main.py` now catches `KeyboardInterrupt`/`EOFError` and says goodbye.
