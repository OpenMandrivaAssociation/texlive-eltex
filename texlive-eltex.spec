# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/eltex
# catalog-date 2009-11-09 17:57:09 +0100
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-eltex
Version:	2.0
Release:	3
Summary:	Simple circuit diagrams in LaTeX picture mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eltex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eltex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eltex.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 751409
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 718324
- texlive-eltex
- texlive-eltex
- texlive-eltex
- texlive-eltex

