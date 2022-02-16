class Element:
    def __init__(self, mesh_id, vector, rotation, guid, type, color, info):
        self.info = info
        self.color = color
        self.guid = guid
        self.rotation = rotation
        self.vector = vector
        self.type = type
        self.mesh_id = mesh_id
