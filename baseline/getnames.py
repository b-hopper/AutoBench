import benchmarkname

cpu = benchmarkname.get_cpu_nice_name()
gpu = benchmarkname.get_gpu_nice_name()
name = benchmarkname.get_system_model_name()
print('\nName: ' + name)
print('CPU: ' + cpu)
print('GPU: ' + gpu)

print('Path: results\\' + cpu + '\\1080p ' + gpu + ' ' + name + '\\')
input("")