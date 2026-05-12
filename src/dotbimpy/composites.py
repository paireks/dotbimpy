import json
from typing import Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field

from dotbimpy.primitives import Color, Mesh, Rotation, Vector


class Element(BaseModel):
    mesh_id: int = Field(0, ge=0, description="Reference to a Mesh by its mesh_id")
    color: Color = Field(default_factory=Color, description="RGBA color of the element")
    guid: UUID = Field(description="Globally unique identifier")
    rotation: Rotation = Field(
        default_factory=Rotation, description="Quaternion rotation applied to the mesh"
    )
    vector: Vector = Field(
        default_factory=Vector,
        description="Translation vector applied after rotation",
    )
    # TODO: KLS: "type" is keyword, maybe use "kind" instead?
    type: str = Field("", description="Element type (e.g. 'Beam', 'Column')")
    info: Dict[str, str] = Field(
        default_factory=dict, description="Element level metadata"
    )
    face_colors: Optional[List[int]] = Field(
        None,
        description="Per-face RGBA colors as flat list [r1,g1,b1,a1, r2,g2,b2,a2, ...]",
    )

    # TODO: KLS: "has_colors()" or "has_face_colors()" is more pythonic.
    def check_if_has_face_colors(
        self,
    ) -> bool:
        return self.face_colors is not None

    def __eq__(self, other):
        if not isinstance(other, Element):
            return False
        return (
            self.mesh_id == other.mesh_id
            and self.color == other.color
            and self.guid == other.guid
            and self.rotation == other.rotation
            and self.vector == other.vector
            and self.type == other.type
            and self.info == other.info
            and self.face_colors == other.face_colors
        )

    def equals_without_mesh_id(self, other):
        if not isinstance(other, Element):
            return False
        return (
            self.color == other.color
            and self.guid == other.guid
            and self.rotation == other.rotation
            and self.vector == other.vector
            and self.type == other.type
            and self.info == other.info
            and self.face_colors == other.face_colors
        )


class File(BaseModel):
    schema_version: str = Field("1.0.0", description="dotbim schema version")
    meshes: List[Mesh] = Field(
        default_factory=list, description="List of meshes in the file"
    )
    elements: List[Element] = Field(
        default_factory=list, description="List of elements referencing meshes"
    )
    info: Dict[str, str] = Field(
        default_factory=dict, description="File-level metadata"
    )

    def __init__(self, schema_version="1.0.0", meshes=None, elements=None, info=None):
        super().__init__(
            schema_version=schema_version,
            meshes=meshes if meshes is not None else [],
            elements=elements if elements is not None else [],
            info=info if info is not None else {},
        )

    def __eq__(self, other):
        if not isinstance(other, File):
            return False
        return (
            self.schema_version == other.schema_version
            and self.meshes == other.meshes
            and self.elements == other.elements
            and self.info == other.info
        )

    def __add__(self, other):
        if not isinstance(other, File):
            return NotImplemented

        new_meshes = [m.model_copy(deep=True) for m in self.meshes]
        new_elements = [e.model_copy(deep=True) for e in self.elements]

        max_mesh_id = max((m.mesh_id for m in self.meshes), default=-1)

        for m in other.meshes:
            new_id = m.mesh_id + max_mesh_id + 1
            copy = m.model_copy(deep=True, update={"mesh_id": new_id})
            new_meshes.append(copy)

        for e in other.elements:
            new_id = e.mesh_id + max_mesh_id + 1
            copy = e.model_copy(deep=True, update={"mesh_id": new_id})
            new_elements.append(copy)

        return File(
            schema_version=self.schema_version,
            meshes=new_meshes,
            elements=new_elements,
            info=self.info.copy(),
        )

    def save(self, path: str) -> None:
        if not path.endswith(".bim"):
            raise ValueError("Expected a path ending with '.bim'")

        with open(path, "w") as f:
            f.write(self.model_dump_json(indent=4, exclude_none=True, by_alias=True))

    @staticmethod
    def read(path: str) -> "File":
        if not path.endswith(".bim"):
            raise ValueError("Expected a path ending with '.bim'")

        with open(path, "r") as f:
            data = json.loads(f.read())

        return File.model_validate(data)
