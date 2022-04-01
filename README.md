# fastapi-advance
FIX ERROR WHEN DEPLOY ON SYSTEM:
<h2>- CentOS 8:</h2>
During run install requirementst.txt, psycopg2 error issue. Follow below solving problem:</br>
Install OKey repository: $yum -y install http://repo.okay.com.mx/centos/8/x86_64/release/okay-release-1-1.noarch.rpm</br>
Install libpq-devel rpm package: $yum -y install libpq-devel


