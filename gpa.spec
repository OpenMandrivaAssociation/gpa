Summary:	The GNU Privacy Assistant
Name:		gpa
Version:	0.7.6
Release:	%mkrel 3
License:	GPLv2+
Group:		File tools
URL:		http://wald.intevation.org/projects/gpa/
Source0:	http://wald.intevation.org/frs/download.php/350/%{name}-%{version}.tar.bz2
Source1:	%{SOURCE0}.sig
BuildRequires:	gnupg
BuildRequires:	gpgme-devel >= 0.4.3
BuildRequires:	gtk+2-devel
Requires:	gnupg
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -fr %{buildroot}
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

%if %mdkversion < 200900
%post
%{update_menus}
%endif
 
%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README README-alpha THANKS TODO
%{_bindir}/*
%{_datadir}/gpa
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png
