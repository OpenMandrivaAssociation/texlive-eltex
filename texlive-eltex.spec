# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/eltex
# catalog-date 2009-11-09 17:57:09 +0100
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-eltex
Version:	2.0
Release:	1
Summary:	Simple circuit diagrams in LaTeX picture mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eltex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eltex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eltex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The macros enable the user to draw simple circuit diagrams in
the picture environment, with no need of special resources. The
macros are appropriate for drawing for school materials. The
circuit symbols accord to the various parts of the standard IEC
617.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
