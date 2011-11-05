# revision 20843
# category Package
# catalog-ctan /macros/latex/contrib/lpic
# catalog-date 2010-12-23 21:19:38 +0100
# catalog-license lppl1.3
# catalog-version 0.8
Name:		texlive-lpic
Version:	0.8
Release:	1
Summary:	Put LaTeX material over included graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lpic
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lpic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lpic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package defines a convenient interface to put any LaTeX
material on top of included graphics. The LaTeX material may
also be rotated and typeset on top of a white box overshadowing
the graphics. The coordinates of the LaTeX boxes are given
relative to the original, unscaled graphics; when the graphics
is rescaled, the LaTeX annotations stay at their right places
(unless you do something extreme). In a draft mode, the package
enables you to draw a coordinate grid over the picture for easy
adjustment of positions of the annotations.

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
%{_texmfdistdir}/tex/latex/lpic/lpic.sty
%doc %{_texmfdistdir}/doc/latex/lpic/README
%doc %{_texmfdistdir}/doc/latex/lpic/instructions-differential.eps
%doc %{_texmfdistdir}/doc/latex/lpic/instructions-differential.pdf
%doc %{_texmfdistdir}/doc/latex/lpic/instructions.pdf
%doc %{_texmfdistdir}/doc/latex/lpic/instructions.tex
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
