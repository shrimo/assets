#!/usr/bin/python3

"""
A system for describing and managing assets for computer graphics.
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
        for element in self.elements:
            print('name: {n}, element: {e}'.format(n=element, e=self.elements[element]))

class ExternalFile:
    """ This is the element that stores the path to the file and its description """
    def __init__(self, name, file_path, file_type, info=None):
        self.name = name
        self.file_path = file_path
        self.file_type = file_type
        self.info = info


if __name__ == '__main__':
    scene01 = Scene('Scene01')

    asset01 = Asset('Asset 01')
    asset02 = Asset('Asset 02')

    image_file_01 = ExternalFile('flower', '/Image/rose-flower.jpeg', 'jpeg', 'Image file')
    image_file_02 = ExternalFile('flower01', '/Image/rose-flower.jpeg', 'jpeg', 'Image file01')

    asset01.append_element('image_file', image_file_01)
    asset02.append_element('image_file01', image_file_01)

    scene01.append_asset('Asset_01', asset01)
    scene01.append_asset('Asset_02', asset02)

    scene01.show_assets()

    test_asset01 = scene01.asset_by_name('Asset_01')    
    ifile = test_asset01.element_by_name('image_file')
    print(ifile.name, ifile.file_path)

    # test_asset02 = scene01.asset_by_name('Asset_02')
    # ifile2 = test_asset02.element_by_name('image_file')
    # print(ifile2.name, ifile2.file_path)



