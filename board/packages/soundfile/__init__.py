from sampler import settings

FILES_PATH = settings.BASE_DIR + '/files'


def build_path(name):
    return FILES_PATH + '/' + name
