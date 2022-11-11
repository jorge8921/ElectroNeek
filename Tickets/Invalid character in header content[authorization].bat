@echo off
cd %userprofile%\AppData\Roaming\ElectroNeek\studio
if exist electroneek_license_key_3.0 (
    rem file exists
    echo "Existe electroneek_license_key_3.0"
    del electroneek_license_key_3.0
) else (
    rem file doesn't exist
)

if exist use_proxy (
    rem file exists
    del use_proxy
) else (
    rem file doesn't exist
)
pause