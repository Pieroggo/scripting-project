@echo off
:menu
echo "       >===>>=====> >======>     >=>       >>       >==>    >=>    >===>    >=>       >=======>   >=>>=>          "
echo "           >=>     >=>    >=>   >=>      >>=>      >> >=>  >=>  >>    >=>  >=>       >=>       >=>    >=>         "
echo "           >=>     >=>    >=>   >=>     >> >=>     >=> >=> >=> >=>         >=>       >=>        >=>               "
echo "           >=>     >> >==>      >=>    >=>  >=>    >=>  >=>>=> >=>         >=>       >=====>      >=>             "
echo "           >=>     >=>  >=>     >=>   >=====>>=>   >=>   > >=> >=>   >===> >=>       >=>             >=>          " 
echo "           >=>     >=>    >=>   >=>  >=>      >=>  >=>    >>=>  >=>    >>  >=>       >=>       >=>    >=>         "
echo "           >=>     >=>      >=> >=> >=>        >=> >=>     >=>   >====>    >=======> >=======>   >=>>=>           "
echo "=================================================================================================================="
echo Welcome to Project Triangles!
echo 1 - Start Python Scripts
echo 2 - Print Info
echo 3 - Make Backup
echo 4 - Exit File
set /p opt=Input a number to pick an option: 
if %opt%==1 goto :start
if %opt%==2 goto :info
if %opt%==3 goto :backup
if %opt%==4 (goto :exit) else (echo Invalid option & goto :exit)
:start
echo Starting...
python triangles.py
python report.py
goto :finish
:info
echo Project v1.0
echo Task: Triangles (IO)
echo Task Overview: For a list of numbers from 1 to 1000000000, check if there is a set of three numbers that could satisfy the traingle condition, else print NIE
goto :finish
:backup
echo Doing backup...
call backup.bat
goto :finish
:finish
set /p cont=Do you want to exit the program? (y/n) 
if %cont%==n (cls & goto :menu)
:exit
echo Exiting...
pause