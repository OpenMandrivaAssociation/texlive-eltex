Name:		texlive-eltex
Version:	15878
Release:	2
Summary:	Simple circuit diagrams in LaTeX picture mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eltex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eltex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eltex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The macros enable the user to draw simple circuit diagrams in
the picture environment, with no need of special resources. The
macros are appropriate for drawing for school materials. The
circuit symbols accord to the various parts of the standard IEC
617.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eltex/eltex1.tex
%{_texmfdistdir}/tex/latex/eltex/eltex2.tex
%{_texmfdistdir}/tex/latex/eltex/eltex3.tex
%{_texmfdistdir}/tex/latex/eltex/eltex4.tex
%{_texmfdistdir}/tex/latex/eltex/eltex5.tex
%{_texmfdistdir}/tex/latex/eltex/eltex6.tex
%{_texmfdistdir}/tex/latex/eltex/eltex7.tex
%doc %{_texmfdistdir}/doc/latex/eltex/README
%doc %{_texmfdistdir}/doc/latex/eltex/man_en.pdf
%doc %{_texmfdistdir}/doc/latex/eltex/man_en.tex
%doc %{_texmfdistdir}/doc/latex/eltex/pri_cz.pdf
%doc %{_texmfdistdir}/doc/latex/eltex/pri_cz.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
