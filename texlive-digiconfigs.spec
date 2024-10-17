Name:		texlive-digiconfigs
Version:	15878
Release:	2
Summary:	Writing "configurations"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/digiconfigs
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/digiconfigs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/digiconfigs.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In Stochastic Geometry and Digital Image Analysis some problems
can be solved in terms of so-called "configurations". A
configuration is basically a square matrix of \circ and \bullet
symbols. This package provides a convenient and compact
mechanism for displaying these configurations.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/digiconfigs/digiconfigs.sty
%doc %{_texmfdistdir}/doc/latex/digiconfigs/README
%doc %{_texmfdistdir}/doc/latex/digiconfigs/digiconfigs.pdf
%doc %{_texmfdistdir}/doc/latex/digiconfigs/digiconfigs.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
