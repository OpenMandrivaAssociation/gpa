Summary:	The GNU Privacy Assistant
Name:		gpa
Version:	0.9.3
Release:	2
License:	GPLv2+
Group:		File tools
URL:		http://wald.intevation.org/projects/gpa/
Source0:	ftp://ftp.gnupg.org/gcrypt/gpa/%{name}-%{version}.tar.bz2
BuildRequires:	gnupg
BuildRequires:	gpgme-devel >= 0.4.3
BuildRequires:	gtk+2-devel
BuildRequires:	libassuan-devel
BuildRequires:	gettext-devel
Requires:	gnupg

%description
The GNU Privacy Assistant is a graphical user interface for the
GNU Privacy Guard (GnuPG). GnuPG is a system that provides you with
privacy by encrypting emails or other documents and with
authentication of received files by signature management.

Install this package if you want to have an easy interface for GnuPG.

%prep
%setup -q

%build
%configure2_5x \
	--disable-rpath
%make

%install
%makeinstall_std

# menu entry
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/gpa
Icon=%{name}
Name=GNU Privacy Assistant
Comment=Graphical User Interface for GnuPG
Categories=GTK;System;
EOF

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README THANKS TODO
%{_bindir}/*
%{_datadir}/gpa
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/gpa.1.*


%changelog
* Tue Sep 11 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.3-1
+ Revision: 816773
- package man file
- fix docs
- update to new version 0.9.3
- drop patch 0, fixed by upstream
- spec file clean

* Sun Jul 24 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.0-4
+ Revision: 691422
- rebuild

* Sat Apr 02 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.0-3
+ Revision: 649826
- rebuild

* Mon Dec 06 2010 Funda Wang <fwang@mandriva.org> 0.9.0-2mdv2011.0
+ Revision: 612135
- br gettext-devel
- add upstream patch to build with assuan 2.0

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Thu Dec 10 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.0-1mdv2010.1
+ Revision: 476132
- update to new version 0.9.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Nov 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.0-1mdv2009.1
+ Revision: 300959
- update to new version 0.8.0
- add buildrequires on libassuan-devel

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.7.6-3mdv2009.0
+ Revision: 246529
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Dec 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.6-1mdv2008.1
+ Revision: 139673
- new version 0.7.6
- drop useless icons
- correct url and Source0
- fix desktop file
- new license policy
- do not package COPYING file
- fix file list
- nuke rpath

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Tue Aug 28 2007 Thierry Vignaud <tv@mandriva.org> 0.7.0-5mdv2008.0
+ Revision: 72269
- convert menu to XDG
- use %%mkrel


* Wed Apr 20 2005 Lenny Cartier <lenny@mandriva.com> 0.7.0-3mdk
- rebuild

* Wed Feb 11 2004 David Baudens <baudens@mandrakesoft.com> 0.7.0-2mdk
- Fix menu

* Sat Jan 24 2004 Abel Cheung <deaddog@deaddog.org> 0.7.0-1mdk
- 0.7.0
- Use bundled 48 icon, and hand-made 32/16 icons, as this icon is
  uncomprehensible in smaller sizes

* Thu Jan 16 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.4.3-2mdk
- rebuild

* Tue Jan 15 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.4.3-1mdk
- 0.4.3

* Wed Dec 26 2001 David BAUDENS <baudens@mandrakesoft.com> 0.4.2-2mdk
- Use default file tools icon for menu entry
- Add missing files

* Mon Dec 03 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4.2-1mdk
- 0.4.2

* Thu Nov 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4.1-3mdk
- rebuild

* Sun Apr 08 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.4.1-2mdk
- %%find_lang to get locales.
- Don't make /usr/share belong to the package.

* Sun Apr 08 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.4.1-1mdk
- Back in contribs built with a new and shiny source.
- s/I/j/ for the tar command during build.

* Mon Oct 02 2000 Daouda Lo <daouda@mandrakesoft.com> 0.3.1-6mdk
- add icons to menuentry

* Wed Sep 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-5mdk
- fix menu entry

* Fri Sep 01 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-4mdk
- added %%lang

* Wed Aug 02 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-3mdk
- add menu

* Wed Aug 02 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-2mdk
- fix requires

* Wed Jul 26 2000 Alexander Skwar <> 0.3.1-1mdk
- First Mandrake package

