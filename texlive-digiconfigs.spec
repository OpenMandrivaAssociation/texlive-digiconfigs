%global tl_name digiconfigs
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Writing configurations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/digiconfigs
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/digiconfigs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/digiconfigs.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
In Stochastic Geometry and Digital Image Analysis some problems can be
solved in terms of so-called "configurations". A configuration is
basically a square matrix of \circ and \bullet symbols. This package
provides a convenient and compact mechanism for displaying these
configurations.

