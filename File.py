import jsonpickle


class File:
    def __init__(self, schema_version, meshes, elements, info):
        self.schema_version = schema_version
        self.meshes = meshes
        self.elements = elements
        self.info = info

    def save(self, path):
        if path[-4:] != ".bim":
            raise Exception("Path should end up with .bim extension")

        with open(path, "w") as bim_file:
            bim_file.write(jsonpickle.encode(self, unpicklable=False, indent=4))
