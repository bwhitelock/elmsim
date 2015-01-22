dnl Process this file with autoconf to produce a configure script.

AC_INIT([elmsim], [0.1])

AM_INIT_AUTOMAKE
AM_PATH_PYTHON([2.5])

AM_CHECK_PYMOD(serial,,,[AC_MSG_ERROR(Please install the pyserial module)])

AC_CONFIG_FILES([Makefile src/Makefile src/elmDevice/Makefile src/tkinter/Makefile src/wxpython/Makefile src/ecu/Makefile])

AS_AC_EXPAND(PYTHONDIR, $pythondir)
AS_AC_EXPAND(ELMSIMDIR, $pythondir/$PACKAGE)

AC_OUTPUT
