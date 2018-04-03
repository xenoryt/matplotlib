:: This assumes you have installed all the dependencies via conda packages:
:: # create a new environment with the required packages
:: conda create -n "matplotlib_build" python=3.5 numpy python-dateutil pyparsing pytz tornado cycler tk libpng zlib freetype
:: activate matplotlib_build
:: if you want qt backend, you also have to install pyqt
:: conda install pyqt
:: # this package is only available in the conda-forge channel
:: conda install -c conda-forge msinttypes

set TARGET=bdist_wheel
IF [%1]==[] (
    echo Using default target: %TARGET%
) else (
    set TARGET=%1
    echo Using user supplied target: %TARGET%
)

IF NOT DEFINED CONDA_PREFIX (
    echo No Conda env activated: you need to create a conda env with the right packages and activate it!
    GOTO:eof
)

:: copy the libs which have "wrong" names
set LIBRARY_LIB=%CONDA_PREFIX%\Library\lib
mkdir lib || cmd /c "exit /b 0"
copy %LIBRARY_LIB%\zlibstatic.lib lib\z.lib
copy %LIBRARY_LIB%\libpng_static.lib lib\png.lib

:: Make the header files and the rest of the static libs available during the build
:: CONDA_PREFIX is a env variable which is set to the currently active environment path
set MPLBASEDIRLIST=%CONDA_PREFIX%\Library\;.

:: build the target
python setup.py %TARGET%
