for %%f in (SDATs\*.sdat) do (
    python sdat.py SDATs\%%~nf.sdat >> InfoDump\%%~nf.txt
)