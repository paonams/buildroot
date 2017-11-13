Summary: A library for interfacing IEEE 1284-compatible devices.
Name: libieee1284
Version: 0.2.11
Release: 0.1
License: GPL
Group: System Environment/Libraries
URL: http://cyberelk.net/tim/libieee1284/
Source0: ftp://cyberelk.net/tim/data/%{name}/devel/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: xmlto, python-devel

%description
The libieee1284 library is for communicating with parallel port devices.

%package devel
Summary: Files for developing applications that use libieee1284.
Requires: %{name} = %{version}
Group: Development/Libraries

%description devel
The header files, static library, libtool library and man pages for
developing applications that use libieee1284.

%package python
Summary: Python extension module for libieee1284.
Group: System Environment/Libraries

%description python
Python extension module for libieee1284.  To use libieee1284 with Python,
use 'import ieee1284'.

%prep
%setup -q

%build
%configure
make CFLAGS="$RPM_OPT_FLAGS"
# Also make the documentation in PDF format
make doc/interface.pdf

%install
rm -rf %{buildroot}
%makeinstall
rm -f %{buildroot}%{_libdir}/python*/*/*a

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING TODO
%{_libdir}/*.so.*
%{_bindir}/*

%files devel
%defattr(-,root,root)
%doc doc/interface.pdf
%{_includedir}/ieee1284.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.la
%{_mandir}/*/*

%files python
%defattr(-,root,root)
%{_libdir}/python*/*/*.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Tue Feb  3 2004 Tim Waugh <twaugh@redhat.com>
- Build requires python-devel.
- Ship Python extension module.

* Wed Feb 26 2003 Tim Waugh <twaugh@redhat.com>
- Use the Makefile rule to build the PDF.

* Sat Aug 24 2002 Tim Waugh <twaugh@redhat.com>
- Ship test program.

* Sat Aug  3 2002 Tim Waugh <twaugh@redhat.com>
- The archive is now distributed in .tar.bz2 format.

* Fri Apr 26 2002 Tim Waugh <twaugh@redhat.com>
- No need to create man page symlinks any more.
- Build requires xmlto now, not docbook-utils.

* Wed Apr 24 2002 Tim Waugh <twaugh@redhat.com>
- The tarball builds its own man pages now; just adjust the symlinks.
- Run ldconfig.

* Mon Jan  7 2002 Tim Waugh <twaugh@redhat.com>
- Ship the PDF file with the devel package.

* Thu Nov 15 2001 Tim Waugh <twaugh@redhat.com>
- Initial specfile.
