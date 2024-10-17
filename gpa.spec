Summary:	The GNU Privacy Assistant
Name:		gpa
Version:	0.10.0
Release:	2
License:	GPLv2+
Group:		File tools
URL:		https://wald.intevation.org/projects/gpa/
Source0:	https://gnupg.org/ftp/gcrypt/gpa/%{name}-%{version}.tar.bz2
BuildRequires:	gnupg
BuildRequires:	gpgme-devel >= 0.4.3
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	libassuan-devel
BuildRequires:	gettext-devel
BuildSystem:	autotools
Requires:	gnupg

%patchlist
gpa-0.10.0-libassuan-3.0.patch

%description
The GNU Privacy Assistant is a graphical user interface for the
GNU Privacy Guard (GnuPG). GnuPG is a system that provides you with
privacy by encrypting emails or other documents and with
authentication of received files by signature management.

Install this package if you want to have an easy interface for GnuPG.

%prep -a
autoconf

%install -a
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

%find_lang %{name} --with-man

%files -f %{name}.lang
%doc AUTHORS README THANKS TODO
%{_bindir}/*
%{_datadir}/gpa
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/gpa.1*
