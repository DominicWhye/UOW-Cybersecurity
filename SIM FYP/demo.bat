@echo off
setlocal enableextensions enabledelayedexpansion

REM Always run from the folder where this .bat lives
cd /d "%~dp0"

REM - Locate Python (prefer the repo-local .venv) -
set "VENV_PY=%~dp0.venv\Scripts\python.exe"
set "PY="

if exist "%VENV_PY%" (
    set "PY=%VENV_PY%"
) else (
    for /f "delims=" %%P in ('where python 2^>nul') do (
        if not defined PY set "PY=%%P"
    )
)

if not defined PY (
    echo.
    echo  ERROR: Python not found.
    echo  Create the virtual environment first:
    echo      python -m venv .venv
    echo      .venv\Scripts\python -m pip install -r requirements.txt
    echo  Expected venv path: %VENV_PY%
    echo.
    pause
    exit /b 1
)

echo  [init] Python: %PY%

REM - Verify Python runs -
"%PY%" --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo  ERROR: Python found but cannot execute: %PY%
    echo.
    pause
    exit /b 1
)

REM - .env check -
if not exist "%~dp0.env" (
    echo.
    echo  ERROR: .env not found at %~dp0
    echo  Create a .env file with at least DATABASE_URL set, e.g.:
    echo      DATABASE_URL=postgresql://fyp_user:fyp_user@localhost:5432/fyp_database
    echo.
    pause
    exit /b 1
)

REM - Dependency check -
"%PY%" -c "import fastapi, uvicorn, cv2, psycopg2, insightface" >nul 2>&1
if errorlevel 1 (
    echo  [setup] Installing dependencies, please wait...
    "%PY%" -m pip install -r "%~dp0requirements.txt"
    if errorlevel 1 (
        echo.
        echo  ERROR: pip install failed.
        echo.
        pause
        exit /b 1
    )
)

REM -
:MAIN_MENU
cls
echo.
echo  +--------------------------------------------------+
echo  ^|  FYP-26-S2-17  Attendance AI   Demo Launcher     ^|
echo  +--------------------------------------------------+
echo.
echo    [1]  Start Web API       -- FastAPI server on 127.0.0.1:8000
echo    [2]  Serve frontend      -- static files on 127.0.0.1:5500
echo    [3]  Start full demo     -- API (new window) + frontend + browser
echo    [4]  Health check        -- GET /health on the running API
echo    [5]  Setup database      -- apply schema.sql + demo seed (first run)
echo    [0]  Exit
echo.
echo    Note: the API needs a reachable PostgreSQL (pgvector) at DATABASE_URL.
echo          First time? Run [5] once to create the schema and demo data.
echo.

set "CHOICE="
set /p "CHOICE=  Select [0-5]: "

if "!CHOICE!"=="0" goto :END
if "!CHOICE!"=="1" goto :MODE_WEB
if "!CHOICE!"=="2" goto :MODE_FRONTEND
if "!CHOICE!"=="3" goto :MODE_FULL
if "!CHOICE!"=="4" goto :MODE_HEALTH
if "!CHOICE!"=="5" goto :MODE_DB
echo  Invalid choice, try again.
timeout /t 1 >nul
goto :MAIN_MENU

REM -
:MODE_WEB
echo.
echo  [demo] Launching FastAPI server at http://127.0.0.1:8000 ...
echo  (API docs: http://127.0.0.1:8000/docs  -  Press Ctrl+C to stop)
echo.
"%PY%" -m uvicorn main_api:app --host 127.0.0.1 --port 8000
goto :DONE

:MODE_FRONTEND
echo.
echo  [demo] Serving frontend at http://127.0.0.1:5500 ...
echo  (Make sure the Web API (option 1) is also running in another window)
echo  (Press Ctrl+C to stop)
echo.
"%PY%" -m http.server 5500 --directory "%~dp0frontend"
goto :DONE

:MODE_FULL
echo.
echo  [demo] Starting API in a new window...
start "FYP Web API" cmd /k ""%PY%" -m uvicorn main_api:app --host 127.0.0.1 --port 8000"
echo  [demo] Waiting for the API to come up...
timeout /t 5 >nul
echo  [demo] Opening browser at http://127.0.0.1:5500 ...
start "" "http://127.0.0.1:5500/index.html"
echo  [demo] Serving frontend (Press Ctrl+C to stop the frontend)...
echo.
"%PY%" -m http.server 5500 --directory "%~dp0frontend"
goto :DONE

:MODE_HEALTH
echo.
echo  [demo] GET http://127.0.0.1:8000/health ...
"%PY%" -c "import urllib.request,sys; print(urllib.request.urlopen('http://127.0.0.1:8000/health',timeout=5).read().decode())" 2>nul
if errorlevel 1 (
    echo  Could not reach the API. Start it first with option 1.
)
goto :DONE

:MODE_DB
echo.
echo  [db] Initialising the database (schema + demo seed)...
echo.

REM - psql is required to apply the SQL (seed uses psql meta-commands) -
where psql >nul 2>&1
if errorlevel 1 (
    echo  ERROR: psql not found on PATH.
    echo  Install the PostgreSQL client tools, or apply the SQL manually:
    echo      psql "DATABASE_URL" -f database\schema.sql
    echo      psql "DATABASE_URL" -v demo_password_hash="HASH" -f database\seed_demo.sql
    goto :DONE
)

REM - Read DATABASE_URL out of .env (first match wins) -
set "DBURL="
for /f "usebackq tokens=1,* delims==" %%A in ("%~dp0.env") do (
    if /i "%%A"=="DATABASE_URL" if not defined DBURL set "DBURL=%%B"
)
if not defined DBURL (
    echo  ERROR: DATABASE_URL not found in .env
    goto :DONE
)

REM - Destructive guard: seed_demo.sql DELETEs all data before re-seeding.
REM   .env may point at a LIVE/remote database (e.g. Supabase), so confirm.
echo.
echo  ************************* WARNING *************************
echo   This RESETS the database in your .env: it DELETES all
echo   existing data and re-inserts demo data. If DATABASE_URL
echo   points at your LIVE Supabase, that data will be wiped.
echo  **********************************************************
echo.
set "CONFIRM="
set /p "CONFIRM=  Type YES to proceed (anything else cancels): "
if /i not "!CONFIRM!"=="YES" (
    echo  Cancelled. No changes made.
    goto :DONE
)

REM - Generate the Argon2id hash for the demo password (demo123) -
echo  [db] Generating Argon2id hash for the demo accounts...
"%PY%" -c "from argon2 import PasswordHasher, Type; open(r'%TEMP%\fyp_pw.txt','w').write(PasswordHasher(type=Type.ID, memory_cost=65536, time_cost=3, parallelism=4).hash('demo123'))"
if errorlevel 1 (
    echo  ERROR: could not generate password hash ^(is argon2-cffi installed?^).
    goto :DONE
)
set "PWHASH="
set /p "PWHASH="<"%TEMP%\fyp_pw.txt"
del "%TEMP%\fyp_pw.txt" >nul 2>&1
if not defined PWHASH (
    echo  ERROR: password hash came back empty.
    goto :DONE
)

REM - Ensure pgvector exists (no-op if already enabled, e.g. on Supabase).
REM   Requires the pgvector extension to be installed on the PG server.
echo  [db] Enabling pgvector extension...
psql "!DBURL!" -v ON_ERROR_STOP=1 -c "CREATE EXTENSION IF NOT EXISTS vector;"
if errorlevel 1 (
    echo.
    echo  ERROR: could not enable pgvector. Is the extension installed on the
    echo         PostgreSQL server? ^(Supabase has it built in.^)
    goto :DONE
)

REM - Apply schema, then the demo seed with the injected hash -
echo  [db] Applying database\schema.sql ...
psql "!DBURL!" -v ON_ERROR_STOP=1 -f "%~dp0database\schema.sql"
if errorlevel 1 (
    echo.
    echo  ERROR: schema.sql failed to apply. See the psql output above.
    goto :DONE
)

echo  [db] Applying database\seed_demo.sql ...
psql "!DBURL!" -v ON_ERROR_STOP=1 -v demo_password_hash=!PWHASH! -f "%~dp0database\seed_demo.sql"
if errorlevel 1 (
    echo.
    echo  ERROR: seed_demo.sql failed to apply. See the psql output above.
    goto :DONE
)

echo.
echo  [db] Done. Demo accounts created (password: demo123).
echo       e.g. admin@demo.local / demo123
goto :DONE

REM -
:DONE
echo.
if "!ERRORLEVEL!"=="0" (echo  Done.) else (echo  Exited with code !ERRORLEVEL!.)
echo.
pause
goto :MAIN_MENU

:END
echo.
echo  Goodbye.
pause
endlocal
exit /b 0
