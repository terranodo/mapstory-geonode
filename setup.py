from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os
import sys

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
mapstory_dir = 'mapstory'

for dirpath, dirnames, filenames in os.walk(mapstory_dir):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

setup(name='MapStory',
      version="0.1",
      description="MapStory, based on GeoNode",
      ong_description=(read('README.md')),
      classifiers=[
        "Development Status :: 4 - Beta"],
      keywords='',
      author='MapStory Developers',
      author_email='admin@mapstory.org',
      url='http://mapstory.org',
      license='GPL',
      packages=packages,
      data_files=data_files,
      install_requires=[
          'docutils',
          'textile',
          # dev dependencies
          'dj.paste',
          'PasteDeploy',
          'django-haystack==2.4.0',
          'elasticsearch==1.6.0',
          'django-slack==4.1.0',
          #specific dependency versions from mapstory v1 to support oauth and social authnz
          'django-oauth2-provider==0.2.6.1',
          'django-social-auth==0.7.22',
          'oauth2==1.5.211',
          #AWS S3 dependencies
          'django-storages==1.1.8',
          'boto==2.38.0',
          #threaded comments dependencies
          'django-threadedcomments==1.0.1',
          'django-fluent-comments==1.0.5'
        ],
      zip_safe=False,
      )