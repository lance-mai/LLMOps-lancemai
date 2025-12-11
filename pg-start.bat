@echo off
set PG_PATH="G:\PostgreSQL\16\bin"
set PG_DATA="G:\PostgreSQL\16\data"

echo Starting PostgreSQL...
%PG_PATH%\pg_ctl.exe start -D %PG_DATA%
echo PostgreSQL Started.