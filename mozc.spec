Name: mozc-git
Summary: A Japanese Input Method Editor (IME) designed for multi-platform
Version: 2.0.1
Release: 0%{?dist}
Group: Applications/Editors
License: BSD-3-Clause
URL: https://github.com/ciffelia/mozc-amzn2
BuildArch: x86_64

%description
Mozc is a Japanese Input Method Editor (IME) designed for multi-platform including GNU/Linux.
This package provides Mozc for Amazon Linux desktop environment.

%install
install -D --preserve-timestamps %{_sourcedir}/mozc_server                %{buildroot}/usr/lib/mozc/mozc_server
install -D --preserve-timestamps %{_sourcedir}/mozc_tool                  %{buildroot}/usr/lib/mozc/mozc_tool
install -D --preserve-timestamps %{_sourcedir}/mozc_renderer              %{buildroot}/usr/lib/mozc_renderer
install -D --preserve-timestamps %{_sourcedir}/ibus_mozc                  %{buildroot}/usr/lib/ibus-mozc/ibus-engine-mozc
install -D --preserve-timestamps %{_sourcedir}/mozc_emacs_helper          %{buildroot}/usr/bin/mozc_emacs_helper
install -D --preserve-timestamps %{_sourcedir}/product_icon_32bpp-128.png %{buildroot}/usr/share/ibus-mozc/product_icon.png
install -D --preserve-timestamps %{_sourcedir}/mozc.xml                   %{buildroot}/usr/share/ibus/component/mozc.xml

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root)
/usr/lib/mozc/mozc_server
/usr/lib/mozc/mozc_tool
/usr/lib/mozc_renderer
/usr/lib/ibus-mozc/ibus-engine-mozc
/usr/bin/mozc_emacs_helper
%defattr(0644,root,root)
/usr/share/ibus-mozc/product_icon.png
/usr/share/ibus/component/mozc.xml
