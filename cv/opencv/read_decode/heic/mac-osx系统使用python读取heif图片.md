```bash
# 安装所需依赖
brew install libffi libheif

# 安装python库
pip install pyheif
pip install whatimage
```



```bash
(py37_urs) ➜  src git:(zxdev_multi_type) ✗ brew install libffi libheif
==> Downloading https://homebrew.bintray.com/bottles/libffi-3.3.catalina.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libffi-3.3.catalina.bottle.tar.gz
==> Caveats
libffi is keg-only, which means it was not symlinked into /usr/local,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

For compilers to find libffi you may need to set:
  export LDFLAGS="-L/usr/local/opt/libffi/lib"
  export CPPFLAGS="-I/usr/local/opt/libffi/include"

==> Summary
🍺  /usr/local/Cellar/libffi/3.3: 16 files, 489.4KB
==> Downloading https://homebrew.bintray.com/bottles/jpeg-9d.catalina.bottle.tar.gz
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/8f7b82a952fb3937889c7f22da1403e5338cd320495917eb26b0c5b2e614791c?response-content-disp
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/libde265-1.0.8.catalina.bottle.tar.gz
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/774fe5c9c849784aa10648fe3fae971c7d702a47807b6954c8a8763368bce9fc?response-content-disp
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/libpng-1.6.37.catalina.bottle.tar.gz
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/c8e74da602c21f978cd7ee3d489979b4fc6681e71f678a1d99012943ee3a909f?response-content-disp
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/pcre-8.44.catalina.bottle.tar.gz
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/f8ac266e04f984fa55091a43f0fdc39a40d57c2489d289a186c88ccedaba7eeb?response-content-disp
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/glib-2.66.4.catalina.bottle.tar.gz
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/65d130d343e12482908e6faa372af3c80dbcd5d02652cab648282a733c5e4f93?response-content-disp
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/docbook-5.1_1.catalina.bottle.tar.gz
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/8152e5356c47a7b8282f3ed84ee3f29565e8ce620bddeaeaf23dfd1f5ef111a3?response-content-disp
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/docbook-xsl-1.79.2_1.catalina.bottle.tar.gz
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/65a5442556a88a865ef377cb73df0b3edf9ab2240e6f4bb2d71a71eabc74fa26?response-content-disp
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/gnu-getopt-2.36.1.catalina.bottle.tar.gz
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/xmlto-0.0.28.catalina.bottle.2.tar.gz
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/shared-mime-info-2.0.catalina.bottle.tar.gz
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/5aefdc7964e569188cb67a49f4a428c64130f7c048ffd55106c656eb0c6caa25?response-content-disp
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/x265-3.4_1.catalina.bottle.tar.gz
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/0e268d680b103353ff708f4514b54f40d5a8793951a1caea1355addcda80450c?response-content-disp
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/libheif-1.10.0.catalina.bottle.tar.gz
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/cfbf48ac25a4a2d5c193837a03ad99abd2097f8be642c1fd234eebe082bdc4da?response-content-disp
######################################################################## 100.0%
==> Installing dependencies for libheif: jpeg, libde265, libpng, pcre, glib, docbook, docbook-xsl, gnu-getopt, xmlto, shared-mime-info and x265
==> Installing libheif dependency: jpeg
==> Pouring jpeg-9d.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/jpeg/9d: 21 files, 775.2KB
==> Installing libheif dependency: libde265
==> Pouring libde265-1.0.8.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/libde265/1.0.8: 22 files, 2.3MB
==> Installing libheif dependency: libpng
==> Pouring libpng-1.6.37.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/libpng/1.6.37: 27 files, 1.2MB
==> Installing libheif dependency: pcre
==> Pouring pcre-8.44.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/pcre/8.44: 204 files, 5.5MB
==> Installing libheif dependency: glib
==> Pouring glib-2.66.4.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/glib/2.66.4: 436 files, 15.5MB
==> Installing libheif dependency: docbook
==> Pouring docbook-5.1_1.catalina.bottle.tar.gz
==> xmlcatalog --noout --create /usr/local/etc/xml/catalog
==> xmlcatalog --noout --del file:///usr/local/opt/docbook/docbook/xml/4.2/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add nextCatalog  file:///usr/local/opt/docbook/docbook/xml/4.2/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --del file:///usr/local/opt/docbook/docbook/xml/4.1.2/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add nextCatalog  file:///usr/local/opt/docbook/docbook/xml/4.1.2/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --del file:///usr/local/opt/docbook/docbook/xml/4.3/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add nextCatalog  file:///usr/local/opt/docbook/docbook/xml/4.3/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --del file:///usr/local/opt/docbook/docbook/xml/4.4/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add nextCatalog  file:///usr/local/opt/docbook/docbook/xml/4.4/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --del file:///usr/local/opt/docbook/docbook/xml/4.5/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add nextCatalog  file:///usr/local/opt/docbook/docbook/xml/4.5/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --del file:///usr/local/opt/docbook/docbook/xml/5.0/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add nextCatalog  file:///usr/local/opt/docbook/docbook/xml/5.0/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --del file:///usr/local/opt/docbook/docbook/xml/5.1/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add nextCatalog  file:///usr/local/opt/docbook/docbook/xml/5.1/catalog.xml /usr/local/etc/xml/catalog
==> Caveats
To use the DocBook package in your XML toolchain,
you need to add the following to your ~/.bashrc:

export XML_CATALOG_FILES="/usr/local/etc/xml/catalog"
==> Summary
🍺  /usr/local/Cellar/docbook/5.1_1: 199 files, 8.9MB
==> Installing libheif dependency: docbook-xsl
==> Pouring docbook-xsl-1.79.2_1.catalina.bottle.tar.gz
==> xmlcatalog --noout --del file:///usr/local/opt/docbook-xsl/docbook-xsl/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add nextCatalog  file:///usr/local/opt/docbook-xsl/docbook-xsl/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --del https://cdn.docbook.org/release/xsl-nons/1.79.2 /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add rewriteSystem https://cdn.docbook.org/release/xsl-nons/1.79.2 file:///usr/local/opt/docbook-xsl/docbook-xsl /usr/loc
==> xmlcatalog --noout --add rewriteURI https://cdn.docbook.org/release/xsl-nons/1.79.2 file:///usr/local/opt/docbook-xsl/docbook-xsl /usr/local/
==> xmlcatalog --noout --del https://cdn.docbook.org/release/xsl-nons/current /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add rewriteSystem https://cdn.docbook.org/release/xsl-nons/current file:///usr/local/opt/docbook-xsl/docbook-xsl /usr/lo
==> xmlcatalog --noout --add rewriteURI https://cdn.docbook.org/release/xsl-nons/current file:///usr/local/opt/docbook-xsl/docbook-xsl /usr/local
==> xmlcatalog --noout --del http://docbook.sourceforge.net/release/xsl/1.79.2 /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add rewriteSystem http://docbook.sourceforge.net/release/xsl/1.79.2 file:///usr/local/opt/docbook-xsl/docbook-xsl /usr/l
==> xmlcatalog --noout --add rewriteURI http://docbook.sourceforge.net/release/xsl/1.79.2 file:///usr/local/opt/docbook-xsl/docbook-xsl /usr/loca
==> xmlcatalog --noout --del http://docbook.sourceforge.net/release/xsl/current /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add rewriteSystem http://docbook.sourceforge.net/release/xsl/current file:///usr/local/opt/docbook-xsl/docbook-xsl /usr/
==> xmlcatalog --noout --add rewriteURI http://docbook.sourceforge.net/release/xsl/current file:///usr/local/opt/docbook-xsl/docbook-xsl /usr/loc
==> xmlcatalog --noout --del file:///usr/local/opt/docbook-xsl/docbook-xsl-ns/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add nextCatalog  file:///usr/local/opt/docbook-xsl/docbook-xsl-ns/catalog.xml /usr/local/etc/xml/catalog
==> xmlcatalog --noout --del https://cdn.docbook.org/release/xsl/1.79.2 /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add rewriteSystem https://cdn.docbook.org/release/xsl/1.79.2 file:///usr/local/opt/docbook-xsl/docbook-xsl-ns /usr/local
==> xmlcatalog --noout --add rewriteURI https://cdn.docbook.org/release/xsl/1.79.2 file:///usr/local/opt/docbook-xsl/docbook-xsl-ns /usr/local/et
==> xmlcatalog --noout --del https://cdn.docbook.org/release/xsl/current /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add rewriteSystem https://cdn.docbook.org/release/xsl/current file:///usr/local/opt/docbook-xsl/docbook-xsl-ns /usr/loca
==> xmlcatalog --noout --add rewriteURI https://cdn.docbook.org/release/xsl/current file:///usr/local/opt/docbook-xsl/docbook-xsl-ns /usr/local/e
==> xmlcatalog --noout --del http://docbook.sourceforge.net/release/xsl-ns/1.79.2 /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add rewriteSystem http://docbook.sourceforge.net/release/xsl-ns/1.79.2 file:///usr/local/opt/docbook-xsl/docbook-xsl-ns
==> xmlcatalog --noout --add rewriteURI http://docbook.sourceforge.net/release/xsl-ns/1.79.2 file:///usr/local/opt/docbook-xsl/docbook-xsl-ns /us
==> xmlcatalog --noout --del http://docbook.sourceforge.net/release/xsl-ns/current /usr/local/etc/xml/catalog
==> xmlcatalog --noout --add rewriteSystem http://docbook.sourceforge.net/release/xsl-ns/current file:///usr/local/opt/docbook-xsl/docbook-xsl-ns
==> xmlcatalog --noout --add rewriteURI http://docbook.sourceforge.net/release/xsl-ns/current file:///usr/local/opt/docbook-xsl/docbook-xsl-ns /u
🍺  /usr/local/Cellar/docbook-xsl/1.79.2_1: 4,910 files, 94.0MB
==> Installing libheif dependency: gnu-getopt
==> Pouring gnu-getopt-2.36.1.catalina.bottle.tar.gz
==> Caveats
gnu-getopt is keg-only, which means it was not symlinked into /usr/local,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have gnu-getopt first in your PATH run:
  echo 'export PATH="/usr/local/opt/gnu-getopt/bin:$PATH"' >> ~/.zshrc

==> Summary
🍺  /usr/local/Cellar/gnu-getopt/2.36.1: 10 files, 199.3KB
==> Installing libheif dependency: xmlto
==> Pouring xmlto-0.0.28.catalina.bottle.2.tar.gz
🍺  /usr/local/Cellar/xmlto/0.0.28: 46 files, 174.3KB
==> Installing libheif dependency: shared-mime-info
==> Pouring shared-mime-info-2.0.catalina.bottle.tar.gz
==> /usr/local/Cellar/shared-mime-info/2.0/bin/update-mime-database /usr/local/share/mime
🍺  /usr/local/Cellar/shared-mime-info/2.0: 86 files, 4.4MB
==> Installing libheif dependency: x265
==> Pouring x265-3.4_1.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/x265/3.4_1: 11 files, 35.8MB
==> Installing libheif
==> Pouring libheif-1.10.0.catalina.bottle.tar.gz
==> /usr/local/opt/shared-mime-info/bin/update-mime-database /usr/local/share/mime
🍺  /usr/local/Cellar/libheif/1.10.0: 24 files, 2.6MB
==> Caveats
==> libffi
libffi is keg-only, which means it was not symlinked into /usr/local,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

For compilers to find libffi you may need to set:
  export LDFLAGS="-L/usr/local/opt/libffi/lib"
  export CPPFLAGS="-I/usr/local/opt/libffi/include"

==> docbook
To use the DocBook package in your XML toolchain,
you need to add the following to your ~/.bashrc:

export XML_CATALOG_FILES="/usr/local/etc/xml/catalog"
==> gnu-getopt
gnu-getopt is keg-only, which means it was not symlinked into /usr/local,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have gnu-getopt first in your PATH run:
  echo 'export PATH="/usr/local/opt/gnu-getopt/bin:$PATH"' >> ~/.zshrc
```
