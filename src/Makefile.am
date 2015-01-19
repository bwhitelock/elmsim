SUBDIRS = elmDevice tkinter wxpython includes

bin_SCRIPTS = elmsim
CLEANFILES = $(bin_SCRIPTS) commandLineParse.pyc __init__.pyc
EXTRA_DIST = elmsim.in
DISTCLEANFILES = Makefile Makefile.in

elmsim_PYTHON = commandLineParse.py __init__.py
elmsimdir = $(ELMSIMDIR)/

uninstall-hook:
	if test -d ${ELMSIMDIR}/elmDevice; then rmdir ${ELMSIMDIR}/elmDevice; fi
	if test -d ${ELMSIMDIR}/tkinter; then rmdir ${ELMSIMDIR}/tkinter; fi
	if test -d ${ELMSIMDIR}/wxpython; then rmdir ${ELMSIMDIR}/wxpython; fi
	if test -d ${ELMSIMDIR}/includes; then rmdir ${ELMSIMDIR}/includes; fi
	if test -d ${ELMSIMDIR}; then rmdir ${ELMSIMDIR}; fi

do_substitution = sed -e 's,[@]pythondir[@],$(pythondir),g' \
	-e 's,[@]PACKAGE[@],$(PACKAGE),g' \
	-e 's,[@]VERSION[@],$(VERSION),g' \
	-e 's,[@]ELMSIMDIR[@],$(ELMSIMDIR),g' 

elmsim: elmsim.in Makefile
	$(do_substitution) < $(srcdir)/elmsim.in > elmsim
	chmod +x elmsim
