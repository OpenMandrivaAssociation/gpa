Summary:	The GNU Privacy Assistant
Name:		gpa
Version:	0.7.0
Release:	%mkrel 5
License:	GPL
URL:		http://www.gnupg.org/related_software/gpa/
Group:		File tools

Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/%{name}/%{name}-%{version}.tar.gz
Source1:	%{SOURCE0}.sig
Source10:	%{name}-32.png
Source11:	%{name}-16.png

BuildRequires:	gnupg
BuildRequires:	gpgme-devel >= 0.4.3
BuildRequires:	gtk+2-devel
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
%configure2_5x
%make

%install
rm -fr %{buildroot}

%makeinstall_std

# menu entry
mkdir -p %buildroot%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/gpa 
Icon=%{name}.png 
Name=GNU Privacy Assistant 
Comment=Graphical User Interface for GnuPG 
Categories=Utility;System;
EOF

# icons
install -D -m 0644 gpa-logo-48x48.png %{buildroot}%{_liconsdir}/%{name}.png
install -D -m 0644 %{SOURCE10}        %{buildroot}%{_iconsdir}/%{name}.png
install -D -m 0644 %{SOURCE11}        %{buildroot}%{_miconsdir}/%{name}.png

%find_lang %{name}

%post
%update_menus
 
%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README README-alpha THANKS TODO
%{_bindir}/*
%{_datadir}/gpa

%{_datadir}/applications/mandriva-*.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

