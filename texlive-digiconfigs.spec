# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/digiconfigs
# catalog-date 2007-03-05 22:02:45 +0100
# catalog-license lppl
# catalog-version 0.5
Name:		texlive-digiconfigs
Version:	0.5
Release:	4
Summary:	Writing "configurations"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/digiconfigs
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/digiconfigs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/digiconfigs.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5-2
+ Revision: 750957
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.5-1
+ Revision: 718230
- texlive-digiconfigs
- texlive-digiconfigs
- texlive-digiconfigs
- texlive-digiconfigs

