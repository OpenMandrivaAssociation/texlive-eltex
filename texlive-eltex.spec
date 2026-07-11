%global tl_name eltex
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Simple circuit diagrams in LaTeX picture mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eltex
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eltex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eltex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The macros enable the user to draw simple circuit diagrams in the
picture environment, with no need of special resources. The macros are
appropriate for drawing for school materials. The circuit symbols accord
to the various parts of the standard IEC 617.

