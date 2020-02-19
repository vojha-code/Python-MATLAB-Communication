%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                             %
%                Communication: From MATALB to Python                         %
%                                                                             %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function ret = communication(a,b)
    [version, executable, isloaded] = pyversion;
    if (isloaded)
        version;
    else
        pyversion 'C:\Users\~\AppData\Local\Continuum\anaconda3\envs\python35\python.exe';    
    end  
    if count(py.sys.path,'') == 0
        insert(py.sys.path,int32(0),'');
    end
    %ret = pwd;
    c = py.pymodule.add2(5,5); % current dir
    d = py.subdir.pymodule1.add3(2,3); % sub dir
    %e = py.subdir.subsubdir.pymodule2.add4(2,3); % subsubdir doesn't work
    ret = a + b + c + d;
end
