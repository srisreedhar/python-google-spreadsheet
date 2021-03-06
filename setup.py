from setuptools import setup, find_packages


version = '2.0.0'


setup(name='python-google-spreadsheet',
      version=version,
      description="A simple Python wrapper for the Google Spreadsheets API",
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: BSD License",
          ],
      keywords='google, docs, spreadsheets, api',
      author='Yoav Aviram',
      author_email='support@cleverblocks.com',
      url='https://github.com/yoavaviram/python-google-spreadsheet',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=["gdata"],
)
