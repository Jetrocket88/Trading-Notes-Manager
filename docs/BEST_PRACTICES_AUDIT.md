# Best Practices Audit

This audit highlights the highest-impact best-practice violations in the current codebase and how to fix each one.

## 1) Data model and form contract mismatch (critical correctness issue)

**Problem**
- The form stores the key `takeaway`, but the insert path expects `takeaways`, which can crash with `KeyError` or silently break data capture when the field naming changes in one place only.
- The database column is also named `bais` instead of `bias`, which increases long-term maintenance risk.

**Where**
- `src/main.py` (form key definition): `"takeaway"`
- `src/database.py` (insert expects): `data["takeaways"]`
- `src/database.py` (schema typo): `bais`

**Fix**
- Introduce a single source of truth for field names (e.g., constants/dataclass/Pydantic model).
- Rename schema column `bais` -> `bias` via migration.
- Align all UI keys and insert payload keys to one canonical naming convention.

## 2) Tight coupling between persistence and UI (critical architecture issue)

**Problem**
- `insertToDb` performs DB write and directly calls `messagebox`, making persistence non-reusable and hard to test.

**Where**
- `src/database.py`: `insertToDb` calls `messagebox.showinfo` and `messagebox.showerror`.

**Fix**
- Keep database layer pure: return success/failure (or raise typed exceptions).
- Move user messaging to the UI/controller layer (`main.py`).
- This separation enables unit testing DB logic without Tk dependencies.

## 3) Overly broad exception handling and error swallowing

**Problem**
- `helpers.screenRes()` catches all exceptions and only shows a message box, returning `None` implicitly; callers then assume width/height exist.

**Where**
- `src/helpers.py`: `except Exception as e` in `screenRes`.

**Fix**
- Catch only expected exceptions.
- Return a safe default `(width, height)` fallback if recovery is desired.
- Re-raise unexpected errors after logging context.

## 4) Input validation is incomplete for typed DB fields

**Problem**
- Required-field checks only validate non-empty strings, but `risk` and `rewardRatio` should be numeric and constrained.

**Where**
- `src/main.py`: `handleSubmitData` currently only checks empty values.
- `src/database.py`: schema expects `REAL NOT NULL`.

**Fix**
- Parse and validate `risk` and `rewardRatio` in UI/service before DB insert.
- Enforce sensible bounds (e.g., `risk > 0`, `rewardRatio >= 0`).
- Use uniform datetime validation for `entryDate`/`exitDate`.

## 5) Resource lifecycle and connection management inconsistency

**Problem**
- Some paths use context managers (`initDb`), while `insertToDb` uses manual connection handling.

**Where**
- `src/database.py`: manual `conn = connect()`/`finally: conn.close()` in `insertToDb`.

**Fix**
- Prefer `with connect() as conn:` everywhere.
- Keep transaction boundaries explicit and consistent.

## 6) Hard-coded UI positioning and magic numbers

**Problem**
- Popups are positioned with fixed coordinates (`+875+300`), which is fragile across resolutions/monitors.

**Where**
- `src/tinker.py`: `openPopup` and `openCalendarPopup` geometry setup.

**Fix**
- Use parent-relative centering (`setPopupOpenPosition`) or screen-aware calculations.
- Replace repeated literal values with named constants.

## 7) Naming/import hygiene problems that increase maintenance cost

**Problem**
- Unused import `from turtle import width`.
- Aliasing `import tinker as tk` in `helpers.py` is confusing next to `tkinter as tk` conventions.
- Mixed naming style (`camelCase` in Python module-level functions).

**Where**
- `src/tinker.py`, `src/helpers.py`, and multiple modules.

**Fix**
- Remove unused imports.
- Use explicit, unambiguous aliases (`import tinker` or `import tkinter as tk`).
- Adopt PEP 8 snake_case naming and run linting in CI (`ruff`/`flake8`).

---

## Recommended implementation order

1. **Fix schema/form naming mismatch first** (data correctness).
2. **Decouple DB and UI concerns** (testability).
3. **Add typed validation for numeric/datetime fields** (runtime safety).
4. **Normalize connection management** (reliability).
5. **Address UI magic numbers and style cleanup** (maintainability).
