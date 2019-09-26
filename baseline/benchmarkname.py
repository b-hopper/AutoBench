import wmi

def get_cpu_codename(x):
    name = ""
    if x[3] == '6':
        name = 'SKL '
    elif x[3] == '7':
        name = 'KBL '
    elif x[3] == '8':
        if x[7] == 'U':
            name = 'WHL '
        else:
            name = 'CFL '
    elif x[3] == '9':
        name = 'CFL '
    elif x[3:5] == '10':
        name = 'ICL '
    return name

def get_cpu_nice_name():
    cpu = wmi.WMI().Win32_Processor()[0].name
    cpu = cpu.split()
    name = ""
    
    if "Intel" in cpu[0]:
        name = get_cpu_codename(cpu[2]) + cpu[2]
    elif "AMD" in cpu[0]:
        name = cpu[0] + ' ' + cpu[1] + ' R-' + cpu[2] + ' ' + cpu[3]
    else:
        name = input("CPU name not found. Please input CPU name: ")
    return name
    
def get_gpu_nice_name():
    gpus = wmi.WMI().Win32_VideoController()
    #len(gpus)-1 because integrated will always be index 0, if it's there
    gpu = gpus[len(gpus)-1].name
    return gpu
    
def get_system_model_name():
    mdl = wmi.WMI().Win32_ComputerSystem()[0].model
    return mdl