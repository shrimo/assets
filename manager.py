#!/usr/bin/python3

"""
A system for describing and managing assets for computer graphics.

Each scene (shot or sequence) consists of assets that contain elements. 
Elements are geometry, materials, textures, image files, data files, etc.
"""

import uuid

class Scene:
    """ This is a scene, it contains a assets """
    def __init__(self, name):
        self.name = name
        self.assets = {}

    def append_asset(self, name, asset):
        self.assets[name] = asset

    def remove_asset(self, name):
        if name in self.assets:
            del self.assets[name]

    def asset_by_name(self, name):
        if name in self.assets:
            return self.assets[name]

    def show_assets(self):
        print('Scene:', self.name)
        for asset in self.assets:
            print('name: {n}, asset: {a}'.format(n=asset, a=self.assets[asset]))


class Asset:
    """ This is a asset, it contains a elements """
    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4()
        self.elements = {}

    def append_element(self, name, element):
        self.elements[name] = element

    def remove_element(self, name):
        if name in self.elements:
            del self.elements[name]

    def element_by_name(self, name):
        if name in self.elements:
            return self.elements[name]

    def show_elements(self):
        print('Asset:', self.name)
        for element in self.elements:
            print('name: {n}, element: {e}'.format(n=element, e=self.elements[element]))

class ExternalFile:
    """ This is the element that stores the path to the file and its description """
    def __init__(self, name, file_path, file_type, info=None):
        self.name = name
        self.file_path = file_path
        self.file_type = file_type
        self.info = info

class Camera:
    """ focal length, horiz aperture, vert aperture, focal distance, frame rate, etc """
    def __init__(self, name, focal=50, horiz=24, vert=18):
        self.name = name
        self.focal = focal
        self.horiz = horiz
        self.vert = vert

class PBRMaterial:
    """ Albedo, Metallic, Roughness, Normal, Opacity, Occlusion, Emissive, Scattering """
    def __init__(self, name, color, metallic, roug, normal, opacity, occlusion, emissive, sss):
        self.name = name
        self.color = color
        self.metallic = metallic
        self.roug = roug
        self.normal = normal
        self.opacity = opacity
        self.occlusion = occlusion
        self.emissive = emissive
        self.sss = sss

if __name__ == '__main__':
    scene01 = Scene('Scene01')

    asset01 = Asset('Asset 01')
    asset02 = Asset('Asset 02')
    asset03 = Asset('Asset 03')

    image_file_01 = ExternalFile('flower01', '/Image/rose-flower.jpeg', 'jpeg', 'Image file')
    image_file_02 = ExternalFile('flower02', '/Image/rose-flower.jpeg', 'jpeg', 'Image file01')

    mat01 = PBRMaterial('mat_01', 'rgb_file', 0.1, 0.1, 'bump_file', 0.1, 0.1, 'rgb_file', 0.1)

    cam01 = Camera('camera01')

    asset01.append_element('image_file01', image_file_01)
    asset01.append_element('mat01', mat01)
    asset01.append_element('cam01', cam01)
    asset01.show_elements()

    asset02.append_element('image_file02', image_file_02)
    asset02.append_element('mat01', mat01)
    asset02.append_element('cam01', cam01)
    asset02.show_elements()

    asset03.append_element('cam01', cam01)
    asset03.show_elements()

    scene01.append_asset('Asset_01', asset01)
    scene01.append_asset('Asset_02', asset02)
    scene01.append_asset('Asset_03', asset03)

    scene01.show_assets()

    test_asset01 = scene01.asset_by_name('Asset_01')    
    ifile = test_asset01.element_by_name('image_file01')
    print(ifile.name, ifile.file_path)

    test_asset02 = scene01.asset_by_name('Asset_02')
    ifile2 = test_asset02.element_by_name('image_file02')
    print(ifile2.name, ifile2.file_path)
