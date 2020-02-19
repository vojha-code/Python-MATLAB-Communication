%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                             %
%                Communication: From MATALB to Python                         %
%                                                                             %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[version, executable, isloaded] = pyversion;
if (isloaded)
    version;
else
    pyversion 'C:\Users\~\AppData\Local\Continuum\anaconda3\envs\python35\python.exe';    
end  
if count(py.sys.path,'') == 0
    insert(py.sys.path,int32(0),'');
end
% check current working directory 
ret = pwd
% call python module
py.pymodule.add0()
py.pymodule.add1(5)
py.pymodule.add2(10,5)