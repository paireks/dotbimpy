from distutils.core import setup
setup(
  name='dotbimpy',
  packages=['dotbimpy'],
  version='0.0.1',
  license='MIT',
  description='Python library for dotbim',
  author='Wojciech',
  author_email='w.radaczynski@gmail.com',
  url='https://github.com/paireks/dotbimpy',
  download_url='https://github.com/paireks/dotbimpy/archive/refs/tags/v_0_0_1.tar.gz',
  keywords=[],
  install_requires=[
          'jsonpickle',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
)