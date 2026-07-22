"""
Danh sách các Command chuẩn của SmartLab OS.
Server và Agent phải sử dụng thống nhất.
"""


class Command:

    # Không có lệnh
    NONE = "none"

    # Heartbeat
    HEARTBEAT = "heartbeat"

    # Quản lý nguồn
    SHUTDOWN = "shutdown"
    RESTART = "restart"
    WAKE_ON_LAN = "wake_on_lan"

    # Thông tin hệ thống
    GET_SYSTEM_INFO = "get_system_info"

    # Điều khiển
    RUN_COMMAND = "run_command"

    # Quản lý file
    COPY_FILE = "copy_file"
    DELETE_FILE = "delete_file"

    # Cài đặt phần mềm
    INSTALL_SOFTWARE = "install_software"
    UNINSTALL_SOFTWARE = "uninstall_software"

    # Cập nhật Agent
    UPDATE_AGENT = "update_agent"