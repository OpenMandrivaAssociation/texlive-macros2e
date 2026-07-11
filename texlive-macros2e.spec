%global tl_name macros2e
%global tl_revision 77050

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4a
Release:	%{tl_revision}.1
Summary:	A list of internal LaTeX2e macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/macros2e
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/macros2e.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/macros2e.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This document lists the internal macros defined by the LaTeX2e base
files which can also be useful to package authors. The macros are hyper-
linked to their description in source2e. For this to work both PDFs must
be inside the same directory. This document is not yet complete in
content and format and may miss some macros.

