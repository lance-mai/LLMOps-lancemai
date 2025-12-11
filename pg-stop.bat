@echo off
set PG_PATH="G:\PostgreSQL\16\bin"
set PG_DATA="G:\PostgreSQL\16\data"

echo Stoping PostgreSQL...
%PG_PATH%\pg_ctl.exe stop -D %PG_DATA%
echo PostgreSQL Stoped.