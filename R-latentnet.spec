%global packname  latentnet
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.4.5
Release:          1
Summary:          Latent position and cluster models for statistical networks
Group:            Sciences/Mathematics
License:          file LICENSE
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/latentnet_2.4-5.tar.gz
Requires:         R-network R-shapes R-abind R-tools R-mvtnorm R-coda
Requires:         R-KernSmooth R-snowFT R-ergm R-rgl
Requires:         R-statnet.common
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-network R-shapes R-abind R-tools R-mvtnorm R-coda
BuildRequires:    R-KernSmooth R-snowFT R-ergm R-rgl
BuildRequires:    R-statnet.common
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
A package to fit and simulate latent position and cluster models for
statistical networks.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# FIXME Should eventually finish on i586, but after 5 hours at 100% cpu
# did not finish. Works fine on x86_64, so, could beh a real problem
# that only happens in i586.
%ifarch 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
