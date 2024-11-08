#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-triebeard
Version  : 0.4.1
Release  : 44
URL      : https://cran.r-project.org/src/contrib/triebeard_0.4.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/triebeard_0.4.1.tar.gz
Summary  : 'Radix' Trees in 'Rcpp'
Group    : Development/Tools
License  : MIT
Requires: R-triebeard-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R

%description
to hash tables. 'triebeard' provides an implementation of 'radix trees' for use in R programming and in
             developing packages with 'Rcpp'.

%package lib
Summary: lib components for the R-triebeard package.
Group: Libraries

%description lib
lib components for the R-triebeard package.


%prep
%setup -q -n triebeard
cd %{_builddir}/triebeard

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678827775

%install
export SOURCE_DATE_EPOCH=1678827775
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/triebeard/DESCRIPTION
/usr/lib64/R/library/triebeard/INDEX
/usr/lib64/R/library/triebeard/LICENSE
/usr/lib64/R/library/triebeard/Meta/Rd.rds
/usr/lib64/R/library/triebeard/Meta/features.rds
/usr/lib64/R/library/triebeard/Meta/hsearch.rds
/usr/lib64/R/library/triebeard/Meta/links.rds
/usr/lib64/R/library/triebeard/Meta/nsInfo.rds
/usr/lib64/R/library/triebeard/Meta/package.rds
/usr/lib64/R/library/triebeard/Meta/vignette.rds
/usr/lib64/R/library/triebeard/NAMESPACE
/usr/lib64/R/library/triebeard/NEWS
/usr/lib64/R/library/triebeard/R/triebeard
/usr/lib64/R/library/triebeard/R/triebeard.rdb
/usr/lib64/R/library/triebeard/R/triebeard.rdx
/usr/lib64/R/library/triebeard/doc/index.html
/usr/lib64/R/library/triebeard/doc/r_radix.R
/usr/lib64/R/library/triebeard/doc/r_radix.Rmd
/usr/lib64/R/library/triebeard/doc/r_radix.html
/usr/lib64/R/library/triebeard/doc/rcpp_radix.R
/usr/lib64/R/library/triebeard/doc/rcpp_radix.Rmd
/usr/lib64/R/library/triebeard/doc/rcpp_radix.html
/usr/lib64/R/library/triebeard/help/AnIndex
/usr/lib64/R/library/triebeard/help/aliases.rds
/usr/lib64/R/library/triebeard/help/paths.rds
/usr/lib64/R/library/triebeard/help/triebeard.rdb
/usr/lib64/R/library/triebeard/help/triebeard.rdx
/usr/lib64/R/library/triebeard/html/00Index.html
/usr/lib64/R/library/triebeard/html/R.css
/usr/lib64/R/library/triebeard/include/radix.h
/usr/lib64/R/library/triebeard/include/radix/radix_tree.hpp
/usr/lib64/R/library/triebeard/include/radix/radix_tree_it.hpp
/usr/lib64/R/library/triebeard/include/radix/radix_tree_node.hpp
/usr/lib64/R/library/triebeard/tests/testthat.R
/usr/lib64/R/library/triebeard/tests/testthat/test_alter.R
/usr/lib64/R/library/triebeard/tests/testthat/test_convert.R
/usr/lib64/R/library/triebeard/tests/testthat/test_create.R
/usr/lib64/R/library/triebeard/tests/testthat/test_get.R
/usr/lib64/R/library/triebeard/tests/testthat/test_greedy.R
/usr/lib64/R/library/triebeard/tests/testthat/test_longest.R
/usr/lib64/R/library/triebeard/tests/testthat/test_prefix.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/triebeard/libs/triebeard.so
/usr/lib64/R/library/triebeard/libs/triebeard.so.avx2
/usr/lib64/R/library/triebeard/libs/triebeard.so.avx512
