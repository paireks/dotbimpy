# Changelog

## [Unreleased]

### Breaking Changes

- **All classes are now Pydantic `BaseModel` subclasses.** `Color`, `Vector`, `Rotation`, `Mesh`,
  `Element`, and `File` no longer use plain `__init__`. Constructors now enforce type validation
  and will raise `pydantic.ValidationError` on invalid input.

- **`__eq__` methods return `False` instead of `NotImplemented`** when comparing with incompatible
  types. Code that checked `obj.__eq__(x) is NotImplemented` must be updated to `== False`.

- **`Element.guid` is now `uuid.UUID`**, not `str`. Pydantic coerces valid UUID strings on input,
  but arbitrary non-UUID strings will be rejected with a `ValidationError`.

- **`Element.face_colors` is now `Optional[List[int]]` (default `None`)** instead of a
  conditionally-set attribute. Code that used `hasattr(element, 'face_colors')` should use
  `element.face_colors is not None` or `element.check_if_has_face_colors()`.

- **`Element.info` and `File.info` are now `Dict[str, str]`** instead of untyped `dict`.
  Non-string keys or values will be rejected.

- **`Color` channels are `int` (0–255)**, matching the original. The previous intermediate
  rewrite briefly used `float` (0.0–1.0); this has been reverted to match the `.bim` spec.

- **`Mesh` validates geometry on construction.** `len(coordinates)` must be divisible by 3,
  `len(indices)` must be divisible by 3, and all index values must reference valid vertices.
  Previously invalid meshes were silently accepted.

- **`File.save()` and `File.read()` raise `ValueError`** instead of generic `Exception`
  for invalid file extensions.

- **Serialization uses Pydantic instead of `jsonpickle`.** `File.save()` now calls
  `model_dump_json(exclude_none=True)`. `File.read()` uses `File.model_validate()`.
  JSON output is structurally identical but field ordering may differ.

- **`requires-python` raised to `>=3.11`** (was `>=3.6`).

### Changed

- Migrated all classes to Pydantic `BaseModel` with typed, validated fields.

- Replaced `setup.py` / `setup.cfg` / `MANIFEST` with `pyproject.toml` using `hatchling`
  build backend.

- Package management moved from pip to uv.

- `jsonpickle` removed as a dependency; `pydantic>=2.0` added.

- `File.__add__()` uses `model_copy(deep=True)` instead of `copy.deepcopy`.

- Source split into `primitives.py` (Color, Vector, Rotation, Mesh) and
  `composites.py` (Element, File). All classes re-exported from `dotbimpy.__init__`.
