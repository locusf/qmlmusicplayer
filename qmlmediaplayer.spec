# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       qmlmediaplayer

# >> macros
# << macros

Summary:    Nemo Mobile Music Player
Version:    2.0.0
Release:    1
Group:      Applications/Multimedia
License:    GPLv2
Source0:    %{name}-%{version}.tar.bz2
Source100:  qmlmediaplayer.yaml
Requires:   libqtdeclarative4 >= 4.7.0
Requires:   libqtsql4-sqlite
Requires:   libphonon4
Requires:   libqtopengl4
BuildRequires:  pkgconfig(QtDeclarative)
BuildRequires:  pkgconfig(phonon)
BuildRequires:  pkgconfig(QtOpenGL)
BuildRequires:  desktop-file-utils

%description
Music Player for Nemo Mobile


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
# >> files
/opt/qmlmediaplayer/bin/qmlmediaplayer
%{_datadir}/applications/qmlmediaplayer.desktop
%{_datadir}/pixmaps/qmlmediaplayer.png
# << files
