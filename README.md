# Linux Barcode SDK Wrapper for Python
Build the **Python** extension with Dynamsoft Barcode Reader SDK for Linux. 

## Environment
* Python 2.7
* Ubuntu 14.0
* Dynamsoft Barcode SDK 5.2. Please contact support@dynamsoft.com to get the beta version and trial license.

## How to Build the Extension 
1. Create symlink for libDynamsoftBarcodeReaderx64.so:

    ```
    sudo ln -s <Your PATH>/libDynamsoftBarcodeReaderx64.so /usr/lib/libDynamsoftBarcodeReader.so
    ```

2. Download [Numpy 1.11.2](https://sourceforge.net/projects/numpy/files/). 
3. Install **Numpy**:

    ```
    cd numpy-1.11.2
    sudo python setup.py build install
    ```

4. Add the path of Numpy header files into **setup.py**. For example:

    ```
    include_dirs=["/usr/local/lib/python2.7/dist-packages/numpy-1.11.2-py2.7-linux-x86_64.egg/numpy/core/include/numpy/"],
    ``` 

5. Build the extension:

    ```
    sudo setup.py build install
    ```

6. Run the test app:

    ```
    python test.py
    ```
    ![camera list in Python](screenshot/linux-python-barcode-reader.PNG)

## Blog
[Building Python Barcode Extension with DBR 5.2 for Linux](http://www.codepool.biz/build-linux-python-barcode-extension.html)
