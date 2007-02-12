Summary:	Indeo 3.2 codec for XAnim
Summary(pl.UTF-8):	Kodek Indeo 3.2 dla XAnima
Name:		xanim-codec-iv32
Version:	2.1
Release:	1
License:	non-distributable, for use with xanim exclusively
Group:		X11/Applications/Graphics
# old dlls at http://xanim.polter.net/dlls/
Source1:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_iv32_2.1_linuxELFx86c6.tgz
# NoSource1-md5:	53e598a6c3fc1417db5ad03fc1dbaa10
Source2:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_iv32_2.1_linuxELFalphaC6.tgz
# NoSource2-md5:	5ca7b823b86d177e9d2b350137b99990
Source3:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_iv32_2.1_linuxELFppc.tgz
# NoSource3-md5:	2775ac5cec7f61408f055424caa2c131
NoSource:	1
NoSource:	2
NoSource:	3
URL:		http://xanim.polter.net/
Requires:	xanim >= 1:2920
ExclusiveArch:	%{ix86} alpha ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Intel Indeo 3.2 codec decompression DLL for XAnim.

%description -l pl.UTF-8
Biblioteka do dekompresji kodeka Intel Indeo 3.2 dla XAnima.

%prep
%ifarch %{ix86}
%setup -q -c -T -a1
%endif
%ifarch alpha
%setup -q -c -T -a2
%endif
%ifarch ppc
%setup -q -c -T -a3
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/xanim

install vid_iv32_*.xa $RPM_BUILD_ROOT%{_libdir}/xanim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc iv32.readme
%attr(755,root,root) %{_libdir}/xanim/vid_iv32_*.xa
