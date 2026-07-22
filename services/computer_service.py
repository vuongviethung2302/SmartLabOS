@staticmethod
def sync_host_info(host_info):
    """
    Đồng bộ HostInfo vào Database.
    """

    computer = Computer.query.filter_by(
        ip_address=host_info.ip_address
    ).first()

    if computer is None:

        computer = Computer(
            computer_name=host_info.computer_name,
            room="Unknown",
            vlan=0,
            ip_address=host_info.ip_address,
            mac_address=host_info.mac_address,
            status="Online" if host_info.online else "Offline"
        )

        db.session.add(computer)
        db.session.commit()

    return computer