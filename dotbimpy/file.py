import jsonpickle


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

    def save(self, path):
        if path[-4:] != ".bim":
            raise Exception("Path should end up with .bim extension")

        with open(path, "w") as bim_file:
            bim_file.write(jsonpickle.encode(self, indent=4, unpicklable=False))

    @staticmethod
    def read(path):
        if path[-4:] != ".bim":
            raise Exception("Path should end up with .bim extension")

        with open(path, "r") as bim_file:
            json_dictionary = jsonpickle.decode(bim_file.read())
            file = File.__convert_JSON_to_file(json_dictionary)

            return file

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
