# dotbimpy (Version 0.0.7)

## Description

Open-source Python library for dotbim file format. Read more about dotbim here: https://github.com/paireks/dotbim

dotbim's website: https://dotbim.net/

Here you can find small manual for developers regarding development of tools that will work with .bim file format: https://github.com/paireks/dotbim/blob/master/DeveloperTips.md

## Installation

### Python

```cmd
pip install dotbimpy
```

### JupyterLab / Jupyter Notebooks

To display models inside notebooks additional steps are required, as displaying of models is based on plotly. Check out them there:
- JupyterLab: https://plotly.com/python/getting-started/#jupyterlab-support
- Jupyter Notebooks: https://plotly.com/python/getting-started/#jupyter-notebook-support

### Google colab

To use it in Google colab add this line at the beggining of the notebook:

```cmd
!pip install dotbimpy
```

## Examples

### Pyramid example

![2022-02-18_16h09_04](https://user-images.githubusercontent.com/47977819/154712470-aa4b5b44-3e23-4306-8a53-46d37494a52d.png)

```python
coordinates = [
    # Base
    0.0, 0.0, 0.0,
    10.0, 0.0, 0.0,
    10.0, 10.0, 0.0,
    0.0, 10.0, 0.0,

    # Top
    5.0, 5.0, 4.0
]

indices = [
    # Base faces
    0, 1, 2,
    0, 2, 3,

    # Side faces
    0, 1, 4,
    1, 2, 4,
    2, 3, 4,
    3, 0, 4
]

mesh = Mesh(mesh_id=0, coordinates=coordinates, indices=indices)
color = Color(r=255, g=255, b=0, a=255)
guid = "76e051c1-1bd7-44fc-8e2e-db2b64055068"
info = {"Name": "Pyramid"}
rotation = Rotation(qx=0, qy=0, qz=0, qw=1.0)
type = "Structure"
vector = Vector(x=0, y=0, z=0)
element = Element(mesh_id=0,
                  vector=vector,
                  guid=guid,
                  info=info,
                  rotation=rotation,
                  type=type,
                  color=color)

file_info = {
    "Author": "John Doe",
    "Date": "28.09.1999"
}

file = File("1.0.0", meshes=[mesh], elements=[element], info=file_info)
file.save("Pyramid.bim")
```

### 3 cubes example

![Cubes](https://user-images.githubusercontent.com/47977819/154802229-63284101-d12b-45eb-8b4a-ff7b4e8bdfe6.png)

```python
from dotbimpy import *


coordinates = [
    0.0, 0.0, 0.0,
    10.0, 0.0, 0.0,
    10.0, 0.0, 20.0,
    0.0, 0.0, 20.0,
    0.0, 30.0, 0.0,
    10.0, 30.0, 0.0,
    10.0, 30.0, 20.0,
    0.0, 30.0, 20.0
]

faces_ids = [
    # Front side
    0, 1, 2,
    0, 2, 3,

    # Bottom side
    0, 1, 4,
    1, 4, 5,

    # Left side
    0, 4, 3,
    4, 3, 7,

    # Right side
    1, 2, 5,
    2, 5, 6,

    # Top side
    2, 3, 7,
    2, 6, 7,

    # Back side
    4, 5, 7,
    5, 6, 7
]

mesh = Mesh(mesh_id=0, coordinates=coordinates, indices=faces_ids)

red_cube = Element(mesh_id=0,
                   color=Color(255, 0, 0, 255),
                   vector=Vector(x=-100.0, y=-100.0, z=-100.0),
                   rotation=Rotation(qx=0.0, qy=0.0, qz=0.0, qw=1.0),
                   guid="9f61b565-06a2-4bef-8b72-f37091ab54d6",
                   info={"Name": "Red Cube"},
                   type="Brick")

green_cube = Element(mesh_id=0,
                     color=Color(0, 255, 0, 126),
                     vector=Vector(x=-0.0, y=0.0, z=0.0),
                     rotation=Rotation(qx=0.0, qy=0.0, qz=0.0, qw=1.0),
                     guid="4d00c967-791a-42a6-a5e8-cf05831bc11d",
                     info={"Name": "Green Cube"},
                     type="Brick")

blue_cube = Element(mesh_id=0,
                    color=Color(0, 0, 255, 10),
                    vector=Vector(x=100.0, y=100.0, z=100.0),
                    rotation=Rotation(qx=0.0, qy=0.0, qz=0.0, qw=1.0),
                    guid="8501a5e3-4709-47d8-bd5d-33d745a435d5",
                    info={"Name": "Blue Cube"},
                    type="Brick")

file_info = {"Author": "John Doe"}

file = File(schema_version="1.0.0",
            meshes=[mesh],
            elements=[red_cube, green_cube, blue_cube],
            info=file_info)

file.save("Cubes.bim")
```

### Read file

```python
read_file = File.read("Pyramid.bim")
```

And then you can get all of the properties from it:

```python
version = read_file.schema_version
```

### View file

#### Default

If you want to view your file:

```python
file.view()
```
![2022-02-23_23h49_52](https://user-images.githubusercontent.com/47977819/155422920-9f0a9aa0-d3d6-442b-a0b0-084acb7e0ea7.png)

#### Customize

You can customize the plot that represents the .bim file. You can do it by using:

```python
figure = file.create_plotly_figure()
```

Then you get plotly's figure, which can be edited. E.g.

- adding text tag:

![2022-04-22_22h26_02](https://user-images.githubusercontent.com/47977819/164789418-fa632494-d0dd-4ad3-88de-7e4d14a2d8b3.png)

```python
from dotbimpy import *

bim_file = File.read(r"Teapot.bim")
figure = bim_file.create_plotly_figure()

figure.update_layout(
    scene=dict(
        annotations=[
            dict(
                showarrow=False,
                x=0,
                y=0,
                z=1.5,
                text="My Teapot!"
            )]
    ),
)

figure.show()
```

- combining model view with charts:

![image](https://user-images.githubusercontent.com/47977819/166078209-f2d381cd-00db-45a6-8539-23fc9ace32c4.png)

### Merge files

If you want to merge two files together:

```python
merged_file = file_a + file_b
```

### dotbimpy + trimesh

There is a wonderful library called trimesh: https://github.com/mikedh/trimesh, that has a lot of features regarding meshes. Because .bim files relies on meshes only, therefore you can find this library really helpful for many tasks related dotbim, like:

- converting dotbim's geometries from and to different file formats
- faster preview of .bim files: https://trimsh.org/trimesh.scene.html
- clash detection: https://trimsh.org/trimesh.collision.html?highlight=collision#module-trimesh.collision
![2022-04-07_23h32_50](https://user-images.githubusercontent.com/47977819/162323603-8d722656-dda9-4c7a-add9-b10142223b1d.png)
- convertion of .bim files to single separate .html file with the 3d model: https://trimsh.org/trimesh.viewer.html#trimesh.viewer.scene_to_html
![2022-04-13_19h35_29](https://user-images.githubusercontent.com/47977819/163238086-a866206b-3a76-4be9-b0d0-3930a380fd52.png)

Example notebook: https://github.com/paireks/dotbimpy/blob/master/dotbimpy/other/DotbimToTrimeshScene.ipynb

### dotbimpy + cadquery

Sometimes it's much easier to create B-REP and then convert it into mesh. For this purpose you can try cadquery: https://github.com/CadQuery/cadquery

Example notebook 1: https://github.com/paireks/dotbimpy/blob/master/dotbimpy/other/WallsWithBeams.ipynb

![2022-03-14_00h07_13](https://user-images.githubusercontent.com/47977819/158083248-5d2fb3c8-bf0f-439f-ae74-95035bc5cbff.png)

Example notebook 2: https://github.com/paireks/dotbimpy/blob/master/dotbimpy/other/Truss.ipynb

![2022-03-20_13h18_47](https://user-images.githubusercontent.com/47977819/159161776-a752df76-cd83-4bef-9404-8961f1043003.png)

## Libraries used

- For json serialization it uses jsonpickle: [Repo](https://github.com/jsonpickle/jsonpickle) [License](https://github.com/jsonpickle/jsonpickle/blob/main/LICENSE)
- For math is uses numpy: [Repo](https://github.com/numpy/numpy) [License](https://github.com/numpy/numpy/blob/main/LICENSE.txt)
- For quaternions it uses pyquaternion: [Repo](https://github.com/KieranWynn/pyquaternion) [License](https://github.com/KieranWynn/pyquaternion/blob/master/LICENSE.txt)
- For plotting it uses plotly: [Repo](https://github.com/plotly/plotly.py) [License](https://github.com/plotly/plotly.py/blob/master/LICENSE.txt)
