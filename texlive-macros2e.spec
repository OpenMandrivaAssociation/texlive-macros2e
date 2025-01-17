Name:		texlive-macros2e
Version:	64967
Release:	2
Summary:	A list of internal LaTeX2e macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/macros2e
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macros2e.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macros2e.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This document lists the internal macros defined by the LaTeX2e
base files which can be also useful to package authors. The
macros are hyper-linked to their description in source2e. For
this to work both PDFs must be inside the same directory. This
document is not yet complete in content and format and may miss
some macros.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/macros2e

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
