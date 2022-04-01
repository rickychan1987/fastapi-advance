# fastapi-advance
FIX ERROR WHEN DEPLOY ON SYSTEM:
- CentOS 8:
During run install requirementst.txt, psycopg2 error issue. Follow below solving problem:
Install OKey repository: $yum -y install http://repo.okay.com.mx/centos/8/x86_64/release/okay-release-1-1.noarch.rpm
Install libpq-devel rpm package: $yum -y install libpq-devel


