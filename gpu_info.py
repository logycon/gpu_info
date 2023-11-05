import pynvml
import json

def print_gpu_info():
    gpu_info = []

    pynvml.nvmlInit()
    device_count = pynvml.nvmlDeviceGetCount()

    for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        gpu_name = pynvml.nvmlDeviceGetName(handle)
        gpu_memory = pynvml.nvmlDeviceGetMemoryInfo(handle)
        gpu_info.append({
            'gpu': i + 1,
            'name': gpu_name,
            'memory': {
                'used_mb': gpu_memory.used / 1024**2,
                'total_mb': gpu_memory.total / 1024**2
            }
        })
    pynvml.nvmlShutdown()
    json_str = json.dumps(gpu_info, indent = 4)
    print(json_str)


if __name__ == '__main__':
    print_gpu_info()


