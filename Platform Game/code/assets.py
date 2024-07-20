from settings import *

def import_image(*path, format="png", alpha=True):
    full_path = join(*path) + f".{format}"
    surf = pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()
    return surf

def import_folder(*path):
    frames = []
    for folder_path, _, files_names in walk(join(*path)):
        for file_name in sorted(files_names, key= lambda name: int(name.split('.')[0])):
            full_path = join(folder_path, file_name)
            img_surf = pygame.image.load(full_path).convert_alpha()
            frames.append(img_surf)
    return frames