import jsonpickle
import json
import plotly.graph_objects as go
import pyquaternion
import numpy as np
import copy


class File:
    def __init__(self, schema_version, meshes, elements, info):
        self.schema_version = schema_version
        self.meshes = meshes
        self.elements = elements
        self.info = info

    def __eq__(self, other):
        if not isinstance(other, File):
            return NotImplemented

        return self.schema_version == other.schema_version \
               and self.meshes == other.meshes \
               and self.elements == other.elements \
               and self.info == other.info

    def __add__(self, other):
        if not isinstance(other, File):
            return NotImplemented

        new_meshes = []
        new_elements = []
        new_schema_version = self.schema_version
        new_file_info = self.info.copy()

        max_mesh_id = 0
        for i in self.meshes:
            if max_mesh_id < i.mesh_id:
                max_mesh_id = i.mesh_id
            new_meshes.append(copy.deepcopy(i))

        for i in self.elements:
            new_elements.append(copy.deepcopy(i))

        for i in other.meshes:
            new_id = i.mesh_id + max_mesh_id + 1
            new_meshes.append(Mesh(new_id, i.coordinates.copy(), i.indices.copy()))

        for i in other.elements:
            new_id = i.mesh_id + max_mesh_id + 1
            new_elements.append(Element(mesh_id=new_id,
                                        color=copy.deepcopy(i.color),
                                        rotation=copy.deepcopy(i.rotation),
                                        vector=copy.deepcopy(i.vector),
                                        info=i.info.copy(),
                                        type=i.type,
                                        guid=i.guid))

        return File(schema_version=new_schema_version,
                    info=new_file_info,
                    meshes=new_meshes,
                    elements=new_elements)

    def save(self, path):
        if path[-4:] != ".bim":
            raise Exception("Path should end up with .bim extension")

        with open(path, "w") as bim_file:
            bim_file.write(jsonpickle.encode(self, indent=4, unpicklable=False))

    def view(self):
        geometries = []
        for i in self.elements:
            mesh = next((x for x in self.meshes if x.mesh_id == i.mesh_id), None)
            geometries.append(self.__convert_dotbim_mesh_to_plotly(mesh_to_convert=mesh, element=i))

        layout = go.Layout(scene=dict(aspectmode='data'))
        fig = go.Figure(data=[], layout=layout)
        for i in geometries:
            fig.add_trace(i)
        fig.show()

    @staticmethod
    def read(path):
        if path[-4:] != ".bim":
            raise Exception("Path should end up with .bim extension")

        with open(path, "r") as bim_file:
            json_dictionary = json.loads(bim_file.read())
            file = File.__convert_JSON_to_file(json_dictionary)

            return file

    @staticmethod
    def __convert_dotbim_mesh_to_plotly(mesh_to_convert, element):
        colorHex = '#%02x%02x%02x' % (element.color.r, element.color.g, element.color.b)
        opacity = element.color.a / 255

        x = []
        y = []
        z = []
        counter = 0
        while counter < len(mesh_to_convert.coordinates):
            point = np.array([
                mesh_to_convert.coordinates[counter],
                mesh_to_convert.coordinates[counter + 1],
                mesh_to_convert.coordinates[counter + 2]])

            rotation = pyquaternion.Quaternion(
                a=element.rotation.qw,
                b=element.rotation.qx,
                c=element.rotation.qy,
                d=element.rotation.qz)

            point_rotated = rotation.rotate(point)

            x.append(point_rotated[0] + element.vector.x)
            y.append(point_rotated[1] + element.vector.y)
            z.append(point_rotated[2] + element.vector.z)
            counter += 3

        i = []
        j = []
        k = []
        counter = 0
        while counter < len(mesh_to_convert.indices):
            i.append(mesh_to_convert.indices[counter])
            j.append(mesh_to_convert.indices[counter + 1])
            k.append(mesh_to_convert.indices[counter + 2])
            counter += 3

        return go.Mesh3d(x=x, y=y, z=z, i=i, j=j, k=k, color=colorHex, opacity=opacity, name=element.type,
                         showscale=True)

    @staticmethod
    def __convert_JSON_to_file(json_dictionary):

        schema_version = json_dictionary["schema_version"]
        elements = json_dictionary["elements"]
        meshes = json_dictionary["meshes"]
        created_info = json_dictionary["info"]

        created_meshes = []
        for i in meshes:
            created_meshes.append(Mesh(
                mesh_id=i["mesh_id"],
                coordinates=i["coordinates"],
                indices=i["indices"]
            ))

        created_elements = []
        for i in elements:
            created_elements.append(Element(
                mesh_id=i["mesh_id"],
                vector=Vector(x=i["vector"]["x"],
                              y=i["vector"]["y"],
                              z=i["vector"]["z"]),
                rotation=Rotation(qx=i["rotation"]["qx"],
                                  qy=i["rotation"]["qy"],
                                  qz=i["rotation"]["qz"],
                                  qw=i["rotation"]["qw"]),
                info=i["info"],
                color=Color(r=i["color"]["r"],
                            g=i["color"]["g"],
                            b=i["color"]["b"],
                            a=i["color"]["a"]),
                type=i["type"],
                guid=i["guid"]
            ))

        file = File(schema_version=schema_version, meshes=created_meshes, elements=created_elements, info=created_info)

        return file


class Element:
    def __init__(self, mesh_id, vector, rotation, guid, type, color, info):
        self.info = info
        self.color = color
        self.guid = guid
        self.rotation = rotation
        self.vector = vector
        self.type = type
        self.mesh_id = mesh_id

    def __eq__(self, other):
        if not isinstance(other, Element):
            return NotImplemented

        return self.info == other.info \
               and self.color == other.color \
               and self.guid == other.guid \
               and self.rotation == other.rotation \
               and self.vector == other.vector \
               and self.type == other.type \
               and self.mesh_id == other.mesh_id

    def equals_without_mesh_id(self, other):
        if not isinstance(other, Element):
            return NotImplemented

        return self.info == other.info \
               and self.color == other.color \
               and self.guid == other.guid \
               and self.rotation == other.rotation \
               and self.vector == other.vector \
               and self.type == other.type


class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __eq__(self, other):
        if not isinstance(other, Color):
            return NotImplemented

        return self.r == other.r and self.g == other.g and self.b == other.b and self.a == other.a


class Mesh:
    def __init__(self, mesh_id, coordinates, indices):
        self.mesh_id = mesh_id
        self.coordinates = coordinates
        self.indices = indices

    def __eq__(self, other):
        if not isinstance(other, Mesh):
            return NotImplemented

        return self.mesh_id == other.mesh_id and self.coordinates == other.coordinates and self.indices == other.indices

    def equals_without_mesh_id(self, other):
        if not isinstance(other, Mesh):
            return NotImplemented

        return self.coordinates == other.coordinates and self.indices == other.indices


class Rotation:
    def __init__(self, qx, qy, qz, qw):
        self.qx = qx
        self.qy = qy
        self.qz = qz
        self.qw = qw

    def __eq__(self, other):
        if not isinstance(other, Rotation):
            return NotImplemented

        return self.qx == other.qx and self.qy == other.qy and self.qz == other.qz and self.qw == other.qw


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return self.x == other.x and self.y == other.y and self.z == other.z
