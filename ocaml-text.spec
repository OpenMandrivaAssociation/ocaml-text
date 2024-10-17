%define debug_package %{nil}
%define versionbase 0.5
#define releasecandidate rc5
#define versioncomplete %{versionbase}-%{releasecandidate}
%define versioncomplete %{versionbase}

Name:           ocaml-text
Version:        %{versionbase}
Release:        3
Summary:        OCaml Text helpers
Group:          Development/Other
License:        GPLv2
URL:            https://forge.ocamlcore.org/projects/ocaml-text/
Source0:	http://forge.ocamlcore.org/frs/download.php/641/%{name}-%{version}.tar.gz
BuildRequires:  ocaml >= 3.10.0
BuildRequires:	camlp4
BuildRequires:  ocaml-findlib-devel
BuildRequires:	ocaml-pcre
BuildRequires:  ocaml-doc
BuildRequires:	pkgconfig(ncurses)

%global __ocaml_requires_opts -i Ast_c -i Token_c -i Type_cocci -i Ast_cocci -i Common -i Oassocb -i ANSITerminal -i Oseti -i Sexplib -i Oassoch -i Setb -i Oassoc_buffer -i Ograph2way -i SetPt -i Mapb -i Dumper -i Osetb -i Flag


%description
Caml-Text is a library for dealing with ``text'', i.e. sequence of
unicode characters, in a convenient way.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package doc
Summary:        Documentation for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description doc
The %{name}-doc package contains documentation for %{name}.

%files
%dir %{_libdir}/ocaml/text
%{_libdir}/ocaml/text/META
%{_libdir}/ocaml/text/*.cma
%{_libdir}/ocaml/text/*.cmi

%files doc
%doc LICENSE CHANGES CHANGES.darcs README

%files devel
%{_libdir}/ocaml/text/*.a
%{_libdir}/ocaml/text/*.cmxa
%{_libdir}/ocaml/text/*.mli
%{_libdir}/ocaml/stublibs/*.so*

%prep
%setup -q -n %{name}-%{version}

%build
ocaml setup.ml -configure --prefix %{_prefix} --destdir '%{buildroot}' --enable-pcre --docdir %{_docdir}/%{name}-doc/
make
make doc

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install



%changelog
* Fri Sep 16 2011 Alexandre Lissy <alissy@mandriva.com> 0.5-1
+ Revision: 699997
- Adding missing BuildRequires against libncurses-devel
- Update description field
- Importing ocaml-text package
- Created package structure for 'ocaml-text'.

