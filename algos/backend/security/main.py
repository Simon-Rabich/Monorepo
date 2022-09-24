import sys #line:1
from enum import Enum #line:2
from random import choices #line:3
import statistics #line:4
import argparse #line:5
class WindowsVersion (Enum ):#line:6
    WINDOWS11 ="windows11"#line:7
    WINDOWS10 ="windows10"#line:8
    WINDOWS7 ="windows7"#line:9
    WINDOWS_SERVER_2019 ="windows_server_2019"#line:10
    WINDOWS_SERVER_2016 ="windows_server_2016"#line:11
    WINDOWS_SERVER_2012 ="windows_server_2012"#line:12
class AppVersion (Enum ):#line:13
    _56 ="56"#line:14
    _98 ="98"#line:15
    _74 ="74"#line:16
    _35 ="35"#line:17
RUN_PROBABILITY ={WindowsVersion .WINDOWS7 :0.4 ,WindowsVersion .WINDOWS10 :0.95 ,WindowsVersion .WINDOWS11 :0.97 ,WindowsVersion .WINDOWS_SERVER_2019 :0.8 ,WindowsVersion .WINDOWS_SERVER_2012 :0.92 ,WindowsVersion .WINDOWS_SERVER_2016 :0.7 ,AppVersion ._56 :0.98 ,AppVersion ._98 :0.7 ,AppVersion ._74 :0.7 ,AppVersion ._35 :0.6 }#line:18
CHECK_PROBABILITY ={WindowsVersion .WINDOWS7 :0.8 ,WindowsVersion .WINDOWS10 :0.4 ,WindowsVersion .WINDOWS11 :0.96 ,WindowsVersion .WINDOWS_SERVER_2019 :0.85 ,WindowsVersion .WINDOWS_SERVER_2012 :0.98 ,WindowsVersion .WINDOWS_SERVER_2016 :0.7 ,AppVersion ._56 :0.9 ,AppVersion ._98 :0.7 ,AppVersion ._74 :0.99 ,AppVersion ._35 :0.6 }#line:19
class TestModule :#line:20
    def __init__ (OO000O000OO000O00 ,OO000O0O0000OOO0O ,OOOO0OOOO0O000O0O ):#line:21
        OO000O000OO000O00 .__O0OOO0O0OO00OOOOO =OO000O0O0000OOO0O #line:22
        OO000O000OO000O00 .__O00O00O0O000O00OO =OOOO0OOOO0O000O0O #line:23
    def check (O000OOOO0OO00000O )->int :#line:24
        OO000OO0OOO0000O0 =statistics .mean ([CHECK_PROBABILITY [O000OOOO0OO00000O .__O0OOO0O0OO00OOOOO ],CHECK_PROBABILITY [O000OOOO0OO00000O .__O00O00O0O000O00OO ]])#line:25
        return choices ([0 ,1 ],[OO000OO0OOO0000O0 ,1 -OO000OO0OOO0000O0 ])[0 ]#line:26
    def install_plugin (OO0OO00O0O00OOO00 ):#line:27
        O00O0O0OO0OOOOO00 =statistics .mean ([RUN_PROBABILITY [OO0OO00O0O00OOO00 .__O0OOO0O0OO00OOOOO ],RUN_PROBABILITY [OO0OO00O0O00OOO00 .__O00O00O0O000O00OO ]])#line:28
        return choices ([0 ,1 ],[O00O0O0OO0OOOOO00 ,1 -O00O0O0OO0OOOOO00 ])[0 ]#line:29
SUBCOMMAND_INDEX =2 #line:30
COMMAND_INDEX =1 #line:31
def get_arguments_in_case_no_arguments_are_entered ():#line:32
    if sys .argv [COMMAND_INDEX :]:#line:33
        return [sys .argv [COMMAND_INDEX ],'--help']#line:34
    else :#line:35
        return ['--help']#line:36
if __name__ =='__main__':#line:37
    parser =argparse .ArgumentParser (description ='This is the module runner! \n')#line:38
    subparsers =parser .add_subparsers (dest ='command')#line:39
    run =subparsers .add_parser ("install_plugin",help ="installs the plugin")#line:40
    check =subparsers .add_parser ("check",help ="check if the plugin is expected to be installed succesfuly")#line:41
    run .add_argument ("windows_version",type =WindowsVersion ,help =f"one of the following: {', '.join([O0000O000OO0OOO0O.value for O0000O000OO0OOO0O in WindowsVersion])}")#line:42
    run .add_argument ("app_version",type =AppVersion ,help =f"one of the following: {', '.join([OO0O0O0OOOOO00O00.value for OO0O0O0OOOOO00O00 in AppVersion])}")#line:43
    check .add_argument ("windows_version",type =WindowsVersion ,help =f"one of the following: {', '.join([OO0OOO00OO0OOO0O0.value for OO0OOO00OO0OOO0O0 in WindowsVersion])}")#line:44
    check .add_argument ("app_version",type =AppVersion ,help =f"one of the following: {', '.join([OO0OOO000O0O0OOO0.value for OO0OOO000O0O0OOO0 in AppVersion])}")#line:45
    args =parser .parse_args (args =None if sys .argv [SUBCOMMAND_INDEX :]else get_arguments_in_case_no_arguments_are_entered ())#line:46
    sys .exit (getattr (TestModule (args .windows_version ,args .app_version ),args .command )())#line:47
