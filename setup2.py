from cx_Freeze import setup, Executable
import os

zip_includes = []
for include in ('hovercraft/templates', 'hovercraft/tests/test_data'):
    for dir, dirs, files in os.walk(include):
        for filename in files:
            zip_includes.append(os.path.join(dir, filename))
        
buildOptions = dict(packages = ['lxml', 'docutils', 'svg', 'pygments'], 
                    namespace_packages=['svg'],
                    zip_includes=zip_includes,
                    )

base = 'Console'

executables = [
    Executable('hovercraft/__main__.py', base=base, targetName='hovercraft.exe')
]

version = '1.2.dev0'

with open('README.rst', 'rt') as readme:
    description = readme.read()

with open('CHANGES.txt', 'rt') as changes:
    history = changes.read()

setup(name='hovercraft',
      version=version,
      description="Makes impress.js presentations from reStructuredText",
      long_description=description + '\n' + history,
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Topic :: Multimedia :: Graphics :: Presentation',
                   'Topic :: Text Processing',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
                   ], 
      keywords='presentations restructuredtext',
      author='Lennart Regebro',
      author_email='regebro@gmail.com',
      url='https://github.com/regebro/hovercraft',
      license='CC0 1.0 Universal',
      packages=['hovercraft', 'hovercraft.tests', 'hovercraft.tests.test_data'],
      options = dict(build_exe = buildOptions),
      executables = executables,
)

