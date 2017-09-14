from distutils.core import setup, Extension

module_dbr = Extension('dbr',
                        sources = ['dbr.c'], 
                        include_dirs=["/usr/local/lib/python2.7/dist-packages/numpy-1.11.2-py2.7-linux-x86_64.egg/numpy/core/include/numpy/"],
                        libraries=['DynamsoftBarcodeReader'])

setup (name = 'DynamsoftBarcodeReader',
        version = '1.0',
        description = 'Python barcode extension',
        ext_modules = [module_dbr])
