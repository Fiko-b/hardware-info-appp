import streamlit as st
import platform
import psutil
import shutil

def get_hardware_info():
    uname = platform.uname()
    cpu_info = f"{uname.processor} ({psutil.cpu_count(logical=False)} cores / {psutil.cpu_count()} threads)"
    ram = f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB"
    disk_total, _, disk_free = shutil.disk_usage("/")
    disk_info = f"Total: {round(disk_total / (1024**3), 2)} GB, Free: {round(disk_free / (1024**3), 2)} GB"

    return {
        "System": uname.system,
        "Node Name": uname.node,
        "Release": uname.release,
        "Version": uname.version,
        "Machine": uname.machine,
        "Processor": cpu_info,
        "RAM": ram,
        "Disk": disk_info
    }

def main():
    st.title("🖥️ Hardware Information Viewer")
    st.write("This app shows basic hardware information using Python.")

    if st.button("🔄 Refresh"):
        st.rerun()

    info = get_hardware_info()
    for key, value in info.items():
        st.write(f"**{key}:** {value}")

if __name__ == "__main__":
    main()
