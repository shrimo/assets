import os
from pathlib import Path

class Scene:
    """ This is a scene, it contains a assets """
    def __init__(self, name, scene_path):
        self.name = name
        self.path_object = Path(scene_path)
        self.assets = {}
        self.extension=['.cdl', '.cube', '.json']
        self.assets_mask = 'publish'
        self.directory_processing()
        self.data_to_asset()

    def remove_asset(self, name):
        if name in self.assets:
            del self.assets[name]

    def component_from_asset(self, name, component='.cdl'):
        if name in self.assets:
            return self.assets[name]['asset'][component]

    def show_assets(self):
        print('Scene:', self.name)
        for asset in self.assets:
            print('name: {n}, asset: {a}'.format(n=asset, a=self.assets[asset]['asset']))

    def add_shots(self, components):
        self.assets[components[5]] = {'data':[], 'asset':{}}

    def directory_processing(self):
        tmp_assets_list = []
        for file_path in self.path_object.rglob('*'):
            if file_path.is_file():
                if file_path.suffix in self.extension:
                    list_components = os.path.normpath(file_path).split(os.path.sep)
                    self.add_shots(list_components)
                    if self.assets_mask in list_components:
                        tmp_assets_list.append((file_path.suffix, file_path, list_components[5]))

        for asset in tmp_assets_list:
            if asset[2] in self.assets.keys():
                self.assets[asset[2]]['data'].append((asset[0], asset[1]))

    def data_to_asset(self):
        for k in self.assets:
            self.assets[k]['asset'] = {
                self.assets[k]['data'][0][0]:self.assets[k]['data'][0][1], 
                self.assets[k]['data'][1][0]:self.assets[k]['data'][1][1],
                self.assets[k]['data'][2][0]:self.assets[k]['data'][2][1]}


if __name__ == '__main__':
    dir_path = '/home/mo/vfx/DCM'
    dcm_scene = Scene('DCM', dir_path)
    # dcm_scene.show_assets()
    a = dcm_scene.component_from_asset('TD_106_036_020', '.json')
    print(a)
    

