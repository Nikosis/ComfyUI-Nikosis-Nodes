# ComfyUI-Nikosis-Nodes
ComfyUI custom nodes

## How To Install

### **Recommended**
* Install via [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager).

### **Manual**
* Navigate to `ComfyUI/custom_nodes` in your terminal (cmd).
* Clone the repository under the `custom_nodes` directory using the following command:
  ```
  git clone https://github.com/Nikosis/ComfyUI-Nikosis-Nodes comfyui-nikosis-nodes
  cd comfyui-nikosis-nodes
  ```
* Install dependencies in your Python environment.
    * For Windows Portable, run the following command inside `ComfyUI\custom_nodes\comfyui-nikosis-nodes`:
        ```
        ..\..\..\python_embeded\python.exe -m pip install -r requirements.txt
        ```
    * If using venv or conda, activate your Python environment first, then run:
        ```
        pip install -r requirements.txt