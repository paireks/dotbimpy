from pydantic import BaseModel, Field, model_validator


class Vector(BaseModel):
    x: float = Field(0.0, description="X component of the vector")
    y: float = Field(0.0, description="Y component of the vector")
    z: float = Field(0.0, description="Z component of the vector")

    def __init__(self, x=0.0, y=0.0, z=0.0):
        super().__init__(x=x, y=y, z=z)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False


class Rotation(BaseModel):
    qx: float = Field(0.0, description="X component of the quaternion")
    qy: float = Field(0.0, description="Y component of the quaternion")
    qz: float = Field(0.0, description="Z component of the quaternion")
    qw: float = Field(0.0, description="W component (scalar part) of the quaternion")

    def __init__(self, qx=0.0, qy=0.0, qz=0.0, qw=0.0):
        super().__init__(qx=qx, qy=qy, qz=qz, qw=qw)

    def __eq__(self, other):
        if isinstance(other, Rotation):
            return (
                self.qx == other.qx
                and self.qy == other.qy
                and self.qz == other.qz
                and self.qw == other.qw
            )
        return False


class Color(BaseModel):
    r: int = Field(0, ge=0, le=255, description="Red channel")
    g: int = Field(0, ge=0, le=255, description="Green channel")
    b: int = Field(0, ge=0, le=255, description="Blue channel")
    a: int = Field(0, ge=0, le=255, description="Alpha (opacity) channel")

    def __init__(self, r=0, g=0, b=0, a=0):
        super().__init__(r=r, g=g, b=b, a=a)

    def __eq__(self, other):
        if isinstance(other, Color):
            return (
                self.r == other.r
                and self.g == other.g
                and self.b == other.b
                and self.a == other.a
            )
        return False


class Mesh(BaseModel):
    mesh_id: int = Field(0, ge=0, description="Unique identifier for the mesh")
    coordinates: list[float] = Field(
        default_factory=list,
        description="Flat list of vertex coordinates [x1, y1, z1, x2, y2, z2, ...]",
    )
    indices: list[int] = Field(
        default_factory=list,
        description="Flat list of triangle vertex indices [i1, j1, k1, i2, j2, k2, ...]",
    )

    def __init__(self, mesh_id=0, coordinates=None, indices=None):
        super().__init__(
            mesh_id=mesh_id,
            coordinates=coordinates if coordinates is not None else [],
            indices=indices if indices is not None else [],
        )

    @model_validator(mode="after")
    def validate_mesh_geometry(self) -> "Mesh":
        if len(self.coordinates) % 3 != 0:
            raise ValueError(
                f"len(coordinates) must be divisible by 3, got {len(self.coordinates)}"
            )
        if len(self.indices) % 3 != 0:
            raise ValueError(
                f"len(indices) must be divisible by 3, got {len(self.indices)}"
            )
        num_vertices = len(self.coordinates) // 3
        if self.indices and num_vertices == 0:
            raise ValueError("Indices reference vertices but coordinates list is empty")
        if self.indices and num_vertices > 0:
            max_index = max(self.indices)
            if max_index >= num_vertices:
                raise ValueError(
                    f"Index {max_index} out of range for {num_vertices} vertices"
                )
        return self

    def validate(self) -> "Mesh":
        """Re-run all validators on current data. Raises ValueError if invalid."""
        return self.model_validate(self.model_dump())

    def __eq__(self, other):
        if isinstance(other, Mesh):
            return (
                self.mesh_id == other.mesh_id
                and self.coordinates == other.coordinates
                and self.indices == other.indices
            )
        return False

    def equals_without_mesh_id(self, other):
        if isinstance(other, Mesh):
            return (
                self.coordinates == other.coordinates and self.indices == other.indices
            )
        return False
